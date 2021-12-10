
class PLC_ImgInfo():
	def __init__(self, ID, button_ID):
		self.__button_ID  = button_ID
		self.__group_ID   = '#wall'
		self.__ID 		  = ID
		self.__size 	  = None
		self.__Coords 	  = None
		self.__Corners	  = None
		self.__fileLoc 	  = None
		self.__rotation   = None
		self.__CCollision = None


	def Image_Data(self, fileLoc, size, coords, CCollision, rotation):
		self.__CCollision = CCollision
		self.__rotation   = rotation
		self.__fileLoc 	  = fileLoc
		self.__Corners	  = (coords[0], coords[1], coords[0]+32, coords[1]+32)
		self.__Coords 	  = coords
		self.__size 	  = size


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_ID(self):
		return self.__ID

	def get_group_ID(self):
		return self.__group_ID

	def get_button_ID(self):
		return self.__button_ID

	def get_Size(self):
		return self.__Size

	def get_Coords(self):
		return self.__Coords

	def get_fileLoc(self):
		return self.__fileLoc

	def get_Corners(self):
		return self.__Corners

	def get_rotation(self):
		return self.__rotation

	def get_CCollision(self):
		return self.__CCollision


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_group_ID(self, ID):
		self.__group_ID = ID
