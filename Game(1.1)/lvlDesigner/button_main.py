from .button_info import Button_Info

class Button_Main():
	def __init__(self, button_ID):
		self.__info = Button_Info(button_ID)

	def Image_Info(self, fileLoc, tkIMG, pilIMG, size):
		self.__info.Image_Data(fileLoc, tkIMG, pilIMG, size)


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_button_ID(self):
		return self.__info.get_button_ID()

	def get_Size(self):
		return self.__info.get_Size()

	def get_tkIMG(self):
		return self.__info.get_tkIMG()

	def get_pilIMG(self):
		return self.__info.get_pilIMG()

	def get_fileLoc(self):
		return self.__info.get_fileLoc()
