from fastapi import Depends
from sqlalchemy.orm import Session
from db.session import get_db
from .services import UserService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    """
    Returns an instance of the UserService class.

    Parameters:
    - db: The database session.

    Returns:
    An instance of the UserService class.
    """
    return UserService(db)
