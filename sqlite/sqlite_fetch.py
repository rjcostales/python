#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('scratch.db')

with connection:
    cur = connection.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)
