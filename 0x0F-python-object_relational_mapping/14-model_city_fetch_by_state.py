#!/usr/bin/python3
"""
Module that prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine_str = "mysql://{}:{}@localhost:3306/{}".format(username,
                                                          passwd, db)
    engine = create_engine(engine_str)
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    for s, c in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
