import sqlite3

DB = None
CONN = None

def connect_to_DB():
	global DB, CONN
	CONN = sqlite3.connect("melons.db")
	DB = CONN.cursor()
