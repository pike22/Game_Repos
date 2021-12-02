from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .img_info import IMG_Info


class GUI_Statics():
	def __init__(self, group_ID):
		self.__info   = IMG_Info(group_ID)
		self.__tkIMG  = None
		self.__pilIMG = None


	"""Local Dictionary"""
	def add_IMG(self, tkIMG, pilIMG):
		self.__tkIMG  = tkIMG
		self.__pilIMG = pilIMG
		pass #this will add target img to the dictionary


	"""IMG_INFO CLASS"""
	def Img_Info(self, tkIMG, pilIMG, fLocation):
		self.__info.Image_Data(Size=pilIMG.size, PIL_img=pilIMG, TK_img=tkIMG, file_Location=fLocation)

	def Placed_imgInfo(self, ID, Corners, Coords, pilIMG, tkIMG):
		if tkIMG == None and pilIMG == None:
			self.__info.Placed_imgData(ID=ID, Corners=Corners, Coords=Coords, pilIMG=self.__pilIMG, tkIMG=self.__tkIMG)
		else:
			self.__info.Placed_imgData(ID=ID, Corners=Corners, Coords=Coords, pilIMG=pilIMG, tkIMG=tkIMG)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_pilIMG(self):
		return self.__pilIMG

	def get_tkIMG(self):
		return self.__tkIMG

	def get_ID(self, item=None, full=True):
		return self.__info.get_ID(item=item, full=full)

	def get_fileLocation(self):
		return self.__info.get_fileLocation()

	def show_PLC_Data(self):
		self.__info.show_PLC_Data()

	def get_PLC_tkIMG(self, key):
		return self.__info.get_PLC_tkIMG(key)

	def get_PLC_pilIMG(self, key):
		return self.__info.get_PLC_pilIMG(key)

	def get_PLC_Coords(self, key):
		return self.__info.get_PLC_Coords(key)

	def	get_PLC_Corners(self, key):
		return self.__info.get_PLC_Corners(key)

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_ID(self, ID):
		self.__info.set_ID(ID)
