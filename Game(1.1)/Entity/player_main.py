#this will talk to the player_info as well as act as the way for the
#target entity to be controlled by the user.
#this will be used to set up and and save data.

from .all_entities import All_Entities
from .player_info import Player_Info
from Weapons import *
from Engine import *

import keyboard

class Player_Main(All_Entities):
	def __init__(self, iNode, kNode):
		#iNode == Image_Node
		#clNode == Collision_Node

		#----Class Calls----#
		All_Entities.__init__(self)
		self.__Kinetics		= kNode
		self.__Image	 	= iNode
		self.__info	 		= Player_Info()
		self.__Sword 		= None
		self.__Arrow		= None
		self.__Bow			= None

		#----Keyboard inputs----#
		self.__key_up		= 'w'
		self.__upOFF		= False
		self.__key_down		= 's'
		self.__downOFF		= False
		self.__key_left		= 'a'
		self.__leftOFF		= False
		self.__key_right	= 'd'
		self.__rightOFF		= False
		self.__melee		= 'k'
		self.__ranged		= 'l'

		#----Active Parameters----#
		self.__Cur_Health = 0
		self.__saveTime	  = 0
		self.__Direction  = None
		self.__isAttack	  = False
		self.__isMoving   = False
		self.__isAlive	  = True
		self.__isHit	  = False


	#seting up player bellow
	def player_setUP(self, x, y):
		#img setup
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		Img_info = self.__Image.Img_Add('z_Pictures/purpuloniousthefirst.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/purpuloniousthefirst.png')

		#placing the img
		img_coords = self.__Image.Img_Place(x, y, self.__info.get_TKimg(), tag=ID)

		#final set of information save to player
		Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
		Coords = img_coords[Canvas_ID-1]
		print(Coords, 'Player Coords')
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Player_Data(Coords=Coords, Speed=7, health=100, defense=5, attack=0) #check player_info for well info.
		self.__Kinetics.set_Speed(self.__info.get_Speed())
		Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
		print(self.get_Corners(), 'player corners')

		#Active Parameters
		self.__Cur_Health = self.__info.get_health()

	def Player_Print(self):
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Player Data:')
		print(self.__info.get_ID(), '\t:Entity ID')
		print(self.__info.get_Speed(), 	'\t:Speed')
		print(self.__info.get_health(),	'\t:Health')
		print(self.__info.get_defense(),'\t:Defense')
		print(self.__info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self.__info.get_size(), 	'\t\t:Size')
		print(self.__info.get_Coords(), 	'\t\t:Coords')
		print(self.__info.get_Corners(), 	'\t:Corners')
		print('-----------------------------------\n')

	def Movement_Controll(self):
		if keyboard.is_pressed(self.__key_up) and self.__upOFF == False:
			self.__Direction = 'up'
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True

		if keyboard.is_pressed(self.__key_down) and self.__downOFF == False:
			self.__Direction = 'down'
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True

		if keyboard.is_pressed(self.__key_left) and self.__leftOFF == False:
			self.__Direction = 'left'
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True

		if keyboard.is_pressed(self.__key_right) and self.__rightOFF == False:
			self.__Direction = 'right'
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True

		self.__isMoving = False
		return self.__isMoving

	def Player_MAttack(self):#melee Attack
		if keyboard.is_pressed(self.__melee) == True:
			x, y = self.__info.get_Coords() #current coords
			a, b = self.__Sword.get_size()
			if self.__Direction == 'up':
				self.__Sword.use_Sword(x, y-b)
			elif self.__Direction == 'down':
				self.__Sword.use_Sword(x, y+b)
			elif self.__Direction == 'left':
				self.__Sword.use_Sword(x-a, y)
			elif self.__Direction == 'right':
				self.__Sword.use_Sword(x+a, y)
			self.__isAttack = True
			return self.__isAttack

		elif self.__Sword.get_isActive() == False:
			self.__isAttack = False
			return self.__isAttack

	def Player_RAttack(self):#ranged attack
		if keyboard.is_pressed(self.__ranged) == True:
			x, y = self.__info.get_Coords() #current coords
			a, b = self.__Bow.get_size()
			if self.__Direction == 'up':
				self.__Bow.use_Bow(x, (y-b), 'up')
			elif self.__Direction == 'down':
				self.__Bow.use_Bow(x, (y+b), 'down')
			elif self.__Direction == 'left':
				self.__Bow.use_Bow((x-a), y, 'left')
			elif self.__Direction == 'right':
				self.__Bow.use_Bow((x+a), y, 'right')
			self.__isAttack = True
			# print(self.__isAttack)
			return self.__isAttack

		elif self.__Bow.get_isActive() == False:
			self.__isAttack = False
			# print(self.__isAttack)
			return self.__isAttack


		#OSC == Other Side of Collision, it represents the other object that collided with player
		#OSA == Other Side's Attack, represents the other objects needed parameters. Ex. dmg
	def my_Collision(self, OSC=None, OSA=None, side=None):
		if OSC == 'Enemy':
			if self.__isHit == False:
				'''#_Actuall MATH_#'''
				self.__Cur_Health -= OSA
				if side == 'top':
					Dir = 'up'
				elif side == 'bottom':
					Dir = 'down'
				else:
					Dir = side
				new_Coords = self.__Kinetics.Knock_Back(self.__info.get_Coords(), self.__info.get_ID(), Dir)
				self.__info.set_Coords(new_Coords)
				self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))

				'''#_Logic_#'''
				self.__isHit 	= True
				self.__isAlive  = self.isAlive()
				self.__saveTime = Timer_Node.GameTime

		elif OSC == 'Weapon':
			pass

		elif OSC == 'Static':
			if side == 'top':
				Dir = 'up'
			elif side == 'bottom':
				Dir = 'down'
			else:
				Dir = side
			new_Coords = self.__Kinetics.Static_Hit(self.__info.get_Coords(), self.__info.get_ID(), Dir)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))

		else:
			print('Error: P#108')
			pass




	def reset_hit(self):
		if Timer_Node.GameTime == self.__saveTime+5:
			self.__isHit = False
			print('Player Can Get Hit')
			print(self.__Cur_Health, ':Player Health')

	def isAlive(self):
		if self.__isHit == True:
			if self.__Cur_Health > 0:
				# print("Alive")
				return True
			elif self.__Cur_Health <= 0:
				Image_Node.Render.delete(self.__info.get_ID())
				# print("Not Alive")
				return False
		elif self.__isHit == False:
			print('ERROR: #193','\n\tself.__isHit = False' )




	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_size(self):
		return self.__info.get_size()

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_Coords(self):
		return self.__info.get_Coords()

	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_isAlive(self):
		return self.__isAlive

	def get_isHit(self):
		return self.__isHit

	def get_isMoving(self):
		return self.__isMoving

	def get_isAttack(self):
		return self.__isAttack

		#_attack, health, defense_#
	def get_attack(self):
		return self.__info.get_attack()

	def get_health(self):
		return self.__info.get_health()

	def get_defense(self):
		return self.__info.get_defense()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Weapons(self, sword, bow):
		self.__Sword = sword
		self.__Bow	 = bow


	def set_health(self, health):
		self.__info.set_health(health)

	def set_isAlive(self, isAlive):
		self.__isAlive = isAlive

	def OnOff_Move(self):
		self.__upOFF	= False
		self.__downOFF	= False
		self.__leftOFF	= False
		self.__rightOFF	= False


	"""|--------------Test Functions--------------|#"""

	def test_Coords(self):
		if keyboard.is_pressed('c') == True:
			x, y = self.__info.get_Coords() #current coords
			print(x, y, 'CURRENT CORDS')

	#any required getters & setters will be created.
	#	this is important because the players needed
	#	info isn't stored in this same class.
