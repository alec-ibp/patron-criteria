from datetime import datetime


class User:
    def __init__(self, uid: int, name: str, age: int, birthdate: datetime, email: str, hashed_password: str):
        self.uid: str = uid
        self.name: str = name
        self.age: int = age
        self.birthdate: datetime = birthdate
        self.email: str = email
        self.hashed_password: str = hashed_password
