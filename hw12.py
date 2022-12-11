import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM titles")
description = cursor.description
data = cursor.fetchall()
for row in data:
    print("%-20s%-20s%-20s" % (row[0], row[1], row[2]))
