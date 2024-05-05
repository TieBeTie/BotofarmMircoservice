from fastapi import APIRouter
from fastapi import Depends
from api.dependencies import get_user_service 
from api.schemas.user import UserCreate, UserCreateRespond, UserAquireLock, UserAquireLockRespond, UserReleaseLock, UserReleaseLockRespond, UserList
from api.services import UserService
from uuid import UUID 

router = APIRouter()

@router.post("/", response_model=UserCreateRespond)
def create_user(User: UserCreate, user_service: UserService = Depends(get_user_service)) -> UserCreateRespond:
    """
    Create a new user.

    Args:
        User (UserCreate): The user data to be created.
        user_service (UserService, optional): The user service dependency. Defaults to Depends(get_user_service).

    Returns:
        UserCreateRespond: The response containing the created user data.
    """
    return user_service.create_user(User)

@router.get("/", response_model=UserList)
def get_users(user_service: UserService = Depends(get_user_service)) -> UserList:
    """
    Retrieve a list of users.

    Returns:
        UserList: A list of users.
    """
    return get_user_service().get_users()

@router.put("/{user_id}/lock", response_model=UserAquireLockRespond)
def acquire_lock(user_id: UUID, user_service: UserService = Depends(get_user_service)) -> UserAquireLockRespond:
    """
    Acquires a lock for the specified user.

    Args:
        user_id (UUID): The ID of the user to acquire the lock for.
        user_service (UserService): The user service dependency.

    Returns:
        UserAquireLockRespond: The response model indicating the success or failure of acquiring the lock.
    """
    return user_service.acquire_lock(user_id)


@router.delete("/{user_id}/lock", response_model=UserReleaseLockRespond)
def release_lock(user_id: UUID, user_service: UserService = Depends(get_user_service)) -> UserReleaseLockRespond:
    """
    Release the lock for a user.

    Args:
        user_id (UUID): The ID of the user to release the lock for.
        user_service (UserService): The user service dependency.

    Returns:
        UserReleaseLockRespond: The response model indicating the success of releasing the lock.
    """
    return user_service.release_lock(user_id)
