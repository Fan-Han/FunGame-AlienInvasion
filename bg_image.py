#! /usr/bin/python3
import pygame

class BG_image():
	""" Load background image"""

	def __init__(self, screen, bk):
		self.screen = screen
		self.image = pygame.image.load(bk)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# set position
		self.rect.centerx = self.screen_rect.centerx

	def blit_bg(self):
		self.screen.blit(self.image, self.rect)