import sqlite3
# don't need global vars -- this module will be imported anyways
# DB = None
# CONN = None

class Melon(object):
	"""Creates melon objects to structure and name data from DB """
	def __init__(self, id, melon_type, common_name, price, imgurl):
		self.id = id
		self.melon_type = melon_type
		self.common_name = common_name
		self.price = price
		self.imgurl = imgurl

	def price_str(self):
		# this is a string representation of the objct's price
		#formats the price of the melon
		return "$%.2f" % (self.price)

def connect_to_DB():
	# global DB, CONN
	CONN = sqlite3.connect("melons.db")
	DB = CONN.cursor()
	return DB

def get_all_melons():
	melon_list = []

	DB = connect_to_DB() # gets return val of cursor from connect function
	query = """SELECT id, melon_type, common_name, price, imgurl
	FROM melons
	WHERE imgurl <> ''
	LIMIT 30"""
	DB.execute(query)
	melons = DB.fetchall() # returns a list of matching rows (as tuples!!)

	for melon in melons: # loops through one row at a time
		if not melon[4]:
			print "No image!"
		m = Melon(melon[0], melon[1], melon[2], melon[3], melon[4])
		melon_list.append(m)

	return melon_list #returns a list of Melon instances

def get_melon_by_id(id):
	DB = connect_to_DB()

	query = """SELECT id, melon_type, common_name, price, imgurl
		FROM melons
		WHERE id = ?
		LIMIT 1"""
	DB.execute(query, (id, ))

	melon = DB.fetchone()
	m = Melon(melon[0], melon[1], melon[2], melon[3], melon[4])
	# print m
	return m





