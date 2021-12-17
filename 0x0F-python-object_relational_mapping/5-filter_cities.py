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
    cursor.execute("""SELECT cities.name
                    FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name LIKE '{:s}'
                    ORDER BY cities.id""".format(argv[4]))
    row = cursor.fetchall()
    print(", ".join(city[0] for city in row))
    cursor.close()
    MySQL.close
