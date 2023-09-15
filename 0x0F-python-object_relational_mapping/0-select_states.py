#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        results = cur.fetchall()

        for row  in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cur.close()
        conn.close()
