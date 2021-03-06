#this will talk to the player_info as well as act as the way for the
#target entity to be controlled by the user.
#this will be used to set up and and save data.

from .all_entities import All_Entities
from .player_info import Player_Info
from Weapons import *
from Engine import *

import keyboard

class Player_Main(All_Entities):
	"""
	The main module that handles everything to do with the player.

	Methods
	-------
	init(cLogic, cNode, iNode, kNode)
		This is required when Player_Main() is called
	"""
	def __init__(self, cLogic, cNode, iNode, kNode):
		#iNode == Image_Node
		#cLogic == Collision_Logic

		#----Class Calls----#
		All_Entities.__init__(self)
		self.__cLogic		= cLogic
		self.__cNode		= cNode
		self.__kNode		= kNode
		self.__iNode	 	= iNode
		self.__info	 		= Player_Info()
		self.__Sword 		= None
		self.__Bow			= None

		#----Keyboard inputs----#
		self.__key_up		= 'w'
		self.__key_down		= 's'
		self.__key_left		= 'a'
		self.__key_right	= 'd'
		self.__melee		= 'k'
		self.__ranged		= 'l'

		#----Active Parameters----#
		self.__Cur_Health = 0
		self.__saveTime	  = 0
		self.__Direction  = None
		self.__isAttack	  = False
		self.__isMoving   = False
		self.__isStatic	  = False
		self.__isAlive	  = True
		self.__isHit	  = False


	#seting up player bellow
	def player_setUP(self, x, y):
		"""
		This sets up all of the background info of the player.

		Parameters
		----------
		x : int
			The x position of the player
		y : int
			The y position of the player

		Attributes
		----------
		ID : str
			Is pulled from the Stalfos_Info class
		Img_info : list
			Uses Image_Node.Img_Add() to get the Pil and tk image as well as size.
		Canvas_ID
			The tag that tkinter uses to identify which object is which.
		Coords, img_coords : tuple int
			The coordinants of the image on screen.
		"""
		#img setup
		ID = self.__info.get_ID()
		Img_info = self.__iNode.Img_Add('z_Pictures/purpuloniousthefirst.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/purpuloniousthefirst.png')

		#placing the img
		img_coords = self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, self.__info.get_group_ID()])

		#final set of information save to player
		Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
		Coords = img_coords
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Player_Data(Coords=Coords, Speed=7, health=10, defense=5, attack=0) #check player_info for well info.
		self.__kNode.set_Speed(self.__info.get_Speed())
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))

		#Active Parameters
		self.__Cur_Health = self.__info.get_health()

	def __Player_Print(self):
		"""
		:meta private:
		"""
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
		"""
		Controlls everything to do with the players movement
		"""
		if self.__isStatic == False:
			self.__kNode.set_Speed(self.__info.get_Speed())
			if keyboard.is_pressed(self.__key_up):
				self.__Direction = 'up'
				new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)#, neg=False)
				self.__info.set_Coords(new_Coords)
				self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
				self.__isMoving = True

			if keyboard.is_pressed(self.__key_down):
				self.__Direction = 'down'
				new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)
				self.__info.set_Coords(new_Coords)
				self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
				self.__isMoving = True

			if keyboard.is_pressed(self.__key_left):
				self.__Direction = 'left'
				new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)
				self.__info.set_Coords(new_Coords)
				self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
				self.__isMoving = True

			if keyboard.is_pressed(self.__key_right):
				self.__Direction = 'right'
				new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), self.__Direction)
				self.__info.set_Coords(new_Coords)
				self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
				self.__isMoving = True

			self.__isMoving = False
			return self.__isMoving
		else:
			print("Can't Move, BURH!!!!")

	def Player_MAttack(self):#melee Attack
		"""
		Controlls the functionality of a melee attack.
		"""
		if keyboard.is_pressed(self.__melee) == True:
			x, y = self.__info.get_Coords() #current coords
			a, b = self.__Sword.get_size()
			if self.__Direction == 'up':
				self.__Sword.use_Sword(x, y-b, self.__Direction)
			elif self.__Direction == 'down':
				self.__Sword.use_Sword(x, y+b, self.__Direction)
			elif self.__Direction == 'left':
				self.__Sword.use_Sword(x-a, y, self.__Direction)
			elif self.__Direction == 'right':
				self.__Sword.use_Sword(x+a, y, self.__Direction)
			self.__isAttack = True
			return self.__isAttack

		elif self.__Sword.get_isActive() == False:
			self.__isAttack = False
			return self.__isAttack

	def Player_RAttack(self):#ranged attack
		"""
		Controlls the Functionality of a ranged attack.
		"""
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
	def my_Collision(self, OSC=None, OSA=None, side=None, staticsList=None):
		"""
		Handels what should happen to the player based on the collision.

		Parameters
		----------
		OSC : 'Other Side Collision'
			This holds the classification of what is colliding with the player. EX: ('Enemy', 'Static', or 'Weapon')
		OSA : 'Other Side Attack'
			This holds how much damage should be done when player has come into contact with the OSC.
		side : str
			The direction that the collision came from.
		staticsList : list
			A list of static group_ID's that is used so that when knock back happens an Entity doesn't travel through a static object.

		Attributes
		----------
		Direction : str
			Direction that player is hitting OSC. Dir == newSide
		lastSide : str
			The last direction that was triggered.
		new_Coords : tuple int
			The new coords after collision.
		PossibleCL : list
			The list of everything colliding with player.
		"""
		if self.__isHit == False:
			Direction = None
			if OSC == 'Enemy':
					'''#_Actuall MATH_#'''
					self.__Cur_Health -= OSA
					for newSide in side:
						if newSide == 'top':
							Direction = 'up'
						elif newSide == 'bottom':
							Direction = 'down'
						else:
							Direction = newSide
						for time in range(50):
							new_Coords = self.__kNode.Knock_Back(self.__info.get_Coords(), self.__info.get_ID(), Direction)
							self.__info.set_Coords(new_Coords)
							self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
							x1, y1, x2, y2 = Image_Node.Render.bbox(self.__info.get_ID())
							PossibleCL = self.__cLogic.ForT_Collision(x1=x1, y1=y1, x2=x2, y2=y2)
							if PossibleCL != None:
								# print(PossibleCL, 'yes')
								for obj in PossibleCL:
									if obj != None:
										if obj.get_group_ID() in staticsList:
											# print('wallHIT')
											Direction = self.__cLogic.Side_Calc(self.__cLogic.tagToObj(self.__info.get_ID()))
											self.my_Collision(OSC='Static', side=Direction)
											return
					'''#_Logic_#'''
					self.__isHit 	= True
					self.__isAlive  = self.isAlive()
					self.__saveTime = Timer_Node.GameTime

			elif OSC == 'Weapon':
				pass

			elif OSC == 'Static':
				lastSide = None
				# print(side)
				for newSide in side:
					if newSide == 'top':
						Direction = 'up'
					elif newSide == 'bottom':
						Direction = 'down'
					else:
						Direction = newSide
					# print(Dir, 'direction')
					# print(lastSide, 'last direction')
					if Direction != lastSide:
						new_Coords = self.__kNode.Static_Hit(self.__info.get_Coords(), self.__info.get_ID(), Direction)
						self.__info.set_Coords(new_Coords)
						self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
						lastSide = Direction
					elif lastSide == None:
						new_Coords = self.__kNode.Static_Hit(self.__info.get_Coords(), self.__info.get_ID(), Direction)
						self.__info.set_Coords(new_Coords)
						self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
						lastSide = Direction


			else:
				print('Error: P#283')
				pass




	#The below could be consolidated to all_entities.py to be used acrossed 'all entities'.
	def reset_hit(self):
		print('Consider the above comment, P#294')
		"""
		This is a hit timer so that something can't be hit more than once in a set amount of time.
		"""
		if Timer_Node.GameTime == self.__saveTime+5:
			self.__isHit = False
			print('Player Can Get Hit')
			print(self.__Cur_Health, ':Player Health')

	def isAlive(self):
		"""
		Checks for if Player is still alive.
		"""
		if self.__isHit == True:
			if self.__Cur_Health > 0:
				# print("Alive")
				return True
			elif self.__Cur_Health <= 0:
				Image_Node.Render.delete(self.__info.get_ID())
				# print("Not Alive")
				return False
		elif self.__isHit == False:
			print('ERROR: #285','\n\tself.__isHit = False' )




	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_size(self):
		"""
		:meta private:
		"""
		return self.__info.get_size()

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__info.get_Corners()

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__info.get_Coords()

	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_ID()

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_group_ID()

	def get_isAlive(self):
		"""
		:meta private:
		"""
		return self.__isAlive

	def get_isHit(self):
		"""
		:meta private:
		"""
		return self.__isHit

	def get_isMoving(self):
		"""
		:meta private:
		"""
		return self.__isMoving

	def get_isAttack(self):
		"""
		:meta private:
		"""
		return self.__isAttack

		#_attack, health, defense_#
	def get_attack(self):
		"""
		:meta private:
		"""
		return self.__info.get_attack()

	def get_health(self):
		"""
		:meta private:
		"""
		return self.__info.get_health()

	def get_defense(self):
		"""
		:meta private:
		"""
		return self.__info.get_defense()


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Weapons(self, sword, bow):
		"""
		:meta private:
		"""
		self.__Sword = sword
		self.__Bow	 = bow


	def set_health(self, health):
		"""
		:meta private:
		"""
		self.__info.set_health(health)

	def set_isAlive(self, isAlive):
		"""
		:meta private:
		"""
		self.__isAlive = isAlive

	def set_ammo(self, ammo):
		"""
		:meta private:
		"""
		self.__Bow.set_ammo(ammo)


	"""#|--------------Test Functions--------------|#"""

	def test_Coords(self):
		"""
		:meta private:
		"""
		if keyboard.is_pressed('c') == True:
			x, y = self.__info.get_Coords() #current coords
			print(x, y, 'CURRENT CORDS')

	#any required getters & setters will be created.
	#	this is important because the players needed
	#	info isn't stored in this same class.
