#!/usr/bin/python3
"""
Module listing all cites from the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=pwd, db=db_name)
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               From cities
               LEFT JOIN states
               ON cities.state_id = states.id
               ORDER by cities.id ASC"""
    cur.execute(query)
    selec_data = cur.fetchall()
    for item in selec_data:
        print(item)
    db.close()
