from src.users.models.domain import User
from src.users.models.interfaces import UserSelectorInterface


def fetch_user_by_uid(user_uid: str, repository: UserSelectorInterface) -> User:
    return repository.get_user_by_uid(user_uid=user_uid)
