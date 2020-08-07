#!/usr/bin/python3


import MySQLdb
from sys import argv


def listn():
    """lists all states with a name starting with N from the database"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for x in rows:
        print(x)

if __name__ == "__main__":
    listn()
