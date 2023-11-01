#!/usr/bin/python3
"""a script that lists all cities of a state from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""SELECT c.name FROM cities AS c
                INNER JOIN states AS s ON c.state_id = s.id
                WHERE s.name LIKE BINARY %s
                ORDER BY c.id ASC""", (sys.argv[4],))
    results = cur.fetchall()
    cName = list(row[0] for row in results)
    print(*cName, sep=', ')

    cur.close()
    conn.close()
