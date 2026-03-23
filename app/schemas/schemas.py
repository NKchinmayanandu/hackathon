from pydantic import BaseModel, Field
from typing import Optional, List
from pydantic import Field
# inside schemas (same file is fine)

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class PredictRequest(BaseModel):
    query: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

# ── User Schemas ──────────────────────────────
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int

    posts: List["PostResponse"] = Field(default_factory=list)
    class Config:
        from_attributes = True


# ── Post Schemas ──────────────────────────────
class PostCreate(BaseModel):
    title: str
    content: str
    value: Optional[float] = 0.0
    owner_id: int

class PostResponse(PostCreate):
    id: int

    class Config:
        from_attributes = True


# Needed for forward reference in UserResponse
UserResponse.model_rebuild()
