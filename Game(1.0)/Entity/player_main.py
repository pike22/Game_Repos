#this will talk to the player_info as well as act as the way for the
#target entity to be controlled by the user.
#this will be used to set up and and save data.

from .all_entities import All_Entities
from .player_info import Player_Info
from Engine import *

import keyboard

class Player_Main(Game_Entities):
	def __init__(self, iNode, clNode, kNode, tNode):
		#iNode == Image_Node
		#clNode == Collision_Node

		#----Class Calls----#
		All_Entities.__init__(self)
		self.__Collision_Logic = clNode
		self.__Kinetics		= kNode
		self.__Image	 	= iNode
		self.__Timer 		= tNode
		self.__info	 		= Player_Info()
		self.__Weapon 		= None

		#----Keyboard inputs----#
		self.__key_up		= 'w'
		self.__key_down		= 's'
		self.__key_left		= 'a'
		self.__key_right	= 'd'
		self.__key_attack	= 'k'
		self.__moving		= False

		#----Active Parameters----#
		self.__GameTime	  = 0
		self.__Cur_Health = 0
		self.__isAlive	  = True
		self.__isHit	  = False
		#latter add the others

		#----Random Var----#
		self.__Render = None



	def Movement_Controll(self):
		if keyboard.is_pressed(self.__key_up):
			new_Coords = self.__Kinetics.y_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID(), neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Render.bbox(self.__info.get_CanvasID()))
			self.__moving = True

		if keyboard.is_pressed(self.__key_down):
			new_Coords = self.__Kinetics.y_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID())
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Render.bbox(self.__info.get_CanvasID()))
			self.__moving = True

		if keyboard.is_pressed(self.__key_left):
			new_Coords = self.__Kinetics.x_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID(), neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Render.bbox(self.__info.get_CanvasID()))
			self.__moving = True

		if keyboard.is_pressed(self.__key_right):
			new_Coords = self.__Kinetics.x_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID())
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Render.bbox(self.__info.get_CanvasID()))
			self.__moving = True

		if keyboard.is_pressed(self.__key_right) == False and keyboard.is_pressed(self.__key_up) == False and keyboard.is_pressed(self.__key_down) == False and keyboard.is_pressed(self.__key_left) == False:
			self.__moving = False
			return self.__moving
		else:
			return self.__moving

	def Player_Attack(self):
		if keyboard.is_pressed(self.__key_attack) == True:
			x, y = self.__info.get_Coords() #current coords
			a, b = self.__Weapon.get_Size()
			self.__Weapon.use_Sword(x+a, y)

		if keyboard.is_pressed('l'):
			self.__Weapon.del_Sword()


		#SSC == Second Side Collision, it represents the other object that collided with player
		#SSI == Second Side Info, represents the other objects needed parameters. Ex. dmg
	def my_Collision(self, SSC, SSI):
		saveTime = self.__Timer.get_Seconds()
		saveTime += 2
		print(saveTime,':D')
		print(self.__Timer.get_Seconds(),'D:')
		if SSC == 'Enemy':
			if self.__isHit == False:
				self.__isHit = True
				self.__Cur_Health -= SSI
				new_Coords = self.__Kinetics.Knock_Back(self.__info.get_Coords(), self.__info.get_CanvasID())#, neg=False)
				self.__info.set_Coords(new_Coords)
				self.__info.set_Corners(self.__Render.bbox(self.__info.get_CanvasID()))
				self.__isAlive = self.alive()
				def needTime():
					if self.__Timer.get_Seconds() == saveTime:
						print('can hit?')
					else:
						print('no hit :(')
						self.All_Entities.get_mainApp().after(int(saveTime), needTime)

		elif SSC == 'Weapon':
			pass
			# print('self hit, oops')
		else:
			pass
		return self.__isHit


	def alive(self):
		if self.__isHit == True:
			if self.__Cur_Health > 0:
				# print("Alive")
				return True
			elif self.__Cur_Health <= 0:
				self.__Render.delete(self.__info.get_ID())
				# print("Not Alive")
				return False
		elif self.__isHit == False:
			print('oh no')

	#seting up player bellow
	def player_initial_setUP(self, x, y, priority=0):
		#img setup
		ID = self.__info.get_ID()
		group_ID = "#player"
		Img_info = self.__Image.Img_Add('z_Pictures/purpuloniousthefirst.png')
		self.__info.Image_Data(Size=Img_info[1], group_ID=group_ID, PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/purpuloniousthefirst.png')

		#placing the img
		img_list, img_coords = self.__Image.Img_Place(x, y, self.__info.get_TKimg(), tag=ID)

		#final set of information save to player
		Canvas_ID = self.__Image.get_Render().find_withtag(ID)[0] #finds my canvas ID numb.
		Current_Coords = img_coords[Canvas_ID-1]
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Player_Data(Cur_Coords=Current_Coords, Speed=7, health=10, defense=5, attack=0) #check player_info for well info.
		self.__Kinetics.set_Speed(self.__info.get_Speed())
		self.__Image.get_Render().addtag_withtag(group_ID, Canvas_ID)
		self.__info.set_Corners(self.__Image.get_Render().bbox(Canvas_ID))

		#Active Parameters
		self.__Cur_Health = self.__info.get_health()


	def Player_Print(self):
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Player Data:')
		print(self.__info.get_ID(), '\t:Entity ID')
		print(self.__info.get_CanvasID(), '\t:Canvas ID')
		print(self.__info.get_Speed(), 	'\t:Speed')
		print(self.__info.get_health(),	'\t:Health')
		print(self.__info.get_defense(),'\t:Defense')
		print(self.__info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self.__info.get_Size(), 	'\t\t:Size')
		print(self.__info.get_Coords(), 	'\t\t:Coords')
		print(self.__info.get_Corners(), 	'\t:Corners')
		print('-----------------------------------')
		print('')


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...

	def get_attack(self):
		return self.__info.get_attack()

	def get_health(self):
		return self.__info.get_health()

	def get_defense(self):
		return self.__info.get_defense()

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_isAlive(self):
		return self.__isAlive


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Collision_Logic(self, Logic):
		self.__Collision_Logic = Logic

	def set_Weapon(self, sWeapon):
		self.__Weapon = sWeapon

	def set_health(self, health):
		self.__info.set_health(health)

	def save_GT(self, GameTime):
		self.__GameTime = GameTime

	def set_Render(self, Render):
		self.__Render = Render

	def set_isAlive(self, isAlive):
		self.__isAlive = isAlive


	"""|--------------Test Functions--------------|#"""

	def test_Coords(self):
		if keyboard.is_pressed('c') == True:
			x, y = self.__info.get_Coords() #current coords
			print(x, y, 'CURRENT CORDS')

	#any required getters & setters will be created.
	#	this is important because the players needed
	#	info isn't stored in this same class.
