import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = 'USER'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=func.now())
    login = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    project_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    env = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    locktime = Column(DateTime, default=None)
