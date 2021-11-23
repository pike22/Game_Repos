#imports
from PIL import ImageTk, Image
# from alpha import Alpha
from lvlDesigner import *
from z_Pictures import *
from colored import fg
from tkinter import *
from tkinter import filedialog
from Weapons import *
from Engine import *
from Entity import *
import keyboard
import mouse

class Alpha_LVD():
	BGcolor = 'Grey'
	def __init__(self, ):
		self.__Sc_Width	 = 1400
		self.__Sc_Height = 700
		self.__version	 = "Level Designer [ALPHAv0.0]"
		self.__color 	 = 'Grey'

		"""Class Call's"""
		self.__mainApp	= Tk()
		self.__tNode	= Timer_Node(self.__mainApp)
		self.__iNode	= Image_Node()
		self.__kNode	= Kinetics_Node(self.__iNode)
		self.__GUI		= GUI_Main(self.__iNode, self.__kNode, self.__mainApp, self.__color)

		"""Widget Names"""
		#frames
		self.__projWindow = None
		self.__ImgList	  = None

		#buttons
		self.__Import = None

		"""Variables"""
		#Wumpas = None
		self.__t = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self): #Set Renders HERE
		self.__iNode.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width, color=self.__color)

	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			self.__mainApp.destroy()

	def windowSETUP(self):
		"""#__Frame Creation & Placement__#"""
		# self.__projWindow = LabelFrame(Image_Node.Render, text='Project Window', width=1100, height=600, bg=self.__color)
		self.__ImgList	  = LabelFrame(self.__mainApp, text="Imported", width=250, height=600, bg=self.__color)

		# self.__projWindow.grid(row=0, column=1)
		self.__ImgList.grid(row=0, column=2)

		for frame in [self.__ImgList, ]:#self.__projWindow, ]:
			frame.grid_propagate(0)

		"""#__event Creation__#"""
		# self.__mainApp.bind_all(('<Button-1>'), self.__GUI.mousePosition)

		"""#__Button Creation & Placement__#"""
		self.__Import = Button(self.__mainApp, text='Import',width=32,height=2, command=lambda:self.__GUI.openFiles(self.__ImgList))

		self.__Import.grid(row=1, column=2)

		for frame in [self.__Import, ]:
		    frame.grid_propagate(0)


	def windowLoop(self):
		#closes the window
		self.close_window()

		#-----------------------#
		#more will be added soon#
		#-----------------------#


		#repeats the func after so long
		self.__mainApp.after(int(self.__tNode.get_FPS()), self.windowLoop)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp

	def get_projWindow(self):
		return self.__projWindow

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...




LVD = Alpha_LVD()
LVD.set_MainCanvas()
LVD.windowSETUP()
LVD.windowLoop()
LVD.get_mainAPP().mainloop()
print('<------------------------->')
print('<-----------END----------->')
print('<------------------------->')
