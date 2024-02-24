from abc import ABC, abstractmethod

from .domain import User


class UserSelectorInterface(ABC):
    @abstractmethod
    def get_user_by_uid(self, user_uid: str) -> User:
        raise NotImplementedError
