#!/usr/bin/python3
"""
Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
                        LIKE BINARY '{}'".format(argv[4]))

    # fetch all
    my_data = my_cursor.fetchall()

    # iterate and print
    for rows in my_data:
        print(rows)

    # close all cursors
    my_cursor.close()

    # close all bds
    my_db.close()
