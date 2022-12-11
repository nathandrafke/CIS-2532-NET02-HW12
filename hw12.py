'''
This program will open the books database and use Cursor method to select and execute
all the data in the titles table, then use description and fetchall to display
the data in tabular format.

Name: Nathan Drafke
'''

import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM titles")
description = cursor.description
data = cursor.fetchall()
for row in data:
    print("%-20s%-20s%-20s" % (row[0], row[1], row[2]))
