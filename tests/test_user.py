from app.api.services import UserService
from app.db.models import User
from app.db.session import Session
from datetime import datetime
from datetime import datetime
import pytest


def test_user_service_create_user() -> None:
    """
    Test case for creating a user.
    """
    session = Session()
    user_service = UserService(session)
    user_data = {
        "login": "test",
        "password": "test123",
        "project_id": "123e4567-e89b-12d3-a456-426614174000",
        "env": "prod",
        "domain": "regular"
    }

    user_id = user_service.create_user(User(**user_data))

    user = session.query(User).get(user_id)
    assert user.login == user_data["login"]
    assert user.password == user_data["password"]
    assert user.project_id == user_data["project_id"]
    assert user.env == user_data["env"]
    assert user.domain == user_data["domain"]

    session.delete(user)
    session.commit()


def test_user_service_get_users() -> None:
    """
    Test case for getting users.
    """
    session = Session()
    user_service = UserService(session)
    user_data = {
        "login": "test",
        "password": "test123",
        "project_id": "123e4567-e89b-12d3-a456-426614174000",
        "env": "prod",
        "domain": "regular"
    }
    user = User(**user_data)
    session.add(user)
    session.commit()

    users = user_service.get_users()

    assert len(users) > 0

    session.delete(user)
    session.commit()


def test_user_service_update_locktime() -> None:
    """
    Test case for updating locktime.
    """
    session = Session()
    user_service = UserService(session)
    user_data = {
        "login": "test",
        "password": "test123",
        "project_id": "123e4567-e89b-12d3-a456-426614174000",
        "env": "prod",
        "domain": "regular"
    }
    user = User(**user_data)
    session.add(user)
    session.commit()

    user_service.acquire_lock(user.id, datetime.now())

    updated_user = session.query(User).get(user.id)
    assert updated_user.locktime is not None

    session.delete(updated_user)
    session.commit()