#!/usr/bin/python3
"""Renames the State object with identifier 2 to New Mexico."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = 'New Mexico'
        session.commit()
    session.close()
