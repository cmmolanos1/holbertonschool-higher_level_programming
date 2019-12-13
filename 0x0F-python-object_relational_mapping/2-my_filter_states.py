#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    command = "SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4])
    cur.execute(command)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
