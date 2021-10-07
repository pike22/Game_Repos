#here will be the "Storage" container for player's information.

class Player_Info():
	def __init__(self):
		#engine based Parameters.
		self.__file_Location = None
		self.__Player_Speed  = None
		#self.__Collision_Box = None #this is no longer needed
		self.__Cur_Coords 	= None #constantly saves current coords in tuple: (x, y)
		self.__Canvas_ID	= None
		self.__group_ID		= 'player'
		self.__ID			= 'P#001'
		self.__imgPIL_ID	= None
		self.__imgTK_ID		= None
		self.__img_size		= None #(x, y)tuple of height, width
		self.__Corners		= None #(x1, y1, x2, y2) tuple
		self.__group_ID		= None

		#Game Mechanical Parameters. Totals
		self.__base_health	= None
		self.__base_defense	= None
		self.__base_attack	= None


	def Image_Data(self, Size, group_ID, PIL_img, TK_img, file_Location):
		self.__file_Location	= file_Location
		self.__imgPIL_ID		= PIL_img
		self.__imgTK_ID			= TK_img
		self.__img_size			= Size
		self.__group_ID			= group_ID

	def Player_Data(self, Cur_Coords, Speed, health, defense, attack): #add more here as needed.
		self.__Player_Speed	= Speed
		self.__base_defense	= defense
		self.__base_health	= health
		self.__base_attack	= attack
		self.__Cur_Coords	= Cur_Coords


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...

	def get_TKimg(self):
		return self.__imgTK_ID

	def get_Speed(self):
		return self.__Player_Speed

	def get_Coords(self):
		return self.__Cur_Coords

	def get_Size(self):
		return self.__img_size

	def get_Corners(self):
		return self.__Corners

	def get_ID(self):
		return self.__ID

	def get_group_ID(self):
		return self.__group_ID

		#_attack, health, defense_#
	def get_attack(self):
		return self.__base_attack

	def get_health(self):
		return self.__base_health

	def get_defense(self):
		return self.__base_defense


	"""|--------------Setters--------------|#"""
	def set_Coords(self, Coords):
		self.__Cur_Coords = Coords

	def set_Canvas_ID(self, Canvas_ID):
		self.__Canvas_ID = Canvas_ID

	def set_Corners(self, bbox):
		self.__Corners = bbox

	def set_Collision_Box(self, BOX):
		self.__Collision_Box = BOX
