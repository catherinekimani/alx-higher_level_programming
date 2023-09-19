#!/usr/bin/python3

"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    Base.metadata.create_all(engine)

    my_obj = State(name="Louisiana")

    my_session.add(my_obj)
    my_session.commit()
    print(my_obj)

    # close session
    my_session.close()
