
class Bow_Info():
	def __init__(self):
		self.__file_Location = None
		self.__Canvas_ID	= None
		self.__imgPIL_ID	= None
		self.__imgTK_ID		= None
		self.__group_ID		= '#bow'
		self.__ID 			= 'W#B001'
		self.__img_size		= None #(x, y)tuple of height, width
		self.__Corners		= None #(x1, y1, x2, y2)tuple
		#Parameters
		self.__attack_damage = None


	def Image_Data(self, Size, PIL_img, TK_img, file_Location):
		self.__file_Location 	= file_Location
		self.__imgPIL_ID		= PIL_img
		self.__imgTK_ID			= TK_img
		self.__img_size			= Size

	def Bow_Data(self, attack): #add more here as needed.
		self.__attack_damage = attack


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Attack_Dmg(self):
		return self.__attack_damage

	def get_ID(self):
		return self.__ID

	def get_group_ID(self):
		return self.__group_ID

	def get_Corners(self):
		return self.__Corners

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
