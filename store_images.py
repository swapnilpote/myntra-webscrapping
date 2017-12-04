from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, time
import urllib.request
from db_con import DatabaseConnection
from pprint import pprint

class StoreImages:
	def __init__(self):
		try:
			self.db_connection = DatabaseConnection()
		except:
			pprint("Unable to connect to database.")

	def make_soup(self, url):
		driver = webdriver.Firefox(executable_path='geckodriver')
		driver.get(url)

		return driver

	def store(self):
		products = self.db_connection.query_all()

		for prod in products:
			prod_url = prod[2]
			driver = self.make_soup(prod_url)
			image_url = driver.find_element_by_css_selector('img.thumbnails-selected-image').get_attribute('src')
			urllib.request.urlretrieve(image_url, "images/" + str(prod[0])+".jpg")
			# driver.implicitly_wait(30)
			driver.close()


if __name__ == '__main__':
	storeage = StoreImages()
	storeage.store()
