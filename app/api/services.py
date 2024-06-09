from db.crud import CRUD
from db.models import User
from db.crud import CRUD
from db.models import User
from typing import Optional
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session


class UserService:
    """
    Service class for managing user operations.
    """

    def __init__(self, db: Session):
        self.crud = CRUD(db)

    def create_user(self, user: User) -> UUID:
        """
        Create a new user.

        Args:
            user (User): The user object to create.

        Returns:
            int: The ID of the created user.
        """
        user_id = self.crud.create(user.dict())
        return user_id
    
    def get_users(self) -> List[User]:
        """
        Get all users.

        Returns:
            List[User]: A list of all users.
        """
        return self.crud.get_users()

    def acquire_lock(self, user_id: str) -> bool:
        """
        Acquire a lock on a user.

        Args:
            user_id (str): The ID of the user to lock.

        Returns:
            Optional[User]: The locked user object, or None if the user does not exist.
        """
        user = self.crud.get_user_by_id(user_id)
        if user is not None:
            user.locked = True
            self.db.commit()
            return user
        return None
    
    def release_lock(self, user_id: str) -> bool:
        """
        Release a lock on a user.

        Args:
            user_id (str): The ID of the user to release the lock.

        Returns:
            Optional[User]: The unlocked user object, or None if the user does not exist.
        """
        user = self.crud.get_user_by_id(user_id)
        if user is not None:
            user.locked = False
            self.db.commit()
            return user
        return None
