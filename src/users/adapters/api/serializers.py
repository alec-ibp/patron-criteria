from datetime import date

from pydantic import BaseModel, EmailStr, UUID4, PositiveInt


class UserOutputSerializer(BaseModel):
    uid: UUID4
    name: str
    age: PositiveInt
    birthdate: date
    email: EmailStr
