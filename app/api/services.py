from sqlalchemy.orm import Session
from app.db.crud import CRUD
from app.api.models import User
from app.api.schemas import UserCreate


class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        user_id = CRUD(db).create(user.dict())
        return user_id
        
    @staticmethod
    def get_users(db: Session):
        return CRUD(db).get_users(db)

    @staticmethod
    def acquire_lock(db: Session, user_id: str):
        user = CRUD(db).get_user_by_id(db, user_id)
        if user is not None:
            user.locked = True
            db.commit()
            return user
        return None

    @staticmethod
    def release_lock(db: Session, user_id: str):
        user = CRUD(db).get_user_by_id(db, user_id)
        if user is not None:
            user.locked = False
            db.commit()
            return user
        return None