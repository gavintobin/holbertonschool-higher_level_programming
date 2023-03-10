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
    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
    if not state.name:
        print("Not Found")
