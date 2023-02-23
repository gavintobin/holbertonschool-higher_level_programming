#!/usr/bin/python3
"""lists all states"""
import MySQLdb
import sys


def list_all():
    """list all function"""
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
    cur = conn.cursor()
    cur.execute("Select * FROM states  ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == '__main__':
    list_all()
