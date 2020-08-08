#!/usr/bin/python3
"""This module defines a query"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=dbname)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for x in rows:
        print(x)
    cursor.close()
    conn.close()
