from fastapi import FastAPI
from app.database import Base, engine
from app.routers import posts
from fastapi.staticfiles import StaticFiles
import logging

# Logger
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Auto create all tables from models

app = FastAPI(title="Hackathon ORM App", version="1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def root():
    logger.info("Root hit")
    return {"message": "ORM API running 🚀"}