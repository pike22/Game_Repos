from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .img_info import IMG_Info


class GUI_Statics():
	def __init__(self, ID):
		self.__info   = IMG_Info(ID)
		self.__tkIMG  = None
		self.__pilIMG = None


	"""Local Dictionary"""
	def add_IMG(self, tkIMG, pilIMG):
		self.__tkIMG  = tkIMG
		self.__pilIMG = pilIMG
		pass #this will add target img to the dictionary


	"""IMG_INFO CLASS"""
	def info_Dump(self, ID, tkIMG, pilIMG, fLocation):
		self.__info.Image_Data(Size=pilIMG.size, PIL_img=pilIMG, TK_img=tkIMG, file_Location=fLocation)



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_pilIMG(self):
		return self.__pilIMG

	def get_tkIMG(self):
		return self.__tkIMG

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...
