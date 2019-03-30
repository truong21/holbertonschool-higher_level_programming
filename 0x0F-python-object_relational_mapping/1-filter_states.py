#!/usr/bin/python3
"""
Module listing all states starting with N from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=username, port=3306,
                         passwd=pwd, db=db_name)
    cur = db.cursor()
    query = """SELECT id, name FROM states
               WHERE name like 'N%' ORDER by id ASC"""
    cur.execute(query)
    selec_data = cur.fetchall()
    for item in selec_data:
        print(item)
    cur.close()
    db.close()
