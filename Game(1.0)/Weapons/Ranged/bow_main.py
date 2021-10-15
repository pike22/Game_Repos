from Engine.timer_node import Timer_Node
from Engine.image_node import Image_Node
from .bow_info import Bow_Info
from .Projectiles import *

class Bow_Main():
	def __init__(self, iNode):
		self.__Image	= iNode
		self.__info		= Bow_Info()

		self.__saveTime = 0
		self.__isActive = False


	def Bow_setUP(self):
		#img setup
		Img_info = self.__Image.Img_Add('z_Pictures/red_bow.png')
		print(Img_info[1], 'size')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/red_bow.png')
		self.__info.Bow_Data(2) #check melee_info for well info.

		#self.output = self.Image.

	def use_Bow(self, x, y):
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		if self.__isActive == False:
			self.__Image.Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=ID)

			Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
			self.__info.set_Canvas_ID(Canvas_ID)
			Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
			self.__saveTime = Timer_Node.GameTime
			self.__isActive = True

	def Weapon_Active(self):
		if Timer_Node.GameTime == (self.__saveTime+9):
			self.__isActive = False
			Image_Node.Render.delete(self.__info.get_ID())

	def del_Bow(self):
		self.__isActive = False
		Image_Node.Render.delete(self.__info.get_ID())



	def Bow_Print(self):
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Bow Data:')
		print(self.__info.get_ID(), '\t:ID') #should be None
		print(self.__info.get_Attack_Dmg(), '\t:Attck')
		print('-----------------------------------')
		print('')

		#this may not be needed, depends for now.
	def my_Collision(self):
		pass



	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_attack(self):
		return self.__info.get_Attack_Dmg()

	def get_Size(self):
		return self.__info.get_Size()

	def get_isActive(self):
		return self.__isActive

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_IsWeapon(self, Fort):
		self.__isActive = Fort
