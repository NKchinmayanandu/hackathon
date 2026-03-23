from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class PredictRequest(BaseModel):
    query: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


class PostCreate(BaseModel):
    title: str
    content: str
    value: Optional[float] = 0.0
    owner_id: int

class PostResponse(PostCreate):
    id: int

    class Config:
        from_attributes = True


