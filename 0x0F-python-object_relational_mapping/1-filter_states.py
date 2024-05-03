#!/usr/bin/python3
''''
 List all states with name starting with N from the database hbt_0e_0_usa
 Usage: ./1-filter_states.py <mysql username> \
        <mysql passwd> \
        <database name>
'''

import MySQLdb
import sys
'''
Access tot the database and gets the states
from that database
'''

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
