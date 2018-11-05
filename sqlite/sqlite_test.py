#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

connection = None

try:
    connection = sqlite3.connect('scratch.db')

    cur = connection.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print("SQLite version: %s" % data)

except sqlite3.Error as e:

    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:

    if connection:
        connection.close()
