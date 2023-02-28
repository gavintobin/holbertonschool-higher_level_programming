#!/usr/bin/python3
"""task 12"""
import sys
from sqlalchemy.orm import session, sessionmaker
from model_state import Base, State
from sqlalchemy import engine, create_engine
from model_city import Base, City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()
    for state, city in session.query(State, City) \
            .filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
