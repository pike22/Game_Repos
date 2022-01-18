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
	"""
	This is the main class that is used to run the level designer.
	Current version: v0.5.0
	"""
	BGcolor = 'Grey'
	def __init__(self, ):
		self.__Sc_Width	 = 1280
		self.__Sc_Height = 800
		self.__version	 = "Level Designer [ALPHAv0.5]"
		self.__color 	 = 'Grey'

		"""Class Call's"""
		self.__mainApp	= Tk()
		self.__cLogic	= Collision_Logic(None)
		self.__cNode	= Collision_Node(self.__cLogic)
		self.__tNode	= Timer_Node(self.__mainApp)
		self.__iNode	= Image_Node() #NOTHING TO NOTE
		self.__kNode	= Kinetics_Node(self.__iNode)
		self.__mainMenu = Menu_Main(self.__mainApp, self.__color)
		self.__GUI		= GUI_Main(self.__cLogic, self.__iNode, self.__kNode, self.__cNode, self.__mainApp, 'Grey', self.__mainMenu)

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
		"""
		Sets up the tkinter window
		"""
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width+260) + 'x' + str(self.__Sc_Height))
		self.__mainMenu.menu_setUP()

	def set_MainCanvas(self): #Set Renders HERE
		"""
		Creates The  Canvas and sets it as Render

		:meta private:
		"""
		self.__iNode.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width, color=self.__color)

	def close_window(self): #putting this on HOLD
		"""
		:meta private:
		"""
		if keyboard.is_pressed('q') == True:
			self.__mainApp.quit()

	def GUI_run(self):
		"""
		Calls other functions within the Alpha_LVD class
		"""
		self.__GUI.windowSETUP()
		self.__GUI.gridSETUP()

	def windowLoop(self):
		"""
		Creates the real time Game Loop for Alpha_LVD.

		:meta private:
		"""#if more is added, change private to public

		#closes the window
		self.close_window()

		#-----------------------#
		#more might be added soon#
		#-----------------------#


		#repeats the func after so long
		self.__mainApp.after(int(self.__tNode.get_FPS()), self.windowLoop)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		"""
		:meta private:
		"""
		return self.__mainApp

	def get_projWindow(self):
		"""
		:meta private:
		"""
		return self.__projWindow

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...




LVD = Alpha_LVD()
LVD.tk_windowSETUP()
LVD.set_MainCanvas()
print('\n')
LVD.GUI_run()
LVD.windowLoop()
LVD.get_mainAPP().mainloop()
print('\n')
print('<------------------------->')
print('<-----------END----------->')
print('<------------------------->')
