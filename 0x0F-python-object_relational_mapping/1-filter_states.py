#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[2]
    third = sys.argv[3]

    db = MySQLdb.connect(user=first, passwd=second, db=third)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ")
    rows = cur.fetchall()
    printed_state = set()

    for row in rows:
        state_id, state_name = row
        if state_name not in printed_state:
            print(row)
            printed_state.add(state_name)
