#!/usr/bin/python3
"""
 class definition of a City
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base


class City(Base):
    """ Definition of state class """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement="auto")

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
