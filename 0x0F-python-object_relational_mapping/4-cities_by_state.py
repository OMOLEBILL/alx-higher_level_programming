#!/usr/bin/python3
""" this scripts list the states name"""


import MySQLdb
from sys import argv

""" listing states from a data base """

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          password=argv[2], database=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)
    cur.close()
    con.close()
