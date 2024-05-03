#!/usr/bin/python3
'''
The above script takes an arguement and
displays all values in the states
where name matches the arguement
from the database hbtn_0e_0_usa
the script is safe from MySQLdb injections
'''

import MySQLdb as db
from sys import argv


if __name__ == "__main__":
    '''
    Access to the database and get the states
    from the database
    '''
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    state_dict = {}

    for row in rows_selected:
        state_id, state_name = row
        if state_name not in state_dict:
            print(row)
            state_dict[state_name] = True
