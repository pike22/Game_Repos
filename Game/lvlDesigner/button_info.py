
class Button_Info():
	def __init__(self, button_ID):
		self.__button_ID = button_ID
		self.__fileLoc 	 = None
		self.__pilIMG 	 = None
		self.__tkIMG 	 = None
		self.__Size		 = None

	def Image_Data(self, fileLoc, tkIMG, pilIMG, size):
		self.__fileLoc 	 = fileLoc
		self.__pilIMG 	 = pilIMG
		self.__tkIMG 	 = tkIMG
		self.__Size		 = size

	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_button_ID(self):
		return self.__button_ID

	def get_Size(self):
		return self.__Size

	def get_tkIMG(self):
		return self.__tkIMG

	def get_pilIMG(self):
		return self.__pilIMG

	def get_fileLoc(self):
		return self.__fileLoc
