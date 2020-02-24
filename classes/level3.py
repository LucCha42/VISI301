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

class Level3:

	def __init__(self):

		self.im = Image.open('resources/levels_tab/tab3.jpg')
		self.TAB = convert_to_tab(self.im)

		self.player = Player(32.0, 2.0)
		self.weapon = None

		# ==================== VAGUE 1

		def pre_wave1(self):

			Particle(8.0, 19.0)
			Particle(11.0, 19.0)
			Particle(4.0, 4.0)
			Particle(9.0, 7.0)


		def wave1(self):
			# JOUEUR
			self.player.weaponized = False
			# ARME
			self.weapon = Weapon(56.0, 18.0)
			# ENNEMIES
			Enemy1(8.0, 19.0)
			Enemy1(11.0, 19.0)
			Enemy1(4.0, 4.0)
			Enemy1(9.0, 7.0)


		# ==================== VAGUE 2

		def pre_wave2(self):

			Particle(7.0, 32.0)
			Particle(59.0, 19.0)
			Particle(9.0, 19.0)


		def wave2(self):
			# ARME
			self.weapon = Weapon(9.0, 12.0)
			# ENNEMIES
			Enemy2(7.0, 32.0)
			Enemy2(59.0, 19.0)
			Enemy2(9.0, 19.0)


		# ==================== VAGUE 3

		def pre_wave3(self):

			Particle(30.0, 22.0)


		def wave3(self):
			# ARME
			self.weapon = Weapon(51.0, 30.0)
			# ENNEMIES
			Enemy3(29.0, 20.0)


		# ==================== REPERTOIRE DES FONCTIONS

		self.pre_waves = [ pre_wave1, pre_wave2, pre_wave3 ]
		self.waves = [ wave1, wave2, wave3 ]