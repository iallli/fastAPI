from pydantic import BaseModel
from database import Engine, SessionLocal, Base

#   Schema


class BlogSchema(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=Engine)
