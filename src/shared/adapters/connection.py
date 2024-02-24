from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from config import settings


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        DB_HOST: str = settings.DB_HOST
        DB_NAME: str = settings.DB_NAME
        DB_USER: str = settings.DB_USER
        DB_PORT: str = settings.DB_PORT
        DB_PASSWORD: str = settings.DB_PASSWORD

        self.metadata: MetaData = MetaData()
        self.engine: Engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        self.db_session: Session = Session(bind=self.engine)
