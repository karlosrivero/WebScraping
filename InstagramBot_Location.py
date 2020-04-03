from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()	

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(3)
		email = bot.find_element_by_name('username').send_keys(self.username)
		password = bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)

		time.sleep(3)

	def searchLocation(self,location):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/locations/' + location)

	def likePhotos(self,amount):
		bot = self.bot

		bot.find_element_by_class_name('v1Nh3').click()

		i = 1
		while i <= amount:
			time.sleep(1)
			bot.find_element_by_class_name('fr66n').click()
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			time.sleep(1)

			i += 1


insta = InstagramBot('your_user','your_password')
insta.login()
insta.searchLocation('354438033') # Find the location you want to target -> New Zealand https://www.instagram.com/explore/locations/354438033/new-zealand/
insta.likePhotos(30) # Quantity of photos you want to like
