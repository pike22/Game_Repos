#potentially new one!!
class Arrow_Info():
	def __init__(self):
		self.__file_Location = None
		self.__ID			= None
		self.__group_ID		= "#arrow"
		self.__Canvas_ID	= {}
		self.__imgPIL_ID	= {}
		self.__imgTK_ID		= {}
		self.__img_size		= {} #(x, y)tuple of height, width
		self.__Corners		= {} #(x1, y1, x2, y2) tuple
		self.__Coords		= {} #(x, y) location
		#Parameters
		self.__attack_damage = None


	def Image_Data(self, ID, Size, PIL_img, TK_img):
		self.__imgPIL_ID[ID] = PIL_img
		self.__imgTK_ID[ID]	 = TK_img
		self.__img_size[ID]	 = Size

	def Arrow_Data(self, attack): #add more here as needed.
		self.__attack_damage = attack


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_attack(self):
		return self.__attack_damage

	def get_ID(self):
		return self.__ID

	def get_group_ID(self):
		return self.__group_ID

	def get_canvasID(self):
		return self.__Canvas_ID

	def get_Corners(self):
		return self.__Corners

	def get_Coords(self):
		return self.__Coords

	def get_TKimg(self):
		return self.__imgTK_ID

	def get_ID(self):
		return self.__ID

	def get_Size(self):
		return self.__img_size

	def get_group_ID(self):
		return self.__group_ID


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Canvas_ID(self, ID=ID, Canvas_ID=Canvas_ID):
		self.__Canvas_ID[ID] = Canvas_ID

	def set_Corners(self, ID, Corners):
		self.__Corners[ID] = Corners

	def set_Coords(self, ID, Coords):
		self.__Coords[ID] = Coords

	def set_ID(self, ID):
		self.__ID = ID

	def set_fileLocation(self, file):
		self.__file_Location = file


	"""------------------------------------------------------------------------------
	---------------------------------------------------------------------------------
	------------------------------------------------------------------------------"""


#old one
class Arrow_Info():
	def __init__(self):
		self.__file_Location = None
		self.__Canvas_ID	= None
		self.__imgPIL_ID	= None
		self.__imgTK_ID		= None
		self.__group_ID		= "#arrow"
		self.__ID			= "P#A001"
		self.__img_size		= None #(x, y)tuple of height, width
		self.__Corners		= None #(x1, y1, x2, y2) tuple
		self.__Coords		= None #(x, y) location
		#Parameters
		self.__attack_damage = None


	def Image_Data(self, Size, PIL_img, TK_img, file_Location):
		self.__file_Location	= file_Location
		self.__imgPIL_ID		= PIL_img
		self.__imgTK_ID			= TK_img
		self.__img_size			= Size

	def Arrow_Data(self, attack, Coords): #add more here as needed.
		self.__attack_damage = attack
		self.__Coords = Coords


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_attack(self):
		return self.__attack_damage

	def get_ID(self):
		return self.__ID

	def get_group_ID(self):
		return self.__group_ID

	def get_canvasID(self):
		return self.__Canvas_ID

	def get_Corners(self):
		return self.__Corners

	def get_Coords(self):
		return self.__Coords

	def get_TKimg(self):
		return self.__imgTK_ID

	def get_ID(self):
		return self.__ID

	def get_Size(self):
		return self.__img_size

	def get_group_ID(self):
		return self.__group_ID


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Canvas_ID(self, ID):
		self.__Canvas_ID = ID

	def set_Corners(self, Corners):
		self.__Corners = Corners

	def set_Coords(self, Coords):
		self.__Coords = Coords
