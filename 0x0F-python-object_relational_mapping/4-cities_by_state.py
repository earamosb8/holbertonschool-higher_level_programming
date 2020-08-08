#!/usr/bin/python3
"""This module defines a query"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """lists all cities from the database hbtn_0e_4_usa."""
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name from cities\
                 JOIN states ON states.id = cities.state_id ORDER BY id ASC")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    cur.close()
    conn.close()
