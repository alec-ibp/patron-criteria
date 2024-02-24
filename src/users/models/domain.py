from uuid import UUID
from datetime import date


class User:
    def __init__(self, uid: int, name: str, age: int, birthdate: date, email: str, hashed_password: str):
        self.uid: UUID = uid
        self.name: str = name
        self.age: int = age
        self.birthdate: date = birthdate
        self.email: str = email
        self.hashed_password: str = hashed_password
