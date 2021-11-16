from Engine.timer_node import Timer_Node
from Engine.image_node import Image_Node
from .bow_info import Bow_Info
from .Projectiles import *

class Bow_Main():
	def __init__(self, iNode, cLogic, cNode):
		self.__Image	 = iNode
		self.__Col_logic = cLogic
		self.__Col_node	 = cNode
		self.__info		 = Bow_Info()
		self.__ammo		 = None

		self.__attack	  = 0
		self.__itemCount  = 0
		self.__saveTime   = 0
		self.__isActive   = False
		self.__projActive = False


	def bow_setUP(self):
		#img setup
		Img_info = self.__Image.Img_Add('z_Pictures/red_bow.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/red_bow.png')
		self.__info.Bow_Data(2) #check melee_info for well info.

		#self.output = self.Image.

	def use_Bow(self, x, y, direction):
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		height, width = self.__info.get_size()
		if self.__isActive == False:
			self.__Image.Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=ID)
			self.__Collision.add_Col_Dict(self.__ammo.get_ID(), self.__ammo)

			if direction == 'up':
				self.__ammo.use_Arrow(x, (y-width), 'up', dmgMod=self.__info.get_attackMOD())
			elif direction == 'down':
				self.__ammo.use_Arrow(x, (y+width), 'down', dmgMod=self.__info.get_attackMOD())
			elif direction == 'right':
				self.__ammo.use_Arrow((x+height), y, 'right', dmgMod=self.__info.get_attackMOD())
			elif direction == 'left':
				self.__ammo.use_Arrow((x-height), y, 'left', dmgMod=self.__info.get_attackMOD())


			Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
			self.__info.set_Canvas_ID(Canvas_ID)
			Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
			self.__saveTime = Timer_Node.GameTime
			self.__isActive = True
			self.__projActive = True
			self.__itemCount += 1


	def Weapon_Active(self):
		if Timer_Node.GameTime == (self.__saveTime+9):
			Image_Node.Render.delete(self.__info.get_ID())
			self.__isActive = False
			self.__itemCount -= 1

	def proj_Active(self):
		if self.__projActive == True:
			self.__ammo.isActive()

	def del_item(self):
		Image_Node.Render.delete(self.__info.get_ID())
		self.__isActive = False
		# self.__Collision.del_Col_Dict(self.__ammo.get_ID())
		# self.__ammo.del_Arrow()



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



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_attackMOD(self):
		return self.__info.get_AttackMOD()

	def get_attack(self):
		return self.__attack

	def get_size(self):
		return self.__info.get_size()

	def get_isActive(self):
		return self.__isActive

	def get_projActive(self):
		return self.__projActive

	def get_projCorners(self):
		return self.__ammo.get_Corners()

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_itemCount(self):
		return self.__itemCount

	def get_ammoCount(self):
		return self.__ammoCount


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_IsWeapon(self, Fort):
		self.__isActive = Fort

	def set_ammo(self, ammo):
		self.__ammo = ammo
