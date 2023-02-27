#!/usr/bin/python3
"""task 8"""
import sys
from sqlalchemy.orm import session, sessionmaker
from model_state import Base, State
from sqlalchemy import engine, create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing\n")
    else:
        print("{}: {}".format(state.id, state.name))
