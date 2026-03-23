from app.services.task_logger import log_task
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Post
from app.schemas.schemas import PostCreate, PostResponse, PredictRequest
from app.services.ml import predict_ml
from app.services.rules import predict_rule
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


from app.services.task_logger import log_task
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Post
from app.schemas.schemas import PostCreate, PostResponse, PredictRequest
from app.services.ml import predict_ml
from app.services.rules import predict_rule
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/predict")
def predict(data: PredictRequest):
    if not data.query:
        return {"error": "Invalid input"}

    # STEP 1: Try rules FIRST (cheap)
    rule_result = predict_rule({"query": data.query})

    if rule_result and rule_result.get("result") != "unknown":
        result = rule_result
    else:
        result = predict_ml({"query": data.query})

    log = log_task(data.query, result)

    return {
        "result": result,
        "log": log
    }
import json

@router.get("/export")
def export_logs():
    try:
        with open("logs/tasks.json", "r") as f:
            data = json.load(f)
        return {
            "message": "Logs ready for blockchain anchoring",
            "data": data
        }
    except:
        return {"error": "No logs found"}
    



