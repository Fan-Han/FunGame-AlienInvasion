#! /usr/bin/python3

class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""Initialize the game's settings"""
		# screen size
		self.screen_width = 1200
		self.screen_height = 800
		
		# screen colour and background
		self.bg_colour = (0, 180, 230)
		self.bg_image = "images/alien_background.bmp"

		# Ship speed
		self.speed = 3.5

		# bullet
		self.bullet_speed = 3
		self.bullet_width = 7
		self.bullet_height = 10
		self.bullet_colour = 100, 100, 100
		self.bullet_number = 10