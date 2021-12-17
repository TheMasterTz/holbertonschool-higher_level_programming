#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).order_by(State.id).first()
    if states:
        for state in session.query(State).order_by(State.id).all():
            print("{}".format(state.id))
    else:
        print("Nothing")
    session.close()
