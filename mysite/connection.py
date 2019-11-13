import sqlite3

conn = sqlite3.connect('db.sqlite3')

cur = conn.cursor()

sql_command = """
CREATE TABLE employee (
session_number INTEGER,
room_number INTEGER
);"""

##cur.execute(sql_command)

sql_command = """INSERT INTO employee
(session_number, room_number)
	VALUES ("1", "2");"""
cur.execute(sql_command)

conn.commit()

conn.close()
