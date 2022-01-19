#here will be the information of the enemy "Stalfos"

class Stalfos_Info():
	"""
	This is Where wall info is stored.

	Methods
	-------
	init(ID)
		This is required when Stalfos_Info() is called
	Image_Data(Size, PIL_img, TK_img, file_Location)
		Stores the images render data.
	Stalfos_Data(Coords, Speed, health, defense, attack)
		Stores the stalfos game data.
	"""
	def __init__(self, ID):
		#engine based Parameters.
		self.__file_Location = None #holds the images file location
		self.__img_size		 = None #(x, y)tuple of height, width
		self.__group_ID		 = "#stalfos"
		self.__Canvas_ID	 = None
		self.__imgPIL_ID	 = None
		self.__imgTK_ID		 = None
		self.__Corners		 = None #(x1, y1, x2, y2) tuple
		self.__Coords	 	 = None #constantly saves current coords in tuple: (x, y), list of tuple
		self.__ID			 = ID
		self.__Speed 		 = None
		#Game Mechanical Parameters.
		self.__base_health	= None
		self.__base_defense	= None
		self.__base_attack	= None


	def Image_Data(self, Size=None, PIL_img=None, TK_img=None, file_Location=None):
		"""
		:meta private:
		"""
		self.__file_Location	= file_Location
		self.__imgPIL_ID		= PIL_img
		self.__imgTK_ID			= TK_img
		self.__img_size			= Size

	def Stalfos_Data(self, Coords=None, Speed=None, health=None, defense=None, attack=None): #add more here as needed.
		"""
		:meta private:
		"""
		self.__base_health	= health
		self.__base_defense	= defense
		self.__base_attack	= attack
		self.__Coords		= Coords
		self.__Speed 		= Speed


		#Switch the def get_1 /get_2 to the same format as get_ID
	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...

	def get_TKimg(self):
		"""
		:meta private:
		"""
		return self.__imgTK_ID

	def get_Speed(self):
		"""
		:meta private:
		"""
		return self.__Speed

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__Coords

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__img_size

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__Corners

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

		#_attack, health, defense_#
	def get_attack(self):
		"""
		:meta private:
		"""
		return self.__base_attack

	def get_health(self):
		"""
		:meta private:
		"""
		return self.__base_health

	def get_defense(self):
		"""
		:meta private:
		"""
		return self.__base_defense


	"""#|--------------Setters--------------|#"""
	def set_Coords(self, Coords):
		"""
		:meta private:
		"""
		self.__Coords = Coords

	def set_Canvas_ID(self, Canvas_ID):
		"""
		:meta private:
		"""
		self.__Canvas_ID = Canvas_ID

	def set_Corners(self, bbox):
		"""
		:meta private:
		"""
		self.__Corners = bbox
