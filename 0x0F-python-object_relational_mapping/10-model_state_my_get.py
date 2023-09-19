#!/usr/bin/python3

"""
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    my_session_maker = sessionmaker(bind=engine)

    my_session = my_session_maker()

    for state in my_session.query(State):
        if argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")

    # close session
    my_session.close()
