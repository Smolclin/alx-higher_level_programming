#!/usr/bin/python3

import sys
import MySQLdb


def list_states(username, password, database):
    # connects to MySQL serveet number

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    # To execute the SQL query to fetch all the states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches all the rows from the query result
    rows = cursor.fetchall()

    # prints the result
    for row in rows:
        print(row)

    # closes the database connection
    db.close()


# example in usage
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
