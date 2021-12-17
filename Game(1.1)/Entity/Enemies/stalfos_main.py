#here will be the Stalfos's controller
from .enemy_main import Enemy_Main
from .stalfos_info import Stalfos_Info
from Engine import *

import keyboard #temporary
import random

class Stalfos_Main(Enemy_Main):
	def __init__(self, iNode, clNode, cNode, kNode, ID):
		Enemy_Main.__init__(self)
		#iNode == Image_Node
		#clNode == Collision_Node
		self.__cLogic = clNode
		self.__cNode  = cNode
		self.__kNode  = kNode
		self.__iNode  = iNode
		self.__info	  = Stalfos_Info(ID)
		self.__rand   = random

		#----Keyboard inputs----#
		self.__key_up		= 'w'
		self.__key_down		= 's'
		self.__key_left		= 'a'
		self.__key_right	= 'd'

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
		Img_info = self.__iNode.Img_Add('z_Pictures/bloodboy.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/bloodboy.png')

		#placing the img
		self.__x = 0
		self.__y = 0
		x, y = self.__info.get_size()
		self.__x = int(self.__rand.randint((32+x), Sc_Width-(32+x)))
		self.__y = int(self.__rand.randint((32+y), Sc_Height-(32+y)))
		img_coords = self.__iNode.Img_Place(x=self.__x, y=self.__y, image=self.__info.get_TKimg(), tag=[ID, self.__info.get_group_ID()])

		#final set of information save to stalfos
		Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
		Coords = img_coords
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Stalfos_Data(Coords=Coords, Speed=5, health=1000, defense=5, attack=2) #check stalfos_info for, well info.
		self.__kNode.set_Speed(self.__info.get_Speed())
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
			# print(self.__var, S#82)
			self.__var += 11

		self.__kNode.set_Speed(5)
		if self.__randNum == 0:
			# direction = "left"
			direction = "up"
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True
		elif self.__randNum == 1:
			direction = "right"
			# direction = 'left'
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True
		elif self.__randNum == 2:
			# direction = "left"
			direction = "down"
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True
		elif self.__randNum == 3:
			direction = "left"
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__info.get_ID(), direction)#, neg=False)
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
			self.__isMoving = True

	def Stal_Attack(self):
		pass

		#OSC == Other Side of Collision, it represents the other object that collided with player
		#OSA == Other Side's Attack, represents the other objects needed parameters. Ex. dmg
		#stal_key == The stalfos that is under collision
	def my_Collision(self, OSC=None, OSA=None, side=None, a=None):
		if self.__isHit == False:
			if OSC == 'Weapon':
				lastSide = None
				Dir = None
				'''#_Actuall MATH_#'''
				self.__Cur_Health -= OSA
				print(self.__Cur_Health, 'health')
				for newSide in side:
					if newSide == 'top':
						Dir = 'up'
					elif newSide == 'bottom':
						Dir = 'down'
					else:
						Dir = newSide
					for time in range(50):
						new_Coords = self.__kNode.Knock_Back(self.__info.get_Coords(), self.__info.get_ID(), Dir)
						self.__info.set_Coords(new_Coords)
						self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
						x1, y1, x2, y2 = Image_Node.Render.bbox(self.__info.get_ID())
						# print(x1, y1, x2, y2)
						# print(self.__cLogic.ForT_Collision(x1=x1, y1=y1, x2=x2, y2=y2), 'EHHH')
						listYES = self.__cLogic.ForT_Collision(x1=x1, y1=y1, x2=x2, y2=y2)
						if listYES != None:
							# print(listYES, 'yes')
							for obj in listYES:
								if obj != None:
									if obj.get_group_ID() in a:
										# print('wallHIT')
										Dir = self.__cLogic.Side_Calc(self.__cLogic.tagToObj(self.__info.get_ID()))
										self.my_Collision(OSC='Static', side=Dir)
										return


				'''#_Logic_#'''
				self.__isHit 	= True
				self.__saveTime = Timer_Node.GameTime
				self.__isAlive  = self.isAlive()

			elif OSC == 'Static':
				lastSide = None
				# print(side)
				for newSide in side:
					if newSide == 'top':
						thisisA = 'up'
					elif newSide == 'bottom':
						thisisA = 'down'
					else:
						thisisA = newSide
					new_Coords = self.__kNode.Static_Hit(self.__info.get_Coords(), self.__info.get_ID(), thisisA)
					self.__info.set_Coords(new_Coords)
					self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))

			elif OSC == 'Friend':
				lastSide = None
				for newSide in side:
					if newSide == 'top':
						Dir = 'up'
					elif newSide == 'bottom':
						Dir = 'down'
					else:
						Dir = newSide
					for time in range(50):
						new_Coords = self.__kNode.Knock_Back(self.__info.get_Coords(), self.__info.get_ID(), Dir)
						self.__info.set_Coords(new_Coords)
						self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
						x1, y1, x2, y2 = Image_Node.Render.bbox(self.__info.get_ID())
						# print(x1, y1, x2, y2)
						# print(self.__cLogic.ForT_Collision(x1=x1, y1=y1, x2=x2, y2=y2), 'EHHH')
						listYES = self.__cLogic.ForT_Collision(x1=x1, y1=y1, x2=x2, y2=y2)
						if listYES != None:
							# print(listYES, 'yes')
							for obj in listYES:
								if obj != None:
									if obj.get_group_ID() in a:
										# print('wallHIT')
										Dir = self.__cLogic.Side_Calc(self.__cLogic.tagToObj(self.__info.get_ID()))
										self.my_Collision(OSC='Static', side=Dir)
										return

	def reset_hit(self):
		if Timer_Node.GameTime == self.__saveTime+5:
			self.__isHit = False
			# print('Stalfos Can Get Hit')
			# print(self.__Cur_Health, ':Stalfos Health')

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


	"""#|--------------Getters--------------|#"""
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


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Collision_Logic(self, Logic):
		self.__cLogic = Logic
