from typing import Final

from sqlalchemy.orm import registry
from sqlalchemy import Table, Column, Integer, String, UUID, Date

from src.users.models.domain import User  # TODO - Fix this import doesn't have to be on shared
from ..adapters.connection import DatabaseConnection

mapper_registry: Final[registry] = registry()


def start_sqlalchemy_mappers() -> None:
    user_table: Table = Table(
        "user",
        DatabaseConnection().metadata,
        Column("uid", UUID, primary_key=True),
        Column("name", String(255), nullable=False),
        Column("age", Integer, nullable=False),
        Column("birthdate", Date, nullable=False),
        Column("email", String(255), nullable=False),
        Column("hashed_password", String(255), nullable=False),
    )

    mapper_registry.map_imperatively(User, user_table)
