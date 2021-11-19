#imports
from PIL import ImageTk, Image
# from alpha import Alpha
from lvlDesigner import *
from z_Pictures import *
from colored import fg
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *
import keyboard

class Alpha_LVD():
	def __init__(self, ):
		self.__Sc_Width	 = 1400
		self.__Sc_Height = 700
		self.__version	 = "Level Designer [ALPHAv0.0]"

		"""Class Call's"""
		self.__mainApp	= Tk()
		self.__GUI		= GUI_Main(self.__mainApp)
		self.__tNode	= Timer_Node(self.__mainApp)
		self.__iNode	= Image_Node()

		"""Variables"""
		self.__frameList = []


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self): #Set Renders HERE
		self.__iNode.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width, color='Grey')

	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			self.__mainApp.destroy()

	def windowSETUP(self):
		#Frame Creation
		# placeHold= self.__GUI.Create_Frame(width=50, height=700, parent=Image_Node.Render, bg='Black')
		projWindow = self.__GUI.Create_Frame("Project Window", width=1000, height=700, parent=Image_Node.Render, bg='Grey')
		ImgList	   = self.__GUI.Create_Frame("Imported", width=300, height=700, parent=Image_Node.Render, bg='Grey')

		#Frame Placement
		# self.__GUI.Place_Frame(placeHold, 0, 0)
		self.__GUI.Place_Frame(projWindow, 0, 1)
		self.__GUI.Place_Frame(ImgList, 0, 2)

		#Button Creation
		newfile = self.__GUI.Create_Button("Import", width=4, height=4, parent=ImgList, command=self.__GUI.openFiles())
		testing = self.__GUI.Create_Button("Import", width=4, height=4, parent=ImgList)

		#Button Placement
		self.__GUI.Place_Button(newfile, 0, 0)
		self.__GUI.Place_Button(testing, 0, 1)



	def windowLoop(self):
		#closes the window
		self.close_window()

		#-----------------------#
		#more will be added soon#
		#-----------------------#

		#repeats the func after so long
		self.__mainApp.after(int(self.__tNode.get_FPS()), self.windowLoop)
		print('<------------------------->')


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp


LVD = Alpha_LVD()
LVD.set_MainCanvas()
LVD.windowSETUP()
LVD.windowLoop()
LVD.get_mainAPP().mainloop()
print('<------------------------->')
print('<-----------END----------->')
print('<------------------------->')
