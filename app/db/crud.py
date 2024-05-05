from sqlalchemy.orm import Session
from .models import User
from sqlalchemy.orm import Session
from .models import User
from typing import List

class CRUD:
    def __init__(self, db: Session):
        self.db = db
        
    def get_user_by_id(self, id: int) -> User:
        """Retrieve a user by their ID."""
        return self.db.query(User).filter(User.id == id).first()
    
    def get_users(self) -> List[User]:
        """Retrieve all users."""
        return self.db.query(User).all()

    def create(self, data: dict) -> int:
        """Create a new user."""
        db_item = User(**data) 
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item.id

    def update(self, id: int, data: dict) -> User:
        """Update a user by their ID."""
        item = self.db.query(User).filter(User.id == id).first() 
        for key, value in data.items():
            setattr(item, key, value)
        self.db.commit()
        return item

    def delete(self, id: int) -> int:
        """Delete a user by their ID."""
        item = self.db.query(User).filter(User.id == id).first()
        self.db.delete(item)
        self.db.commit()
        return id
