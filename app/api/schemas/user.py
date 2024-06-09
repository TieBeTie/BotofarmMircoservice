from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List 
from pydantic import Field, field_validator
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List 
from pydantic import Field, field_validator

class UserBase(BaseModel):
    """
    Base model for user data.
    """
    id: UUID = Field(..., description="User ID")
    login: str = Field(..., description="User login")
    password: str = Field(..., description="User password")

    env: str = Field(..., description="User environment")
    @field_validator('env')
    def validate_env(cls, env):
        """
        Validator for env field.
        """
        valid_envs = ["prod", "prepord", "stage"]
        if env not in valid_envs:
            raise ValueError(f"Invalid env value. Allowed values are {', '.join(valid_envs)}.")
        return env
    
    domain: str = Field(..., description="User domain")
    @field_validator('domain')
    def validate_domain(cls, domain):
        """
        Validator for domain field.
        """
        valid_domains = ["canary", "regular"]
        if domain not in valid_domains:
            raise ValueError(f"Invalid domain value. Allowed values are {', '.join(valid_domains)}.")
        return domain

class User(BaseModel):
    """
    Model for user data.
    """
    user: UserBase = Field(..., description="User's main information")
    created_at: datetime = Field(..., description="User creation timestamp")
    locktime: datetime = Field(..., description="User lock timestamp")


class UserCreate(BaseModel):
    """
    Model for creating a new user.
    """
    pass

class UserCreateRespond(BaseModel):
    """
    Model for response when creating a new user.
    """
    id: UUID = Field(..., description="Created user ID")

class UserList(BaseModel):
    """
    Model for a list of users.
    """
    users: List[User] = Field(..., description="List of users")

class UserAquireLock(BaseModel):
    """
    Model for acquiring a lock on a user.
    """
    id: UUID = Field(..., description="User ID")

class UserAquireLockRespond(BaseModel):
    """
    Model for response when acquiring a lock on a user.
    """
    is_locked: bool = Field(..., description="Lock status")

class UserReleaseLock(BaseModel):
    """
    Model for releasing a lock on a user.
    """
    id: UUID = Field(..., description="User ID")

class UserReleaseLockRespond(BaseModel):
    """
    Model for response when releasing a lock on a user.
    """
    is_unlocked: bool = Field(..., description="Unlock status")
