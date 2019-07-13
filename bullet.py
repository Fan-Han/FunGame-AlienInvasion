#! /usr/bin/python3

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to control bullets fired from the ship"""
	def __init__(self, ai_settings, screen, ship):
		""" Create a bullet at the ship's current place"""
		super().__init__()
		self.screen = screen

		# createa bullet rect at (0,0)
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# store the bullet's position as a decimal value
		self.y = float(self.rect.y)

		self.colour = ai_settings.bullet_colour
		self.speed = ai_settings.bullet_speed

	def update(self):
		"""Move the bullet up"""
		self.y -= self.speed
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.colour, self.rect)
