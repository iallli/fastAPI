from pydantic import BaseModel
from database import Engine, SessionLocal, Base

#   Schema
class UserSchema(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=Engine)
