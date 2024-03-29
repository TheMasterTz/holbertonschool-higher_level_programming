#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    MySQL = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    cursor = MySQL.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    row = cursor.fetchall()
    for state in row:
        if state[1][0] == 'N':
            print(state)
    cursor.close()
    MySQL.close
