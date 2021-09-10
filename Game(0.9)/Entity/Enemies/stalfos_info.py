#here will be the information of the enemy "Stalfos"

class Stalfos_Info():
	def __init__(self):
		#engine based Parameters.
		self.__file_Location = None #holds the images file location
		self.__img_size		 = None #(x, y)tuple of height, width
		self.__Stalfos_Speed = None
		self.__group_ID		 = None
		self.__Cur_Coords	 = [] #constantly saves current coords in tuple: (x, y), list of tuple
		self.__Canvas_ID	 = []
		self.__imgPIL_ID	 = []
		self.__imgTK_ID		 = []
		self.__Corners		 = [] #(x1, y1, x2, y2) tuple
		self.__ID			 = []
		#Game Mechanical Parameters.
		self.__base_health	= None
		self.__base_defense	= None
		self.__base_attack	= None


	def Image_Data(self, Size, ID, group_ID, PIL_img, TK_img, file_Location):
		self.__file_Location	= file_Location
		self.__group_ID			= group_ID
		self.__img_size			= Size
		self.__imgPIL_ID.append(PIL_img)
		self.__imgTK_ID.append(TK_img)
		self.__ID.append(ID)

	def Stalfos_Data(self, Cur_Coords, Speed, health, defense, attack): #add more here as needed.
		self.__Stalfos_Speed = Speed
		self.__base_health	 = health
		self.__base_defense	 = defense
		self.__base_attack	 = attack
		self.__Cur_Coords.append(Cur_Coords)


	"""|--------------Getters--------------|#"""
	def get_TKimg(self, item):
		return self.__imgTK_ID[item]

	def get_Speed(self):
		return self.__Stalfos_Speed

	def get_Coords(self, item):
		return self.__Cur_Coords[item]

	def get_CanvasID(self, item):
		return self.__Canvas_ID[item]

	def get_CanvasID2(self):
		return self.__Canvas_ID

	def get_Size(self):
		return self.__img_size

	def get_Corners(self, item):
		return self.__Corners[item]

	def get_Corners2(self):
		return self.__Corners

	def get_ID(self, item):
		return self.__ID[item]

	def get_ID2(self):
		return self.__ID

	def get_attack(self):
		return self.__base_attack

	def get_health(self):
		return self.__base_health

	def get_defense(self):
		return self.__base_defense


	"""|--------------Setters--------------|#"""
	def set_Coords(self, Coords):
		self.__Cur_Coords.append(Coords)

	def set_Canvas_ID(self, Canvas_ID):
		self.__Canvas_ID.append(Canvas_ID)

	def set_Corners(self, bbox):
		self.__Corners.append(bbox)
