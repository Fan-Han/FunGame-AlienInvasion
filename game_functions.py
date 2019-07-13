#! /usr/bin/python3

import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keyboard and mouse events."""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit("You have quit the game.")
			
			elif event.type == pygame.KEYDOWN:
				check_keydown(event, ai_settings, screen, ship, bullets)

			elif event.type == pygame.KEYUP:
				check_keyup(event, ship)

def update_screen(ai_settings, screen, bg_image, ship, bullets):
	"""Update image position and flip to the new screen"""
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_colour)
	bg_image.blit_bg()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# Make the most recently drawn screen visible
	pygame.display.flip()

def check_keydown(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_ESCAPE:
		sys.exit("You have quit the game.")

	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True

	if event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup(event, ship):
	ship.moving_right = False
	ship.moving_left = False

def update_bullets(bullets):
	bullets.update()
	# Remove the bullets out of the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullet_number:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)