#!/usr/bin/python3
""" sqlachemy list all states"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print(f"{state.id}, {state.name}")
session.close()