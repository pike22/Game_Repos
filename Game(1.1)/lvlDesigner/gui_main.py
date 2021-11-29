from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_events import GUI_Events


class GUI_Main():
	def __init__(self, iNode, kNode, mainApp, color):
		self.__iNode  = iNode
		self.__kNode  = kNode
		self.__mainApp= mainApp
		self.__color  = color
		self.__eGUI	  = GUI_Events(iNode, kNode, mainApp, color)
		self.__ImgList= None

		#Img variables
		self.__pilIMG	 = None
		self.__tkIMG	 = None
		self.__IMG		 = None


	def windowSETUP(self):
		"""#__Frame Creation & Placement__#"""
		self.__ImgList	  = LabelFrame(self.__mainApp, text="Imported", width=250, height=600, bg=self.__color)

		self.__ImgList.grid(row=0, column=2)

		for frame in [self.__ImgList, ]:#self.__projWindow, ]:
			frame.grid_propagate(0)

		"""#__event Calls__#"""
		#NOTHING YET

		"""#__Button Creation & Placement__#"""
		self.__Import = Button(self.__mainApp, text='Import',width=32,height=2, command=lambda:self.__eGUI.openFiles(self.__ImgList))

		self.__Import.grid(row=1, column=2)

		for frame in [self.__Import, ]:
		    frame.grid_propagate(0)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	#def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_frame
