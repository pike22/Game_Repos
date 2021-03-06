from Engine.timer_node import Timer_Node
from Engine.image_node import Image_Node
from .sword_info import Sword_Info

class Sword_Main():
	"""
	The main class the does everything that is with a sword.

	Methods
	-------
	init(iNode, cLogic, cNode, kNode)
		This is required when Sword_Main() is called		
	"""
	def __init__(self, iNode, cLogic):
		self.__iNode	 = iNode
		self.__cLogic = cLogic
		self.__info		 = Sword_Info()

		self.__itemCount = 0
		self.__saveTime	 = 0
		self.__isActive	 = False


	def sword_setUP(self):
		"""
		Sets up the basic information of the sword.
		"""
		#img setup
		Img_info = self.__iNode.Img_Add('z_Pictures/notasword.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/notasword.png')
		self.__info.Sword_Data(2) #check melee_info for well info.



	def use_Sword(self, x, y, direction):
		"""
		Displayes the weapon on screen as well as all of the parameters that go with it.

		Parameters
		---------
		direction : str
			The direction that the attack happens.
		x, y : int
			The coords that the weapon will be placed at.
		"""
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		if self.__isActive == False:
			self.__info.set_Coords(Coords=(x, y))

			if direction == 'up':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 90)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
			if direction == 'down':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 270)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
			if direction == 'left':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 180)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
			if direction == 'right':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 0)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])

			Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
			self.__info.set_Canvas_ID(Canvas_ID)
			Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
			self.__saveTime = Timer_Node.GameTime

			self.__isActive = True
			self.__itemCount += 1

	def Weapon_Active(self):
		"""
		Deactivates the weapon after a set amount of time.
		"""
		if Timer_Node.GameTime == (self.__saveTime+9):
			Image_Node.Render.delete(self.__info.get_ID())
			self.__isActive = False
			self.__itemCount -= 1

	def del_item(self):
		"""
		Delets the displayed weapon image on the tkinter window.
		"""
		Image_Node.Render.delete(self.__info.get_ID())
		self.__isActive = False



	def Sword_Print(self):
		"""
		:meta private:
		"""
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Sword Data:')
		print(self.__info.get_ID(), '\t:ID') #should be None
		print(self.__info.get_Attack_Dmg(), '\t:Attck')
		print('-----------------------------------')
		print('')

		#this may not be needed, depends for now.
	def my_Collision(self):
		"""
		:meta private:
		"""
		pass



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_attack(self):
		"""
		:meta private:
		"""
		return self.__info.get_Attack_Dmg()

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__info.get_size()

	def get_isActive(self):
		"""
		:meta private:
		"""
		return self.__isActive

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__info.get_Coords()

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__info.get_Corners()

	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_ID()

	def get_PILimg(self):
		"""
		:meta private:
		"""
		return self.__info.get_PILimg()

	def get_TKimg(self):
		"""
		:meta private:
		"""
		return self.__info.get_TKimg()

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_group_ID()

	def get_itemCount(self):
		"""
		:meta private:
		"""
		return self.__itemCount


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_IsWeapon(self, Fort):
		"""
		:meta private:
		"""
		self.__isActive = Fort
