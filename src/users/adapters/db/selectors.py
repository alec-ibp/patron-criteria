from sqlalchemy.orm import Session

from src.users.models.domain import User
from src.users.models.interfaces import UserSelectorInterface
from src.shared.adapters.connection import DatabaseConnection


class UserSelectorRepository(UserSelectorInterface):
    def __init__(self, session: Session = DatabaseConnection().db_session) -> None:
        self.session: Session = session

    def get_user_by_uid(self, user_uid: str) -> User:
        return self.session.query(User).filter(User.uid == user_uid).first()
