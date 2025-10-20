from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    
class PostCreate(PostBase):
    author_id: int

class PostResponse(PostBase):
    id: int
    date: datetime
    author_id: int

    class Config:
        from_attributes = True