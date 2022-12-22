#!/usr/bin/python3
""" module that links MySQL table states """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """inherits from Base
    links to the MySQL table states
    class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
