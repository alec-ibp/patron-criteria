from uuid import UUID
from typing import Annotated

from fastapi import Request, status
from fastapi import APIRouter, HTTPException, Query, Path

from pydantic import EmailStr

from src.shared.domain.filters import Filter

from src.users.models.domain import User
from .serializers import UserOutputSerializer
from src.users.app.user import fetch_user_by_uid, fetch_users_by_criteria
from src.users.adapters.db.selectors import UserSelectorRepository

router: APIRouter = APIRouter()


def get_filterset(request: Request) -> list[Filter | None]:
    filters: list[Filter] = []
    if request.query_params:
        for param_key, param_value in request.query_params.items():
            # TODO improve fixed operator
            filters.append(Filter(field=param_key, value=param_value, operator="eq"))

    return filters


@router.get(
    path="patron-criteria/{user_uid}",
    response_model=list[UserOutputSerializer | None],
    status_code=status.HTTP_200_OK,
)
async def list_users(
    request: Request,
    name: Annotated[str | None, Query(max_length=255, min_length=1)] = None,
    age: Annotated[int | None, Query(gt=0, lt=150)] = None,
    email: Annotated[EmailStr | None, Query(max_length=255, min_length=1)] = None,
    order_by: Annotated[str, Query(max_length=255, min_length=1)] = "uid",
) -> list[UserOutputSerializer]:

    filtered_users: list[User] = fetch_users_by_criteria(
        repository=UserSelectorRepository(),
        filters=get_filterset(request),
        order_by=order_by,
    )
    return filtered_users


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
