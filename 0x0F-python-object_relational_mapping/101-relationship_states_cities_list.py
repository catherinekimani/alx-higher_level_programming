#!/usr/bin/python3

"""
script that lists all State objects, and corresponding City objects
contained in the database hbtn_0e_101_usa
"""


from sys import argv
from relationship_city import City
from relationship_state import Base, State
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

    Base.metadata.create_all(engine)
    for state in my_session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # close session
    my_session.close()
