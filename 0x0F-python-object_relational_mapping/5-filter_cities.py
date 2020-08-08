#!/usr/bin/python3
"""This module defines a query"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """takes a state as an argument and lists all cities of that state"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    states = argv[4]
    my_list = []
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           password=password, db=dbname)
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                 from cities JOIN states ON states.id = cities.state_id\
                 WHERE states.name = %s ORDER BY cities.id", [states])
    rows = cur.fetchall()
    for x in rows:
        for y in x:
            my_list.append(y)
    print(", ".join(my_list))
    cur.close()
    conn.close()
