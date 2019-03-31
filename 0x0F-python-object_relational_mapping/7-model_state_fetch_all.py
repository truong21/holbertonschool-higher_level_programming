#!/usr/bin/python3
"""module lists all State objects from database hbtn_0e_6_usa using SQLAlchemy
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

    list = session.query(State).order_by(State.id).all()
    for item in list:
        print("{}: {}".format(item.id, item.name))
