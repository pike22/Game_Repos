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
	def __init__(self, ):
		self.__Sc_Width	 = 1400
		self.__Sc_Height = 700
		self.__version	 = "Level Designer [ALPHAv0.0]"

		"""Class Call's"""
		self.__mainApp	= Tk()
		self.__GUI		= GUI_Main()
		self.__tNode	= Timer_Node(self.__mainApp)
		self.__iNode	= Image_Node()

		"""Variables"""
		#Wumpas = None
		self.__t = 0


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
		projWindow = LabelFrame(Image_Node.Render, text='Project Window', width=1100, height=600, bg='Grey')
		ImgList	   = LabelFrame(Image_Node.Render, text="Imported", width=250, height=600, bg='Grey')

		#Frame Placement
		# self.__GUI.Place_Frame(placeHold, 0, 0)
		projWindow.grid(row=0, column=1)
		ImgList.grid(row=0, column=2)

		for frame in [projWindow, ImgList, ]:
			frame.grid_propagate(0)

		#Button Creation
		Import = Button(Image_Node.Render, text='Import',width=32,height=2, command=lambda:self.__GUI.openFiles(ImgList))

		#Button Placement
		Import.grid(row=1, column=2)

		for frame in [Import, ]:
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


LVD = Alpha_LVD()
LVD.set_MainCanvas()
LVD.windowSETUP()
LVD.windowLoop()
LVD.get_mainAPP().mainloop()
print('<------------------------->')
print('<-----------END----------->')
print('<------------------------->')
