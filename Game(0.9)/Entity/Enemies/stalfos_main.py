#here will be the Stalfos's controller
import random
from .enemy_main import Enemy_Main
from .stalfos_info import Stalfos_Info
from Engine.kinetics_node import Kinetics_Node

import keyboard #temporary

class Stalfos_Main(Enemy_Main):
	def __init__(self, iNode):
		Enemy_Main.__init__(self)
		#iNode == Image_Node
		#cNode == Collision_Node
		self.__Collision_Logic = None
		self.__Kinetics		= Kinetics_Node(iNode)
		self.__info	 		= Stalfos_Info()
		self.__Image	 	= iNode
		self.__rand 		= random
		self.__x			= 0
		self.__y			= 0


	#this is to go at the end.
	def Stalfos_Print(self, item):
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Stalfos Data:')
		print(self.__info.get_ID(item), '\t:Entity ID')
		print(self.__info.get_CanvasID(item), '\t:Canvas ID')
		print(self.__info.get_Speed(), 	'\t:Speed')
		print(self.__info.get_health(),	'\t:Health')
		print(self.__info.get_defense(),	'\t:Defense')
		print(self.__info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self.__info.get_Size(), 	'\t\t:Size')
		print(self.__info.get_Coords(item), 	'\t\t:Coords')
		print(self.__info.get_Corners(item), 	'\t:Corners')
		print('-----------------------------------')

	#seting up player bellow
	def stalfos_initial_setUP(self, Sc_Width, Sc_Height, stalfosCount, priority):
		for item in range(stalfosCount):
			#img setup
			"""!!ITEM IS NOT STATIC!! **REFER HERE FOR FUTURE PROBLEMS CAUSED**"""
			if item < 10: #Spacific Entity ID
				ID = 'S#00'+str(item)
			elif item >= 10 and item < 100:
				ID = 'S#0'+str(item)
			group_ID = "#stalfos" #Stalfos Class ID
			Img_info = self.__Image.Img_Add('z_Pictures/RedBoy2.png')
			self.__info.Image_Data(Size=Img_info[1], ID=ID, group_ID=group_ID, PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/RedBoy2.png')

			#placing the img
			self.__x = 0
			self.__y = 0
			x, y = self.__info.get_Size()
			self.__x = self.__rand.randint((25+x), Sc_Width-(25+x))
			self.__y = self.__rand.randint((25+y), Sc_Height-(25+y))
			print(self.__x, self.__y, "Cords for stalfos:", ID)
			img_list, img_coords = self.__Image.Img_Place(self.__x, self.__y, self.__info.get_TKimg(item), Grid='no', tag=ID)

			#final set of information save to stalfos
			#print(item, ':List Item')
			Canvas_ID = self.__Image.get_Render().find_withtag(ID)[0] #finds my canvas ID numb.
			Coords = img_coords[Canvas_ID-1]
			self.__info.set_Canvas_ID(Canvas_ID)
			self.__info.Stalfos_Data(Cur_Coords=Coords, Speed=7, health=10, defense=5, attack=2) #check stalfos_info for, well info.
			self.__Kinetics.set_Speed(self.__info.get_Speed())
			self.__Image.get_Render().addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(self.__Image.get_Render().bbox(Canvas_ID))
			#self.__Image.get_Render().create_rectangle(self.__info.get_Corners(item))

			self.Stalfos_Print(item)
		print(self.__info.get_CanvasID2(), "list of stalfos Canvas_Id's")






	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Corners(self):
		return self.__info.get_Corners2()

	def get_ID(self):
		return self.__info.get_ID2()

	def get_Health(self):
		return self.__info.get_health()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Collision_Logic(self, Logic):
		self.__Collision_Logic = Logic