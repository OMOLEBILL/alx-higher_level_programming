#!/usr/bin/python3
"""list all states using sqlalchemy"""

from model_city import Base, City
from model_state import State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        c = session.query(City, State).filter(City.state_id == State.id)\
                .order_by(City.id).all()
        for cty, st in c:
            print("{}: ({}) {}".format(st.name, cty.id, cty.name))
