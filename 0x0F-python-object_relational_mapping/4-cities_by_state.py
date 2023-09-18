#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect db
    my_db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                            password=argv[2], db=argv[3])

    # create cursor object
    my_cursor = my_db.cursor()

    # execute SELECT query
    my_cursor.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id
        """
        )

    # fetch all
    my_data = my_cursor.fetchall()

    # iterate
    for rows in my_data:
        print(rows)

    # close all cursors
    my_cursor.close()

    # close all bds
    my_db.close()
