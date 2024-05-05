from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db, get_user_service 
from app.api.schemas import UserCreate, UserList, UserLock
from app.api.services import UserService

router = APIRouter()


@router.post("/users", response_model=UserList)
def create_user(user: UserCreate, db: Session = Depends(get_db), user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(db, user)


@router.get("/users", response_model=UserList)
def get_users(db: Session = Depends(get_db), user_service: UserService = Depends(get_user_service)):
    return user_service.get_users(db)


@router.put("/users/{user_id}/lock", response_model=UserLock)
def acquire_lock(user_id: str, db: Session = Depends(get_db), user_service: UserService = Depends(get_user_service)):
    return user_service.acquire_lock(db, user_id)


@router.delete("/users/{user_id}/lock", response_model=UserLock)
def release_lock(user_id: str, db: Session = Depends(get_db), user_service: UserService = Depends(get_user_service)):
    return user_service.release_lock(db, user_id)