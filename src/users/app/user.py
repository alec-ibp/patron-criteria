from src.shared.domain.filters import Criteria, Filter, Ordering

from src.users.models.domain import User
from src.users.models.interfaces import UserSelectorInterface


def fetch_user_by_uid(user_uid: str, repository: UserSelectorInterface) -> User:
    return repository.get_user_by_uid(user_uid=user_uid)


def fetch_users_by_criteria(
    repository: UserSelectorInterface,
    filters: list[Filter],
    order_by: str,
) -> list[User]:

    criteria: Criteria = Criteria(filters=filters, ordering=Ordering(field=order_by), limit=10, offset=0)
    return repository.get_users_by_criteria(criteria=criteria)
