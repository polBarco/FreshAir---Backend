from fastapi import FastAPI, Depends, HTTPException
from starlette import status

import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Comment
from schemas import CommentSchema

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()



@app.post("/comment")
def create_comment(request: CommentSchema, db: Session = Depends(get_db)):
    new_comment = Comment(name=request.name, content=request.content)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


#no funciona
@app.get("/comment/{id}")
def get_comment(comment_id: int, db_session):
    return db_session.query(Comment).filter(Comment.id == comment_id).first()

@app.get("/comments")
def get_comments(db: Session = Depends(get_db)):
    all_comments = db.query(models.Comment).all()
    return all_comments



@app.put("/update/{id}")
def update_comment(id: int, content: str, db:Session=Depends(get_db)):
    updated_post = db.query(Comment).filter(Comment.id == id).first()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    updated_post.content = content
    db.commit()
    db.refresh(updated_post)
    return updated_post

@app.put("/updatename/{id}")
def update_comment(id: int, name: str, db:Session=Depends(get_db)):
    updated_post = db.query(Comment).filter(Comment.id == id).first()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    updated_post.name = name
    db.commit()
    db.refresh(updated_post)
    return updated_post

@app.delete("/delete/{id}")
def delete_comment(id: int, db: Session = Depends(get_db)):

    delete_post = db.query(Comment).filter(Comment.id == id).first()
    if not delete_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    db.delete(delete_post)
    db.commit()
    return delete_post



@app.get("/")
def home():
    return {"message": "Hello, World!"}
