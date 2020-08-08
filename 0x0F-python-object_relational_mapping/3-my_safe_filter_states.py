#!/usr/bin/python3
"""This module defines a query"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """displays all values in the table where name matches the argument"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    search = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           password=password, db=dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", [search])
    rows = cur.fetchall()
    for x in rows:
        print(x)
    cur.close()
    conn.close()
