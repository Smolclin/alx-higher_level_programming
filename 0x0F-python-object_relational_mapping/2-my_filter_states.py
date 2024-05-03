#!/usr/bin/python3
'''
This script takes arguement and
displays all values in the states
where name matches the arguement
from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''
    Access to the database and get the states
    from the database
    '''
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    state_dict = {}

    for row in rows:
        state_id, state_name = row
        if state_name not in state_dict:
            print(row)
            state_dict[state_name] = True
