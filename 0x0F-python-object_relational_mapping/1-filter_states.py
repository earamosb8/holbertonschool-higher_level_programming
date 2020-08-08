#!/usr/bin/python3
"""This module defines a query """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """lists all states with a name starting with N from the database"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           password=password, db=dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    rows = cur.fetchall()
    for x in rows:
        print(x)
    cur.close()
    conn.close()
