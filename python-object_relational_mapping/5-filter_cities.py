#!/usr/bin/python3
"""Lists cities belonging to a supplied state name."""

import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON "
                   "cities.state_id = states.id WHERE states.name LIKE "
                   "BINARY %s ORDER BY cities.id ASC", (sys.argv[4],))
    print(", ".join(city[0] for city in cursor.fetchall()))
    cursor.close()
    connection.close()
