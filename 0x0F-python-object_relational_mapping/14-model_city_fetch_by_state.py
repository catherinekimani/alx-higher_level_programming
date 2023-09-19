#!/usr/bin/python3

"""
script that prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
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

    for state, city in my_session.query(State, City).filter(
                                        State.id == City.state_id).all():

        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close session
    my_session.close()
