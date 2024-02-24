from typing import Any, Callable

from sqlalchemy import desc
from sqlalchemy.orm import Session
from src.shared.domain.filters import Criteria, Ordering

from src.users.models.domain import User
from src.users.models.interfaces import UserSelectorInterface
from src.shared.adapters.connection import DatabaseConnection

from src.users.utils import is_attribute


class UserSelectorRepository(UserSelectorInterface):
    def __init__(self, session: Session = DatabaseConnection().db_session) -> None:
        self.session: Session = session

    def get_user_by_uid(self, user_uid: str) -> User:
        return self.session.query(User).filter(User.uid == user_uid).first()

    def get_users_by_criteria(self, criteria: Criteria) -> list[User | None]:
        filter_by: dict[str, Any] = {}

        if filters := criteria.filters:
            filter_by = {
                filter.field: filter.value for filter in filters if is_attribute(User, filter.field)
            }

        order_by: str | Callable = criteria.ordering.order_by
        if criteria.ordering.order_type == Ordering.OrderingType.DESC.value:
            order_by = desc(order_by)

        return self.session.query(User).filter_by(**filter_by).order_by(order_by).all()
