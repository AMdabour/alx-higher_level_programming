#!/usr/bin/python3
"""a script that lists all states with a name starting
with N(upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    cur.execute(query)
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
