# -*- coding : utf-8 -*-

import pygame

class Globals:

	RATIO = 20 # ratio écran / grille
	FPS = 60 # images/boucles par seconde
	RESOLUTION = (1280,720)
	counter = 0 # compteur de boucle
	launched = False
	ecran = "menu"
	pygame.font.init()
	FONT = pygame.font.Font("./resources/FFFFORWA.TTF", 15)
	TITLE_FONT = pygame.font.Font("./resources/FFFFORWA.TTF", 40)
	m = 5
	s = 0

	# COULEURS
	WHITE = (255,255,255)
	LIGHT_GRAY = (200, 200, 200)
	GRAY = (76, 76, 76)
	BLACK = (0,0,0)
	RED = (255,0,0)
	YELLOW = (255,255,0)
	GREEN = (0,255,0)
	CYAN = (0,255,255)
	BLUE = (0,0,255)
	PURPLE = (255,0,255)

	# NIVEAU
	level = 1 # sélectionne le niveau
	blocks = [] # liste qui stock des blocs de l'environnement

	# ENNEMIES
	enemies = [] # liste de tout les ennemies

	# PROJECTILES
	projectiles = [] # liste de tous les projectiles

	# BROUILLARD
	TRANSITION = 180 # attente entre deux vagues (en image/sec)
	transition_counter = TRANSITION # compteur entre deux vagues
	particles = []

	# POPUPS
	popups = [] # liste de tout les popups