#!/usr/bin/python3


import MySQLdb
from sys import argv


def select():
    """lists all states from the database"""
    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    db = MySQLdb.connect(host="127.0.0.1", port=3306,
                         user=username, passwd=password, db=dbname)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for x in rows:
        print(x)

if __name__ == "__main__":
    select()