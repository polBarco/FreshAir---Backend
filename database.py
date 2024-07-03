from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///user_comments.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)

def create_comment(content: str, db_session):
    new_comment = Comment(content=content)
    db_session.add(new_comment)
    db_session.commit()
    db_session.refresh(new_comment)
    return new_comment

def get_comment(comment_id: int, db_session):
    return db_session.query(Comment).filter(Comment.id == comment_id).first()

def get_comments(skip: int = 0, limit: int = 10, db_session=None):
    return db_session.query(Comment).offset(skip).limit(limit).all()

def update_comment(comment_id: int, new_content: str, db_session):
    comment = db_session.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        comment.content = new_content
        db_session.commit()
        db_session.refresh(comment)
        return comment
    return None

def delete_comment(comment_id: int, db_session):
    comment = db_session.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        db_session.delete(comment)
        db_session.commit()
        return True
    return False

def init_db():
    Base.metadata.create_all(engine)

