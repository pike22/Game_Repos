from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_events import GUI_Events


class GUI_Main():
	def __init__(self, iNode, cLogic, kNode, mainApp, color):
		self.__iNode  = iNode
		self.__kNode  = kNode
		self.__cLogic = cLogic
		self.__mainApp= mainApp
		self.__color  = color
		self.__eGUI	  = GUI_Events(iNode, cLogic, kNode, mainApp, color)

		#Frame Vars
		self.__ImgList= None

		#Button Vars
		self.__Import = None
		self.__delKEY = None
		self.__saveFILE = None
		self.__lvlImport = None

		#Grid Mapping
		self.__Key = 32
		self.__x, self.__y = 0, 0
		self.__linex, self.__liney = 0, 0
		self.__placeABLE = [] #(x1, y1, x2, y2) this represents one square of the grid

	def windowSETUP(self):
		"""#__Frame Creation & Placement__#"""
		self.__ImgList = LabelFrame(self.__mainApp, text="Imported", width=250, height=600, bg=self.__color)

		self.__ImgList.grid(row=0, column=2, columnspan=10)

		for frame in [self.__ImgList, ]:
			frame.grid_propagate(0)

		"""#__event Calls__#"""
		# self.__mainApp.bind_all(('<Button-1>'), self.__eGUI.mousePosition)
		self.__mainApp.bind_all(('<Button-3>'), self.__eGUI.deleteImg)

		"""#__Button Creation & Placement__#"""
		self.__lvlImport = Button(self.__mainApp, text='Import LVL', width=16, height=2, command=self.__eGUI.open_lvlFIles)
		self.__saveFILE = Button(self.__mainApp, text='Save', width=16, height=2, command=self.__eGUI.saveFILE)
		self.__delKEY = Button(self.__mainApp, text='Map Wipe', width=16, height=2, command=self.__eGUI.fullCLear)
		self.__Import = Button(self.__mainApp, text='Import Image', width=16, height=2,
											   command=lambda:self.__eGUI.open_imgFiles(self.__ImgList))

		self.__Import.grid(row=1, column=2)
		self.__delKEY.grid(row=2, column=3)
		self.__saveFILE.grid(row=1, column=3)
		self.__lvlImport.grid(row=2, column=2)

		for frame in [self.__Import, self.__delKEY, self.__saveFILE, self.__lvlImport]:
		    frame.grid_propagate(0)

	def gridSETUP(self):
		segment_x = int(1400/32)
		segment_y = int(700/32)
		for item in range(segment_x+1):
			lineID = Image_Node.Render.create_line(self.__linex, 0, self.__linex, 700)
			self.__linex += self.__Key
		for item in range(segment_y+1):
			lineID = Image_Node.Render.create_line(0, self.__liney, 1400, self.__liney)
			self.__liney += self.__Key

		for xPos in range(segment_x+1):
			if xPos == 0:
				self.__x = 0
			else:
				self.__x += self.__Key
			for yPos in range(segment_y+1):
				self.__y += self.__Key
				if yPos == (segment_y):
					self.__y = 0
				#						(x1=    x, y1=    y, x2=    x+self.__Key, y2=    y+self.__Key)
				self.__placeABLE.append((self.__x, self.__y, self.__x+self.__Key, self.__y+self.__Key))
		# print('Corners for placement\n', self.__placeABLE)
		self.__eGUI.set_gridSETUP(self.__placeABLE)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_placeABLE(self, item=None):
		if item == None:
			return self.__placeABLE
		else:
			return self.__placeABLE[item]


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_frame
