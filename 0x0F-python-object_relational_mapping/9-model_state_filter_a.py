#!/usr/bin/python3
"""print all State with the letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    states = session.query(State).all()
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()
