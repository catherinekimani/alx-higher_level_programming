#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    state = sys.argv[4]
    my_db = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3]
                            )

    my_cursor = my_db.cursor()

    my_cursor.execute("SELECT cities.name FROM cities INNER JOIN\
                        states ON state_id = states.id WHERE states.name\
                            = %s", (state, ))

    # fetch
    my_data = my_cursor.fetchall()
    cities = ', '.join(city[0] for city in my_data)

    print(cities)

    # close all cursors
    my_cursor.close()

    # close all bds
    my_db.close()
