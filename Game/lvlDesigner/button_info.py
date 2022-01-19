
class Button_Info():
	"""
	Method
	------
	init(button_ID)
		This is required when Button_Info() is called
	Image_Data(fileLoc, tkIMG, pilIMG, size)
		Stores File based data.
	"""
	def __init__(self, button_ID):
		"""
		:meta private:
		"""
		self.__button_ID = button_ID
		self.__fileLoc 	 = None
		self.__pilIMG 	 = None
		self.__tkIMG 	 = None
		self.__Size		 = None

	def Image_Data(self, fileLoc, tkIMG, pilIMG, size):
		"""
		:meta private:
		"""
		self.__fileLoc 	 = fileLoc
		self.__pilIMG 	 = pilIMG
		self.__tkIMG 	 = tkIMG
		self.__Size		 = size

	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_button_ID(self):
		"""
		:meta private:
		"""
		return self.__button_ID

	def get_Size(self):
		"""
		:meta private:
		"""
		return self.__Size

	def get_tkIMG(self):
		"""
		:meta private:
		"""
		return self.__tkIMG

	def get_pilIMG(self):
		"""
		:meta private:
		"""
		return self.__pilIMG

	def get_fileLoc(self):
		"""
		:meta private:
		"""
		return self.__fileLoc
