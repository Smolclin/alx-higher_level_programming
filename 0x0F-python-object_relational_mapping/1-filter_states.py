#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY statees.id ASC")
    rows = cur.fetchall()

    for row in rows:
        if row[1].startswitch("N"):
            print(row)

    cur.close()
    conn.close()
