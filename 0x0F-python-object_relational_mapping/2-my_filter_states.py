#!/usr/bin/python3
""" this scripts list the states name"""


import MySQLdb
from sys import argv

""" listing states from a data base """

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          password=argv[2], database=argv[3])
    cur = con.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE"
            "'{:s}' ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)
    cur.close()
    con.close()
