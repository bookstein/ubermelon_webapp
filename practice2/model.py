import sqlite3
# don't need global vars -- this module will be imported anyways
# DB = None
# CONN = None

def connect_to_DB():
	# global DB, CONN
	CONN = sqlite3.connect("melons.db")
	DB = CONN.cursor()
	return DB

def get_all_melons():
	connect_to_DB()
	query = """SELECT * from melons LIMIT 30"""
	DB.execute(query)
	melons = DB.fetchall()
	CONN.close()
	return melons
