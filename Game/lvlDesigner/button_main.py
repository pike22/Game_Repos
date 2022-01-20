from .button_info import Button_Info

class Button_Main():
	"""
	Currently just a connection between alpha_lvd.py and button_info.py

	Methods
	-------
	init(button_ID, widget)
		This is required when Button_Main() is called
	Image_Info(fileLoc, tkIMG, pilIMG, size)
		Stores File based data to the button_info.py file.
	"""
	def __init__(self, button_ID, widget_ID):
		self.__info = Button_Info(button_ID)
		self.__widgID = widget_ID

	def Image_Info(self, fileLoc, tkIMG, pilIMG, size):
		"""
		:meta private:
		"""
		self.__info.Image_Data(fileLoc=fileLoc, tkIMG=tkIMG, pilIMG=pilIMG, size=size)


	"""|--------------Getters--------------|#"""
	#this is where a list of getters will go...
	def get_widgID(self):
		"""
		:meta private:
		"""
		return self.__widgID

	def get_button_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_button_ID()

	def get_Size(self):
		"""
		:meta private:
		"""
		return self.__info.get_Size()

	def get_tkIMG(self):
		"""
		:meta private:
		"""
		return self.__info.get_tkIMG()

	def get_pilIMG(self):
		"""
		:meta private:
		"""
		return self.__info.get_pilIMG()

	def get_fileLoc(self):
		"""
		:meta private:
		"""
		return self.__info.get_fileLoc()
