from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Comment

from fastapi import HTTPException, status



class CommentService:

    @staticmethod
    def get_comment(id: int, db):
        comment = db.query(Comment).filter(Comment.id == id).first()
        print(comment.id, comment.text, comment.author_id, comment.film_id)
        return comment

    @staticmethod
    def get_comments_for_film(film_id: str, db):
        return db.query(Comment).filter(Comment.film_id == film_id).all()

    @staticmethod
    def get_comments_for_author(author_id: int, db):
        return db.query(Comment).filter(Comment.author_id == author_id).all()

    @staticmethod
    def post_comment(text: str, author_id: int, film_id: int, db, current_user):
        comment = Comment(text=text, author_id=author_id, film_id=film_id)

        if current_user.id != author_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You do not have permission to post a comment")

        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    @staticmethod
    def put_comment(id: int, text: str, db, current_user):
        comment = db.query(Comment).filter(Comment.id == id).first()

        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

        # Verificar si el usuario tiene permiso para actualizar el comentario
        if comment.author_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You do not have permission to update this comment")

        comment.text = text
        db.commit()
        db.refresh(comment)
        return comment

    @staticmethod
    def delete_comment(id: int, db, current_user):
        comment = db.query(Comment).filter(Comment.id == id).first()

        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

        # Verificar si el usuario tiene permiso para actualizar el comentario
        if comment.author_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You do not have permission to update this comment")

        db.delete(comment)
        db.commit()
        return comment