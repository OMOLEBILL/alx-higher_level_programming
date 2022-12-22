#!/usr/bin/python3
"""list all states using sqlalchemy"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    c1 = session.query(State).filter(State.name.like("%"))\
                .delete(synchronize_session='fetch')
    session.commit()
    session.close()
