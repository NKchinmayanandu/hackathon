from pydantic import BaseModel
from typing import Optional, List

# ── User Schemas ──────────────────────────────
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int
    posts: List["PostResponse"] = []

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
