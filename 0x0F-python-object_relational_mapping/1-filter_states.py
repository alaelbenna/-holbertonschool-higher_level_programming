#!/usr/bin/python3
"""a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""



import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            database=argv[3],
    )
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE Name LIKE BINARY 'N%' ORDER BY is "
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()        
