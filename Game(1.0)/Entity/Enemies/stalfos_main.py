#here will be the Stalfos's controller
from .enemy_main import Enemy_Main
from .stalfos_info import Stalfos_Info
from Engine import *

import keyboard #temporary
import random

class Stalfos_Main(Enemy_Main):
	def __init__(self, iNode, clNode, kNode, ID):
		Enemy_Main.__init__(self)
		#iNode == Image_Node
		#clNode == Collision_Node
		self.__Collision_Logic = clNode
		self.__Kinetics		= kNode
		self.__Image	 	= iNode
		self.__info	 		= Stalfos_Info(ID)
		self.__rand 		= random

		#----Active Parameters----#
		self.__GameTime	  = 0
		self.__saveTime	  = 0
		self.__Cur_Health = 0
		self.__isAlive	  = True
		self.__isHit	  = False
		self.__isMoving	  = False

		#----Temp Var----#
		self.__x	= 0
		self.__y	= 0
		self.__var	= 1
		self.__randNum = None


	#seting up player bellow
	def stalfos_setUP(self, Sc_Width, Sc_Height):
		#img setup
		ID = self.__info.get_ID()
		Img_info = self.__Image.Img_Add('z_Pictures/RedBoy2.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/RedBoy2.png')

		#placing the img
		self.__x = 0
		self.__y = 0
		x, y = self.__info.get_size()
		self.__x = int(self.__rand.randint((25+x), Sc_Width-(25+x)))
		self.__y = int(self.__rand.randint((25+y), Sc_Height-(25+y)))
		img_coords = self.__Image.Img_Place(x=self.__x, y=self.__y, image=self.__info.get_TKimg(), Grid='no', tag=ID)

		#final set of information save to stalfos
		Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
		Coords = img_coords[Canvas_ID-1]
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Stalfos_Data(Coords=Coords, Speed=5, health=10, defense=5, attack=2) #check stalfos_info for, well info.
		self.__Kinetics.set_Speed(self.__info.get_Speed())
		Image_Node.Render.addtag_withtag(self.__info.get_group_ID(), Canvas_ID)
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))

		#Active Parameters
		self.__Cur_Health = self.__info.get_health()


	#this is to go at the end.
	def Stalfos_Print(self):
		#list of prints for start of program(stalfos)
		print('-----------------------------------')
		print('Stalfos Data:')
		print(self.__info.get_ID(), '\t:Entity ID')
		print(self.__info.get_Speed(), 	'\t:Speed')
		print(self.__info.get_health(),	'\t:Health')
		print(self.__info.get_defense(),	'\t:Defense')
		print(self.__info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self.__info.get_size(), 	'\t\t:Size')
		print(self.__info.get_Coords(), 	'\t\t:Coords')
		print(self.__info.get_Corners(), 	'\t:Corners')
		print('-----------------------------------\n')

	def Movement_Controll(self):
		if Timer_Node.GameTime == self.__var:
			self.__randNum = int(self.__rand.randint(0, 3))
			print(self.__var)
			self.__var += 11


		if self.__randNum == 0:
			direction = "up"
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True
		elif self.__randNum == 1:
			direction = "right"
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True
		elif self.__randNum == 2:
			direction = "down"
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True
		elif self.__randNum == 3:
			direction = "left"
			new_Coords = self.__Kinetics.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True

	def Stal_Attack(self):
		pass

		#SSC == Second Side Collision, it represents the other object that collided with player
		#SSI == Second Side Info, represents the other objects needed parameters. Ex. dmg
		#stal_key == The stalfos that is under collision
	def my_Collision(self, SSC, SSI):
		if self.__isHit == False:
			'''#_Actuall MATH_#'''
			self.__Cur_Health -= SSI
			# print(self.__Cur_Health, 'health')

			'''#_Logic_#'''
			self.__isHit 	= True
			self.__isAlive  = self.isAlive()
			self.__saveTime = Timer_Node.GameTime

	def reset_hit(self):
		if Timer_Node.GameTime == self.__saveTime+5:
			self.__isHit = False
			print('Stalfos Can Get Hit')
			print(self.__Cur_Health, ':Stalfos Health')

	def isAlive(self):
		if self.__isHit == True:
			if self.__Cur_Health > 0:
				# print("Alive")
				return True
			elif self.__Cur_Health <= 0:
				Image_Node.Render.delete(self.__info.get_ID())
				# print("Not Alive")
				return False
		else:
			print('ERROR: S#105', '\tself.__isHit = False')


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

	def get_isHit(self):
		return self.__isHit

	def get_isAlive(self):
		return self.__isAlive

	def get_isMoving(self):
		return self.__isMoving

		#_attack, health, defense_#
	def get_attack(self):
		return self.__info.get_attack()

	def get_health(self):
		return self.__info.get_health()

	def get_defense(self):
		return self.__info.get_defense()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Collision_Logic(self, Logic):
		self.__Collision_Logic = Logic
