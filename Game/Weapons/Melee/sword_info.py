
class Sword_Info():
	"""
	This is where all of the Swords data is saved.

	Methods
	-------
	Image_Data(Size, PIL_img, TK_img, file_Location)
		Saves the technical side of the player info.
	Sword_Data(attack)
		Saves the game side of the player info.
	"""
	def __init__(self):
		self.__file_Location = None
		self.__Canvas_ID	= None
		self.__imgPIL_ID	= None
		self.__imgTK_ID		= None
		self.__group_ID		= "#sword"
		self.__ID			= "W#S001"
		self.__img_size		= None #(x, y)tuple of height, width
		self.__Corners		= None #(x1, y1, x2, y2) tuple
		self.__Coords 		= None #(x, y) posistion
		#Parameters
		self.__attack_damage = None


	def Image_Data(self, Size, PIL_img, TK_img, file_Location):
		"""
		:meta private:
		"""
		self.__file_Location	= file_Location
		self.__imgPIL_ID		= PIL_img
		self.__imgTK_ID			= TK_img
		self.__img_size			= Size

	def Sword_Data(self, attack): #add more here as needed.
	"""
	:meta private:
	"""
		self.__attack_damage = attack


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Attack_Dmg(self):
		"""
		:meta private:
		"""
		return self.__attack_damage

	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__ID

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__group_ID

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__Coords

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__Corners

	def get_TKimg(self):
		"""
		:meta private:
		"""
		return self.__imgTK_ID

	def get_PILimg(self):
		"""
		:meta private:
		"""
		return self.__imgPIL_ID

	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__ID

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__img_size

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__group_ID


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Canvas_ID(self, ID):
		"""
		:meta private:
		"""
		self.__Canvas_ID = ID

	def set_Corners(self, Corners):
		"""
		:meta private:
		"""
		self.__Corners = Corners

	def set_Coords(self, Coords):
		"""
		:meta private:
		"""
		self.__Coords = Coords

	def set_TKimg(self, TKimg):
		"""
		:meta private:
		"""
		self.__imgTK_ID = TKimg
