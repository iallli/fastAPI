from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DB_URL = "sqlite:///./sql_app.db"
Engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, bind=Engine)
Base = declarative_base()
