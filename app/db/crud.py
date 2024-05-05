from sqlalchemy.orm import Session
from .models import User

class CRUD:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data):
        db_item = User(**data) 
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item.id

    def read(self, id):
        return self.db.query(User).filter(User.id == id).first()  

    def update(self, id, data):
        item = self.db.query(User).filter(User.id == id).first() 
        for key, value in data.items():
            setattr(item, key, value)
        self.db.commit()
        return item

    def delete(self, id):
        item = self.db.query(User).filter(User.id == id).first()
        self.db.delete(item)
        self.db.commit()
        return id
