#!/usr/bin/python3

"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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

    Base.metadata.create_all(engine)

    my_session_maker = sessionmaker(bind=engine)

    my_session = my_session_maker()

    my_session.add(City(name="San Francisco", state=State(name="California")))

    my_session.commit()

    # close session
    my_session.close()
