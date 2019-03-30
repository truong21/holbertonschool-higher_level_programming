#!/usr/bin/python3
"""
Module listing all states starting with N from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    username = argv[1]
    pwd = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost", user=username, port=3306,
                         passwd=pwd, db=db_name)
    cur = db.cursor()
    query = """SELECT * FROM states
               WHERE BINARY name like 'N%' ORDER by id ASC"""
    cur.execute(query)
    selec_data = cur.fetchall()
    for item in selec_data:
        print(item)
    cur.close()
    db.close()
