#!/usr/bin/python3


import MySQLdb
from sys import argv

""" listing states from a data base """

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          password=argv[2], database=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)
    cur.close()
    con.close()
