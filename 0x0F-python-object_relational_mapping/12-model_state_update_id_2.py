#!/usr/bin/python3
"""list all states using sqlalchemy"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Session = sessionmaker(engine)
    with Session() as session:
        c1 = session.query(State).get(2)
        c1.name = "New Mexico"
        session.commit()
