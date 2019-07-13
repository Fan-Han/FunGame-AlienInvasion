#! /usr/bin/python3

import sys
import pygame
from alien import Alien
from bullet import Bullet
from ship import Ship
from time import sleep

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keyboard and mouse events."""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit("You have quit the game.")
			
			elif event.type == pygame.KEYDOWN:
				check_keydown(event, ai_settings, screen, ship, bullets)

			elif event.type == pygame.KEYUP:
				check_keyup(event, ship)


def update_screen(ai_settings, screen, bg_image, ship, bullets, aliens):
	"""Update image position and flip to the new screen"""
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_colour)
	bg_image.blit_bg()
	ship.blitme()
	aliens.draw(screen)
	for bullet in bullets.sprites():
		bullet.draw_bullet()

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


def update_bullets(ai_settings, screen, aliens, bullets):
	bullets.update()
	# Remove the bullets out of the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	# If bullet hits alien, remove both bullet and alien
	check_alien_bullet_collision(ai_settings, screen, aliens, bullets)


def check_alien_bullet_collision(ai_settings, screen, aliens, bullets):
	""" If bullet hits alien, remove both bullet and alien"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	# create new fleet if all aliens are killed
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, aliens)
		ai_settings.alien_speed *= 1.5


def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullet_number:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
	""" Create a fleet of aliens before the run"""
	alien = Alien(ai_settings, screen)

	for alien_number in range(alien.number_aliens_x):
		for alien_row in range(alien.number_aliens_y):
			alien = Alien(ai_settings, screen)
			alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number
			alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_row
			aliens.add(alien)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""After alien hits ship"""
	if stats.ship_left > 1:
		stats.ship_left -= 1
	
		# Empty aliens and bullets
		aliens.empty()
		bullets.empty()
	
		# Restore the initial screen
		create_fleet(ai_settings, screen, aliens)
		ship.center_ship()
	
		# Pause
		sleep(1.0)
	else:
		stats.game_active = False


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	"""Move the aliens"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# If alien hit ship
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

	# If alien hits the bottom
	check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites(): 
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break


def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def check_alien_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	""" You lose the game if alien hits the bottom"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom > screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
