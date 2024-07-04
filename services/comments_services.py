# from fastapi import HTTPException, status, Depends
# from sqlalchemy.orm import Session
# from core.comments_database import get_db
# from core.comments_models import Comment
# from schemas.comment_schemas import CommentSchema

# class CommentService:

#     @staticmethod
#     async def create_comment(request: CommentSchema, db):
#         new_comment = Comment(name=request.name, content=request.content)
#         db.add(new_comment)
#         db.commit()
#         db.refresh(new_comment)
#         return new_comment

#     @staticmethod
#     async def get_comment(comment_id: int, db_session):
#         return db_session.query(Comment).filter(Comment.id == comment_id).first()

#     @staticmethod
#     async def get_comments(db):
#         all_comments = db.query(Comment).all()
#         return all_comments

#     #update content
#     @staticmethod
#     async def update_comment(id: int, content: str, db):
#         updated_post = db.query(Comment).filter(Comment.id == id).first()
#         if not updated_post:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

#         updated_post.content = content
#         db.commit()
#         db.refresh(updated_post)
#         return updated_post

#     #update name
#     @staticmethod
#     async def update_comment_name(id: int, name: str, db):
#         updated_post = db.query(Comment).filter(Comment.id == id).first()
#         if not updated_post:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

#         updated_post.name = name
#         db.commit()
#         db.refresh(updated_post)
#         return updated_post

#     @staticmethod
#     async def delete_comment(id: int, db):
#         delete_post = db.query(Comment).filter(Comment.id == id).first()
#         if not delete_post:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

#         db.delete(delete_post)
#         db.commit()
#         return delete_post