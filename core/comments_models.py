from sqlalchemy import Column, Integer, String, TIMESTAMP, text

from core.comments_database import Base



class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))
