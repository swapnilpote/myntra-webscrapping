import psycopg2
from pprint import pprint

class DatabaseConnection:
	def __init__(self):
		try:
			self.connection = psycopg2.connect(
				"dbname='myntra' user='swapnilpote' host='localhost' password='' port='5432'")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			pprint("Cannot connect to database")

	def create_table(self):
		create_table_command = "create table if not exists women_cloths(id serial primary key, name varchar(100), brand varchar(100), prod_url text, img_url text)"
		return self.cursor.execute(create_table_command)

	def insert_new_record(name, brand, prod_url, img_url):
		insert_command = "insert into women_cloths(name, brand, prod_url, img_url) values('" + name  + "','" + brand + "','" + prod_url + "','" + img_url + "')"
		pprint(insert_command)
		return self.cursor.execute(insert_command)

	def query_all(self):
		self.cursor.execute("select * from women_cloths")
		women_cloths = self.cursor.fetchall()

		return women_cloths

	def update_record(self):
		update_command = "update women_cloths set price=2599 where id=1"
		return self.cursor.execute(update_command)

	def drop_record(self):
		drop_table_command = "drop table if exists women_cloths"
		return self.cursor.execute(drop_table_command)

# if __name__ == '__main__':
	# database_connection = DatabaseConnection()
	# database_connection.create_table()
	# database_connection.insert_new_record("top 1", "link1", "levis", "2999")
	# database_connection.insert_new_record("top 2", "link2", "spyker", "1999")
	# database_connection.query_all()
	# database_connection.drop_record()











