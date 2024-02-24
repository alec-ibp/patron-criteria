from abc import ABC, abstractmethod

from src.shared.domain.filters import Criteria
from .domain import User


class UserSelectorInterface(ABC):
    @abstractmethod
    def get_user_by_uid(self, user_uid: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def get_users_by_criteria(self, criteria: Criteria) -> list[User | None]:
        raise NotImplementedError
