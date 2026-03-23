from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, posts
import logging
from app.logging_config import setup_logging
from fastapi.staticfiles import StaticFiles

setup_logging()
app = FastAPI(title="Hackathon ORM App", version="1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Logger
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Auto create all tables from models
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])

@app.get("/")
def root():
    logger.info("Root hit")
    return {"message": "ORM API running 🚀"}
