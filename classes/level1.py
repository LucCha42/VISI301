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

class Level1:

	def __init__(self):

		self.im = Image.open('resources/levels_tab/tab1.jpg')
		self.TAB = convert_to_tab(self.im)

		self.player = Player(13.0, 31.0)
		self.weapon = None

		# ==================== VAGUE 1

		def pre_wave1(self):

			Particle(50.0, 30.0)


		def wave1(self):
			# ARME
			self.weapon = Weapon(44.0, 16.0)
			# ENNEMIES
			Enemy1(50.0, 30.0)


		# ==================== VAGUE 2

		def pre_wave2(self):

			Particle(28.0, 32.0)
			Particle(31.0, 32.0)
			Particle(34.0, 32.0)


		def wave2(self):
			# ARME
			self.weapon = Weapon(19.0, 16.0)
			# ENNEMIES
			Enemy1(28.0, 32.0)
			Enemy1(31.0, 32.0)
			Enemy1(34.0, 32.0)


		# ==================== VAGUE 3

		def pre_wave3(self):

			Particle(37.0, 5.0)
			Particle(42.0, 32.0)
			Particle(28.0, 32.0)
			Particle(32.0, 32.0)
			Particle(46.0, 3.0)
			Particle(11.0, 1.0)


		def wave3(self):
			# ARME
			self.weapon = Weapon(4.0, 4.0)
			# ENNEMIES
			Enemy1(37.0, 5.0)
			Enemy1(42.0, 32.0)
			Enemy1(28.0, 32.0)
			Enemy1(32.0, 32.0)
			Enemy1(46.0, 3.0)
			Enemy1(11.0, 1.0)


		# ==================== REPERTOIRE DES FONCTIONS

		self.pre_waves = [ pre_wave1, pre_wave2, pre_wave3 ]
		self.waves = [ wave1, wave2, wave3 ]