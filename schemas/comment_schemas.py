from pydantic import BaseModel

class CommentSchema(BaseModel):
    id: int
    name: str
    content: str

    class Config:
        orm_mode = True
