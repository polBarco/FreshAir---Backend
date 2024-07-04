from sqlalchemy import Column, Integer, String
from core.comments_database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    content = Column(String, nullable=False)
