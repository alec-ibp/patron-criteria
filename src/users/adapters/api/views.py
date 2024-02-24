from uuid import UUID
from typing import Annotated

from fastapi import status
from fastapi import APIRouter, HTTPException, Path

from src.users.models.domain import User
from .serializers import UserOutputSerializer
from src.users.app.user import fetch_user_by_uid
from src.users.adapters.db.selectors import UserSelectorRepository

router: APIRouter = APIRouter()


@router.get(
    path="/{user_uid}",
    response_model=UserOutputSerializer,
    status_code=status.HTTP_200_OK,
)
async def get_user(user_uid: Annotated[UUID, Path(..., title="user unique identifier")]) -> UserOutputSerializer:
    stored_user: User | None = fetch_user_by_uid(repository=UserSelectorRepository(), user_uid=user_uid)
    if not stored_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return stored_user
