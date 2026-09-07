#!/usr/bin/python3
"""Lists states with a name matching the supplied argument."""

import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], charset="utf8")
    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
    cursor.execute(query.format(sys.argv[4]))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    connection.close()
