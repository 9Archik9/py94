from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import registry, DeclarativeBase


own_mapper = registry()
engine = create_engine('postgresql+psycopg2://blog_user:blog_password@localhost/blog')


class Base(DeclarativeBase):
    ...


class Article(Base):
    __tablename__ = 'article'
    id = Column('id', Integer(), primary_key=True)
    header = Column('header', String(255), unique=True)
    content = Column('content', Text(), nullable=False)


Base.metadata.create_all(engine)
