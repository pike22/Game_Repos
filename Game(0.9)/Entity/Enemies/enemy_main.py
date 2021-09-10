#this class will be the "Spokes person" for the enemies.
from ..game_entities import Game_Entities
import random

class Enemy_Main(Game_Entities):
	def __init__(self):
		Game_Entities.__init__(self)
		self.__random = random


	#def
