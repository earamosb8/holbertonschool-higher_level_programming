#!/usr/bin/python3
"""This module defines a query"""

import MySQLdb
from sys import argv


def select():
    """lists all states from the database"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    conn = MySQLdb.connect(host="127.0.0.1", port=3306,
                           user=username, passwd=password, db=dbname)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for x in rows:
        print(x)
    cursor.close()
    conn.close()
if __name__ == "__main__":
    select()
