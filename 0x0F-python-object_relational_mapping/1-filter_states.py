#!/usr/bin/python3
"""
script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # conncet db
    my_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            password=argv[2], db=argv[3])
    # create cursor object
    my_cursor = my_db.cursor()

    # execute SELECT query
    my_cursor.execute("SELECT * FROM states WHERE name\
                        LIKE BINARY 'N%' ORDER BY id ASC")

    # fetch all
    my_data = my_cursor.fetchall()

    # iterate and print
    for rows in my_data:
        print(rows)

    # close all cursors
    my_cursor.close()

    # close all bds
    my_db.close()
