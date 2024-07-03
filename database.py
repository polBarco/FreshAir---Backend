
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker


DATABASE_URL= "sqlite:///user_comments.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    idx = Column(Integer)

def create_comment(content: str):
    db = SessionLocal()
    new_comment = Comment(content=content)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all_comments(skip: int = 0, limit: int = 10):
    db = SessionLocal()

    return db.query(Comment).offset(skip)

# Create the tables in the database
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Database tables created.")

