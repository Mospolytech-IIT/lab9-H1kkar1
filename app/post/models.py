from sqlalchemy import Column, String, Table, Uuid, Text, ForeignKey, Integer
from app.db import db_helper


post = Table(
    "post",
    db_helper.metadata_obj,
    Column("id", Integer(), primary_key=True, autoincrement=True),
    Column("title", String(256), nullable=False),
    Column("content", Text(), nullable=False),
    Column("user_id", Integer(), ForeignKey("user.id"), nullable=False),
)


class Post:
    """ Заглушка для маппинга sql моделей """
    pass


db_helper.mapper_registry.map_imperatively(Post, post)
