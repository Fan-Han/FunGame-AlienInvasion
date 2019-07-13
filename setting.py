#! /usr/bin/python3

class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings"""
		# screen size
		self.screen_width = 1800
		self.screen_height = 1000
		
		# screen colour and background
		self.bg_colour = (0, 180, 230)
		self.bg_image = "images/alien_background.bmp"

		# Ship speed
		self.speed = 3.5
		self.ship_limit = 3

		# bullet
		self.bullet_speed = 5
		self.bullet_width = 7
		self.bullet_height = 20
		self.bullet_colour = 255, 255, 0
		self.bullet_number = 100000

		# alien
		self.alien_speed = 10
		self.fleet_drop_speed = 50
		# fleet direction: 1 - right, -1 - left
		self.fleet_direction = 1