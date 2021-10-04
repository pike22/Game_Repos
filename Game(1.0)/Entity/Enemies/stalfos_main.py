#here will be the Stalfos's controller
from .enemy_main import Enemy_Main
from .stalfos_info import Stalfos_Info
from Engine import *

import keyboard #temporary
import random

class Stalfos_Main(Enemy_Main):
	def __init__(self, iNode, clNode, kNode, tNode, ID):
		Enemy_Main.__init__(self)
		#iNode == Image_Node
		#clNode == Collision_Node
		self.__Collision_Logic = clNode
		self.__Kinetics		= kNode
		self.__Image	 	= iNode
		self.__Timer		= tNode
		self.__info	 		= Stalfos_Info(ID)
		self.__rand 		= random

		#----Active Parameters----#
		self.__Cur_Health = 0
		self.__recent_hit = False
		#latter add the others

		#----Temp Var----#
		self.__x			= 0
		self.__y			= 0


	#seting up player bellow
	def stalfos_initial_setUP(self, Sc_Width, Sc_Height):
		#img setup
		ID = self.__info.get_ID()
		Img_info = self.__Image.Img_Add('z_Pictures/RedBoy2.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/RedBoy2.png')

		#placing the img
		self.__x = 0
		self.__y = 0
		x, y = self.__info.get_Size()
		self.__x = int(self.__rand.randint((25+x), Sc_Width-(25+x)))
		self.__y = int(self.__rand.randint((25+y), Sc_Height-(25+y)))
		img_list, img_coords = self.__Image.Img_Place(x=self.__x, y=self.__y, image=self.__info.get_TKimg(), Grid='no', tag=ID)

		#final set of information save to stalfos
		Canvas_ID = self.__Image.get_Render().find_withtag(ID)[0] #finds my canvas ID numb.
		Coords = img_coords[Canvas_ID-1]
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Stalfos_Data(Cur_Coords=Coords, Speed=7, health=10, defense=5, attack=2) #check stalfos_info for, well info.
		self.__Kinetics.set_Speed(self.__info.get_Speed())
		self.__Image.get_Render().addtag_withtag(self.__info.get_group_ID(), Canvas_ID)
		self.__info.set_Corners(self.__Image.get_Render().bbox(Canvas_ID))


	#this is to go at the end.
	def Stalfos_Print(self):
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Stalfos Data:')
		print(self.__info.get_ID(), '\t:Entity ID')
		print(self.__info.get_Speed(), 	'\t:Speed')
		print(self.__info.get_health(),	'\t:Health')
		print(self.__info.get_defense(),	'\t:Defense')
		print(self.__info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self.__info.get_Size(), 	'\t\t:Size')
		print(self.__info.get_Coords(), 	'\t\t:Coords')
		print(self.__info.get_Corners(), 	'\t:Corners')
		print('-----------------------------------')
		print('')


		#SSC == Second Side Collision, it represents the other object that collided with player
		#SSI == Second Side Info, represents the other objects needed parameters. Ex. dmg
		#stal_key == The stalfos that is under collision
	def my_Collision(self, SSC, SSI):
		if self.__recent_hit == False:
			self.__recent_hit = True
			health = self.__Cur_Health
			health -= SSI
			self.__Cur_Health = health
			self.alive()
			print(self.__Cur_Health, self.get_ID() + "'s health")

	def alive(self):
		if self.__Cur_Health > 0:
			print("Alive")
			return True
		elif self.__Cur_Health <= 0:
			render = self.__Image.get_Render()
			render.delete(self.__info.get_ID())
			print("Not Alive")
			return False


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


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Collision_Logic(self, Logic):
		self.__Collision_Logic = Logic
