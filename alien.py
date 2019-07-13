#! /usr/bin/python3
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent an individual alien"""

	def __init__(self, ai_settings, screen):
		"""Initialize the starting position of the alien"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the image
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# Start each new alien at the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Float the position
		self.x = float(self.rect.x)

		# Determine how many alens could fit in a row
		self.number_aliens_x = int(ai_settings.screen_width/(2 * self.rect.width) - 1)
		# Determine how many alens could fit in a column
		self.number_aliens_y = int(ai_settings.screen_height/(2 * self.rect.height) - 4)


	def blitme(self):
		"""Draw its current position"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Move the alien"""
		self.rect.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direction)

	def check_edges(self):
		"""Check if any alien is at the edge or not"""
		if self.rect.right >= self.screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True 