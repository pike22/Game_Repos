
class PLC_ImgInfo():
	"""
	Where data for the Placed Images (*PLC*) go.

	Methods
	-------
	init(ID, button_ID)
		This is required when PLC_ImgInfo() is called
	"""
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
		"""
		:meta private:
		"""
		self.__CCollision = CCollision
		self.__rotation   = rotation
		self.__fileLoc 	  = fileLoc
		self.__Corners	  = (coords[0], coords[1], coords[0]+32, coords[1]+32)
		self.__Coords 	  = coords
		self.__size 	  = size


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
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

	def get_button_ID(self):
		"""
		:meta private:
		"""
		return self.__button_ID

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__size

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__Coords

	def get_fileLoc(self):
		"""
		:meta private:
		"""
		return self.__fileLoc

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__Corners

	def get_rotation(self):
		"""
		:meta private:
		"""
		return self.__rotation

	def get_CCollision(self):
		"""
		:meta private:
		"""
		return self.__CCollision


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_group_ID(self, ID):
		"""
		:meta private:
		"""
		self.__group_ID = ID
