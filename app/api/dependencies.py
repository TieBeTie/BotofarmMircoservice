from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from .services import UserService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)