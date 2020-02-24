# -*- coding : utf-8 -*-

from classes.entity import *
from classes.player import *
from classes.weapon import *
from classes.enemy1 import *
from classes.enemy2 import *
from classes.enemy3 import *
from classes.particle import *
from resources.conversion_tool import *

# ========== VAGUES

class Level5:

	def __init__(self):

		self.im = Image.open('resources/levels_tab/tab5.jpg')
		self.TAB = convert_to_tab(self.im)

		self.player = Player(13.0, 13.0)
		self.weapon = None

		# ==================== VAGUE 1

		def pre_wave1(self):

			Particle(23.0, 6.0)
			Particle(23.0, 23.0)
			Particle(35.0, 23.0)
			Particle(58.0, 7.0)


		def wave1(self):
			# JOUEUR
			self.player.weaponized = False
			# ARME
			self.weapon = Weapon(55.0, 8.0)
			# ENNEMIES
			Enemy2(23.0, 6.0)
			Enemy2(23.0, 23.0)
			Enemy2(35.0, 23.0)
			Enemy2(58.0, 7.0)


		# ==================== VAGUE 2

		def pre_wave2(self):

			Particle(1.0, 6.0)
			Particle(3.0, 6.0)
			Particle(5.0, 6.0)
			Particle(3.0, 19.0)


		def wave2(self):
			# ARME
			self.weapon = Weapon(62.0, 1.0)
			# ENNEMIES
			Enemy2(1.0, 6.0)
			Enemy2(3.0, 6.0)
			Enemy2(5.0, 6.0)
			Enemy2(3.0, 19.0)

		# ==================== VAGUE 3

		def pre_wave3(self):

			Particle(30.0, 3.0)
			Particle(62.0, 1.0)

		def wave3(self):
			# ARME
			self.weapon = Weapon(32.0, 16.0)
			# ENNEMIES
			Enemy2(62.0, 1.0)
			Enemy3(30.0, 3.0)


		# ==================== REPERTOIRE DES FONCTIONS

		self.pre_waves = [ pre_wave1, pre_wave2, pre_wave3 ]
		self.waves = [ wave1, wave2, wave3 ]