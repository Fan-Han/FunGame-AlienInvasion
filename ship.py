#! /usr/bin/python3

import pygame

class Ship():
	"""Initialize the ship"""

	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship image and get its rect
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start new ship at the bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update ship's movement"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_settings.speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.ai_settings.speed

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)