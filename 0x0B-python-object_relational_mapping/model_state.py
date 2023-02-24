#!/usr/bin/python3
"""declaritive base class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincremented=True)
    name = Column(String(128), nullable=False, autoincrement=True)

