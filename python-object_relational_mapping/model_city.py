#!/usr/bin/python3
"""Defines the SQLAlchemy City model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """Represents a city stored in the cities table."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
