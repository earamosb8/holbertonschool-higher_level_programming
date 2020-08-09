#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    sts = session.query(State).filter(State.name == statename).first()
    if sts:
        print(sts.id)
    else:
        print('Not Found')

    session.close()
