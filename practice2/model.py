import sqlite3

DB = None
CONN = None

def connect_to_DB():
	global DB, CONN
	CONN = sqlite3.connect("melons.db")
	DB = CONN.cursor()

def get_all_melons():
	connect_to_DB()
	query = """SELECT * from melons LIMIT 30"""
	DB.execute(query)
	melons = DB.fetchall()
	CONN.close()
	return melons
