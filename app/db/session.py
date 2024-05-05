from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base

engine = create_engine(
    Base.SQLALCHEMY_DATABASE_URL
)

def get_db():
    db = Base.SessionLocal()
    try:
        yield db
    finally:
        db.close()