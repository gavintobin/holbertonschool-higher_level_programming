#!/usr/bin/python3
"""task 9"""
import sys
from sqlalchemy.orm import session, sessionmaker
from base_model import Base, State
from sqlalchemy import engine, create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()
    for state in session.query(State).order_by(State.id).all():
        if  "a" in state:
            print("{}: {}".format(state.id, state.name))
