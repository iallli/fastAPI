from sqlalchemy import Column, String, Integer
from database import Base

#   Model
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    body = Column(String, unique=True, index=True)
