#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities AS c
                INNER JOIN states AS s ON c.state_id = s.id
                ORDER BY c.id ASC""")
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
