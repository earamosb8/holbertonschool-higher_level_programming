#!/usr/bin/python3


import MySQLdb
from sys import argv


def matches():
    """displays all values in the table where name matches the argument"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    search = argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name= %s", [search])
    rows = cur.fetchall()
    for x in rows:
        print(x)

if __name__ == "__main__":
    matches()
