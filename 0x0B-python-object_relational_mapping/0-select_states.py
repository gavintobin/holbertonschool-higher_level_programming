#!/usr/bin/python3
"""lists all states"""
import MySQLdb
import sys


def list_all():
    """list all function"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("Select * FROM states  ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    list_all()
