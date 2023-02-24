#!/usr/bin/python3
"""contains class definition of class and instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """base class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincremented=True)
    name = Column(String(128), nullable=False, autoincrement=True)
