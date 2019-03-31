#!/usr/bin/python3
"""
Module that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]

    engine_str = "mysql://{}:{}@localhost:3306/{}".format(username,
                                                          passwd, db)
    engine = create_engine(engine_str)
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    flag = 0
    result = session.query(State).filter(State.name == name)
    for item in result:
        print("{}".format(item.id))
        flag = 1
    if flag == 0:
        print("Not found")
