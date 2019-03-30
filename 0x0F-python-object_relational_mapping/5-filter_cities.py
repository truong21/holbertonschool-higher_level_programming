#!/usr/bin/python3
"""
Module listing all cites from user input of state from the database
hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=pwd, db=db_name)
    cur = db.cursor()
    query = """SELECT cities.name
               From cities
               LEFT JOIN states
               ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER by cities.id ASC"""
    cur.execute(query, (state,))
    selec_data = cur.fetchall()
    cities = []
    for item in selec_data:
        cities.append(item[0])
    print(", ".join(cities))
    db.close()
