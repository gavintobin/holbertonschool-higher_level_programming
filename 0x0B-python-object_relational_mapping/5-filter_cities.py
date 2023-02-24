#!/usr/bin/python3
"""selects states by name"""
import MySQLdb
import sys


def list_all():
    """list all function"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("Select name FROM cities  WHERE state_id =  ANY ( SELECT id \
                 FROM states \
                 WHERE name = %(state)s) \
                 ORDER BY id ASC", {'state': sys.argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    list_all()
