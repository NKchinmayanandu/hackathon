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
    if data.query:
        if len(data.query.split()) > 3:
            return predict_ml({"query": data.query})
        else:
            return predict_rule({"query": data.query})
    return {"error": "Invalid input"}


@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    logger.info(f"Created post: {db_post.id}")
    return db_post


@router.get("/", response_model=list[PostResponse])
def get_all_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, updated: PostCreate, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    for key, value in updated.model_dump().items():
        setattr(post, key, value)
    db.commit()
    db.refresh(post)
    logger.info(f"Updated post: {post_id}")
    return post


@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    logger.info(f"Deleted post: {post_id}")
    return {"message": "Post deleted successfully"}


@router.get("/user/{user_id}", response_model=list[PostResponse])
def get_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.owner_id == user_id).all()

@router.post("/predict")
def predict(data: PredictRequest):
    return predict_ml({"query": data.query})

