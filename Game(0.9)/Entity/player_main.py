#this will talk to the player_info as well as act as the way for the
#target entity to be controlled by the user.
#this will be used to set up and and save data.

from Engine.kinetics_node import Kinetics_Node
from .game_entities import Game_Entities
from .player_info import Player_Info
import keyboard

class Player_Main(Game_Entities):
	def __init__(self, iNode):
		#iNode == Image_Node
		#cNode == Collision_Node
		#Collision_Logic set from bellow

		#----Class Calls----#
		Game_Entities.__init__(self)
		self.__Collision_Logic = None
		self.__Kinetics		= Kinetics_Node(iNode)
		self.__info	 		= Player_Info()
		self.__Image	 	= iNode
		self.__Weapon 		= None

		#----Keyboard inputs----#
		self.__key_up		= 'w'
		self.__key_down		= 's'
		self.__key_left		= 'a'
		self.__key_right	= 'd'
		self.__key_attack	= 'k'
		self.__key_test 	= 't'
		self.__moveing		= False


	def Movement_Controll(self):
		if keyboard.is_pressed(self.__key_up):
			new_Coords = self.__Kinetics.y_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID(), neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Image.get_Render().bbox(self.__info.get_CanvasID()))
			self.__moveing = True

		if keyboard.is_pressed(self.__key_down):
			new_Coords = self.__Kinetics.y_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID())
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Image.get_Render().bbox(self.__info.get_CanvasID()))
			self.__moveing = True

		if keyboard.is_pressed(self.__key_left):
			new_Coords = self.__Kinetics.x_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID(), neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Image.get_Render().bbox(self.__info.get_CanvasID()))
			self.__moveing = True

		if keyboard.is_pressed(self.__key_right):
			new_Coords = self.__Kinetics.x_Kinetics(self.__info.get_Coords(), self.__info.get_CanvasID())
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(self.__Image.get_Render().bbox(self.__info.get_CanvasID()))
			self.__moveing = True

		if keyboard.is_pressed(self.__key_right) == False and keyboard.is_pressed(self.__key_up) == False and keyboard.is_pressed(self.__key_down) == False and keyboard.is_pressed(self.__key_left) == False:
			self.__moveing = False
			return self.__moveing
		else:
			return self.__moveing

	def Player_Attack(self):
		if keyboard.is_pressed(self.__key_attack) == True:
			x, y = self.__info.get_Coords() #current coords
			a, b = self.__Weapon.get_Size()
			self.__Weapon.use_Sword(x+a, y)

		if keyboard.is_pressed('l'):
			self.__Weapon.del_Sword()

	def test_Coords(self):
		if keyboard.is_pressed(self.__key_test) == True:
			x, y = self.__info.get_Coords() #current coords
			print(x, y, 'CURRENT CORDS')

	#any required getters & setters will be created.
	#	this is important because the players needed
	#	info isn't stored in this same class.


	#seting up player bellow
	def player_initial_setUP(self, x, y, priority):
		#img setup
		ID = "P#001"
		group_ID = "#player"
		Img_info = self.__Image.Img_Add('z_Pictures/purpuloniousthefirst.png')
		self.__info.Image_Data(Size=Img_info[1], ID=ID , group_ID=group_ID, PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/purpuloniousthefirst.png')

		#placing the img
		img_list, img_coords = self.__Image.Img_Place(x, y, self.__info.get_TKimg(), tag=ID)

		#final set of information save to player
		Canvas_ID = self.__Image.get_Render().find_withtag(ID)[0] #finds my canvas ID numb.
		print(Canvas_ID, "CANVAS")
		Current_Coords = img_coords[Canvas_ID-1]
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Player_Data(Cur_Coords=Current_Coords, Speed=7, health=10, defense=5, attack=2) #check player_info for well info.
		self.__Kinetics.set_Speed(self.__info.get_Speed())
		self.__Image.get_Render().addtag_withtag(group_ID, Canvas_ID)
		self.__info.set_Corners(self.__Image.get_Render().bbox(Canvas_ID))


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


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...

	def get_Params(self):
		A, B, C = self.__info.get_Params()
		return A, B, C

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()

	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Collision_Logic(self, Logic):
		self.__Collision_Logic = Logic

	def set_Weapon(self, sWeapon):
		self.__Weapon = sWeapon
