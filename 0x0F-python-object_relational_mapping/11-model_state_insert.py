#!/usr/bin/python3
"""
Module that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    LA_state = State(name="Louisiana")
    session.add(LA_state)
    session.commit()

    for instance in session.query(State).filter(State.name == 'Louisiana'):
        print("{}".format(instance.id))
