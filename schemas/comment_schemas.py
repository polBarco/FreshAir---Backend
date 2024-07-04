from datetime import time
from pydantic import BaseModel

class CommentSchema(BaseModel):
    id:int
    name:str
    content:str
    #added_at:time

class Config:
    """allows the model to work seamlessly with SQLAlchemy models.
    This setting ensures that SQLAlchemy objects can be converted to Pydantic models and vice versa."""
    orm_mode = True