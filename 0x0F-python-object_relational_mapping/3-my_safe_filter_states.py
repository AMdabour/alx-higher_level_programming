#!/usr/bin/python3
"""a script that lists all states with a name equals to sys.argv[4]
from the database hbtn_0e_0_usa in a safe way"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
                ORDER BY states.id ASC;""", (sys.argv[4],))
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
