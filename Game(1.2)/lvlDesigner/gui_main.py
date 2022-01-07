from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_events import GUI_Events
from .si_files import SI_Files
from .menu_main import Menu_Main


class GUI_Main():
	def __init__(self, cLogic, iNode, kNode, cNode, mainApp, color, mainMenu):
		self.__Key = 32
		self.__iNode  = iNode
		self.__kNode  = kNode
		self.__cNode  = cNode
		self.__cLogic = cLogic
		self.__mainApp= mainApp
		self.__mainMenu=mainMenu
		self.__color  = color
		self.__eGUI	  = GUI_Events(iNode, cLogic, kNode, mainApp, color, self.__Key)
		self.__siFILES= SI_Files(iNode, mainApp, color, self.__eGUI, self.__Key)

		self.__mainMenu.set_eGUI(self.__eGUI)
		self.__mainMenu.set_siFILES(self.__siFILES)

		#Frame Vars
		self.__ImgList= None

		self.__DefultButtons = 'E:\Github\Game_Repos_1\Game(1.2)\lvlDesigner\ButtonLoadOut\Test1.txt'
		#Button Vars
		self.__Import = None
		self.__delKEY = None
		self.__FindIMG = None
		self.__saveFILE = None
		self.__saveLoadO = None
		self.__lvlImport = None
		self.__CCollision = None

		#Grid Mapping
		self.__x, self.__y = 0, 0
		self.__linex, self.__liney = 0, 0
		self.__PLCcorner = [] #(x1, y1, x2, y2) this represents one square of the grid
		self.__PLCcoord  = [] #(x, y) this is for grid coords, may be more helpfull

	def windowSETUP(self):


		"""#__Frame Creation & Placement__#"""
		self.__ImgList = LabelFrame(self.__mainApp, text="Imported", width=250, height=500, bg=self.__color)

		self.__ImgList.grid(row=0, column=2, columnspan=10)

		for frame in [self.__ImgList, ]:
			frame.grid_propagate(0)

		self.__siFILES.set_imgFrame(self.__ImgList)

		"""#__Buttons from load__#"""
		self.__siFILES.open_ImgButtons(self.__DefultButtons)

		"""#__event Calls__#"""
		# self.__mainApp.bind_all(('<Button-1>'), self.__eGUI.mousePosition)
		self.__mainApp.bind_all(('<Button-3>'), self.__eGUI.Del_Image)

		"""#__Button Creation & Placement__#"""
		self.__saveLoadO = Button(self.__mainApp, text='Save Buttons', width=16, height=2, command=lambda:self.__siFILES.save_ImgButtons(self.__eGUI.get_buttonDICT()))
		self.__openLoadO = Button(self.__mainApp, text='Button Set', width=16, height=2, command=self.__siFILES.changeLoadout)
		self.__lvlImport = Button(self.__mainApp, text='Import LVL', width=16, height=2, command=self.__siFILES.Read_File)
		self.__saveFILE = Button(self.__mainApp, text='Save', width=16, height=2,
											   command=lambda:self.__siFILES.saveFILE(self.__eGUI.get_imgDICT()))
		self.__delFILE = Button(self.__mainApp, text='Delete File', width=16, height=2, command=self.__eGUI.Del_File)
		self.__delKEY = Button(self.__mainApp, text='Map Wipe', width=16, height=2, command=self.__eGUI.Map_Wipe)
		self.__Import = Button(self.__mainApp, text='Import Image', width=16, height=2,
											   command=lambda:self.__eGUI.open_imgFiles(self.__ImgList))
		self.__FindIMG= Button(self.__mainApp, text='Find IMG', width=16, height=2, command=self.__eGUI.FindIMG_Button)

		self.__Import.grid(row=1, column=2)
		self.__delKEY.grid(row=2, column=3)
		self.__delFILE.grid(row=3, column=2)
		self.__FindIMG.grid(row=3, column=3)
		# self.__saveFILE.grid(row=1, column=3)
		self.__saveLoadO.grid(row=4, column=2)
		self.__openLoadO.grid(row=4, column=3)
		# self.__lvlImport.grid(row=2, column=2)

		for frame in [self.__Import, self.__delKEY, self.__saveFILE, self.__lvlImport]:
		    frame.grid_propagate(0)

	def gridSETUP(self):
		segment_x = int(1280/32)
		segment_y = int(800/32)
		for item in range(segment_x+1):
			# lineID = Image_Node.Render.create_line(self.__linex, 0, self.__linex, 800, tag='G#line')
			self.__linex += self.__Key
		for item in range(segment_y+1):
			# lineID = Image_Node.Render.create_line(0, self.__liney, 1280, self.__liney, tag='G#line')
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
				self.__PLCcorner.append((self.__x, self.__y, self.__x+self.__Key, self.__y+self.__Key))
				self.__PLCcoord.append((self.__x, self.__y))
		# print('Corners for placement\n', self.__PLCcorner)
		# print('Coords for placement\n', self.__PLCcoord)
		self.__eGUI.set_gridSETUP(self.__PLCcorner, self.__PLCcoord)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_PLCcorner(self, item=None):
		if item == None:
			return self.__PLCcorner
		else:
			return self.__PLCcorner[item]

	def get_PLCcoord(self, item=None):
		if item == None:
			return self.__PLCcoord
		else:
			return self.__PLCcoord[item]

	def get_eGUI(self):
		return self.__eGUI

	def get_siFILE(self):
		return self.__siFILES


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_frame
