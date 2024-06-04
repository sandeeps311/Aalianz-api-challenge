from pydantic import BaseModel
from datetime import datetime


# Comment model
class Comment(BaseModel):
    id: str
    text: str
    created_at: datetime


# Comment response schema
class CommentResponse(BaseModel):
    id: str
    text: str
    polarity: float
    classification: str
