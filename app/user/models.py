from sqlalchemy import Column, String, Table, Integer
from app.db import db_helper


user = Table(
    "user",
    db_helper.metadata_obj,
    Column("id", Integer(), primary_key=True,nullable=False, autoincrement=True),
    Column("username", String(64), nullable=False),
    Column("email", String(64), nullable=False),
    Column("password", String(64), nullable=False),
)


class User:
    pass


db_helper.mapper_registry.map_imperatively(User, user)
