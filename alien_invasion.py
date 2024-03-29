#! /usr/bin/python3

import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from bg_image import BG_image
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
	""" Initialize game and create a screen object"""

	pygame.init()
	print("Welcome back!")
	# set screen size
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Game statistics
	stats = GameStats(ai_settings)

	# background image
	bg_image = BG_image(screen, ai_settings.bg_image)

	# Make a ship
	ship = Ship(ai_settings, screen)

	# Bullets and aliens
	bullets = Group()
	aliens = Group()

	# Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, aliens)


	# Main loop for the game
	while True:

		# Watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
	
		# update screen
		gf.update_screen(ai_settings, screen, bg_image, ship, bullets, aliens)

run_game()
