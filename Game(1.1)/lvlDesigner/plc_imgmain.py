from .plc_imginfo import PLC_ImgInfo
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import *

class PLC_ImgMain():
	def __init__(self, ID, button_ID):
		self.__info = PLC_ImgInfo(ID, button_ID)

	def Image_Info(self, fileLoc, size, coords, CCollision=None, rotation):
		self.__info.Image_Data(fileLoc, size, coords, CCollision, rotation)

	# def ...(self, ):
	# 	This will be for future functions that may need to be
	# 	Created.


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_button_ID(self):
		return self.__info.get_button_ID()

	def get_Size(self):
		return self.__info.get_Size()

	def get_Coords(self):
		return self.__info.get_Coords()

	def get_fileLoc(self):
		return self.__info.get_fileLoc()

	def get_rotation(self):
		return self.__info.get_rotation()

	def get_CCollision(self):
		return self.__info.get_CCollision()



	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_group_ID(self, ID):
		self.__group_ID = ID
