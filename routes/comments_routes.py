# from fastapi import FastAPI, Depends, HTTPException
# from starlette import status
# from core.comments_database import get_db
# from sqlalchemy.orm import Session
# from fastapi import APIRouter
# from core.comments_models import Comment
# from schemas.comment_schemas import CommentSchema
# from services.comments_services import CommentService

# router = APIRouter()

# @router.post("/comment", response_model=CommentSchema)
# async def create_comment(request: CommentSchema, db: Session = Depends(get_db)):
#     new_comment = CommentService.create_comment(request, db)
#     return new_comment

# @router.get("/comment/{id}", response_model=CommentSchema)
# async def get_comment(comment_id: int, db_session):
#     comment = CommentService.get_comment(comment_id, db_session)
#     return comment

# @router.get("/comments", response_model=list[CommentSchema])
# async def get_comments(db: Session = Depends(get_db)):
#     all_comments = CommentService.get_comments(db)
#     return all_comments

# #update content
# @router.put("/update/{id}", response_model=CommentSchema)
# async def update_comment(id: int, content: str, db:Session=Depends(get_db)):
#     updated_post = CommentService.update_comment(id, content, db)
#     return updated_post

# #update name
# @router.put("/updatename/{id}", response_model=CommentSchema)
# async def update_comment_name(id: int, name: str, db:Session=Depends(get_db)):
#     updated_post = CommentService.update_comment_name(id, name, db)
#     return updated_post

# @router.delete("/delete/{id}", response_model=CommentSchema)
# async def delete_comment(id: int, db: Session = Depends(get_db)):
#     delete_post = CommentService.delete_comment(id, db)
#     return delete_post