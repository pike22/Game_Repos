
from .plc_imginfo import PLC_ImgInfo
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import *

class PLC_ImgMain():
	"""
	Grabs then stores the Placed Images (*PLC_Img*) data into another class.
	"""
	def __init__(self, ID, button_ID):
		self.__info = PLC_ImgInfo(ID, button_ID)

	def Image_Info(self, fileLoc, size, coords, rotation, CCollision=None):
		"""
		:meta private:
		"""
		self.__info.Image_Data(fileLoc, size, coords, CCollision, rotation)

	# def ...(self, ):
	# 	This will be for future functions that may need to be
	# 	Created.


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_ID()

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_group_ID()

	def get_button_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_button_ID()

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__info.get_size()

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__info.get_Coords()

	def get_fileLoc(self):
		"""
		:meta private:
		"""
		return self.__info.get_fileLoc()

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__info.get_Corners()

	def get_rotation(self):
		"""
		:meta private:
		"""
		return self.__info.get_rotation()

	def get_CCollision(self):
		"""
		:meta private:
		"""
		return self.__info.get_CCollision()



	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_group_ID(self, ID):
		"""
		:meta private:
		"""
		self.__group_ID = ID
