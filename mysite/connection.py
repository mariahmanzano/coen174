import sqlite3

connect = sqlite.connect('db.sqlite3')

cur = conn.cursor()
cur.execute('CREATE TABLE adminAccess (adminCode NUMERIC)')
conn.commit()

conn.close()
