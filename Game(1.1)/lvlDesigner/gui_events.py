import re
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_statics import GUI_Statics

class GUI_Events():
	def __init__(self, iNode, cLogic, kNode, mainApp, color):
		self.__ColumnMAX = 4
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1

		#other classes
		self.__mainApp = mainApp
		self.__iNode = iNode
		self.__cLogic= cLogic
		self.__kNode = kNode
		self.__color = color

		#GUI vars
		self.__x, self.__y = 0, 0
		self.__lastRotate  = 0
		self.__CUR_widget  = None
		self.__Cur_Square  = None
		self.__isRotate  = False
		self.__isMoving  = False
		self.__isDrag 	 = False
		self.__GRID 	 = []

		#img Vars
		self.__pilIMG_LIST	= []
		self.__tkIMG_LIST	= []
		self.__placedIMG 	= []
		self.__imgKEYL		= []
		self.__imgDICT	 	= {}
		self.__IDsNUMB		= 0
		self.__newNUMB		= 0
		self.__pilIMG 		= None
		self.__tkIMG 		= None
		self.__IMG			= None

		#random var
		self.__mapFiles = 'E:\Github\Game_Repos_1\Game(1.1)\lvlDesigner\mapSaves'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game(1.1)\z_Pictures\Walls'

		self.__tempDICT = {}
		self.__tempLIST = []

		#opening a file
		self.__ID_ff = []


	"""BUTTON PRESS FUNCTIONS"""
	def fullCLear(self, ):
		for item in range(len(self.__tkIMG_LIST)):
			Image_Node.Render.delete(self.__imgDICT[self.__imgKEYL[item]].get_ID())

			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))

	def saveFILE(self, ):
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Map', filetypes=filetype, defaultextension=filetype, initialdir=self.__mapFiles)
		if file == None:
			return

		targFile = open(str(file.name), 'w')

		# self.__tempDICT = {}
		# self.__tempLIST = []
		# for key in self.__imgDICT.keys():
		# 	for item in range(len(self.__imgDICT[key].get_ID())):
		# 		ID = self.__imgDICT[key].get_ID(item, full=False)
		# 		self.__tempLIST.append(ID)
		# 		fileLocation = self.__imgDICT[key].get_fileLocation()
		# 		self.__tempDICT[fileLocation] = self.__tempLIST
		# info = str(self.__tempDICT) +'\n'
		# targFile.write(info)
		# targFile.write('\n<=======================================================>\n\n')

		self.__tempDICT = {}
		self.__tempLIST = []
		for key in self.__imgDICT.keys():
			self.__tempDICT = {}
			self.__tempLIST = []
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID = self.__imgDICT[key].get_ID(item, full=False)
				info = str(ID) +'\n'
				targFile.write(info)
		targFile.write('\n<=======================================================>\n\n')

		self.__tempDICT = {}
		self.__tempLIST = []
		for key in self.__imgDICT.keys():
			self.__tempDICT = {}
			self.__tempLIST = []
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID = self.__imgDICT[key].get_ID(item, full=False)
				fileLocation = self.__imgDICT[key].get_fileLocation()
				self.__tempDICT[ID] = fileLocation
			info = str(self.__tempDICT) +'\n'
			targFile.write(info)
		targFile.write('\n<=======================================================>\n\n')

		self.__tempDICT = {}
		self.__tempLIST = []
		for key in self.__imgDICT.keys():
			self.__tempDICT = {}
			self.__tempLIST = []
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 		= self.__imgDICT[key].get_ID(item, full=False)
				tkIMG	= self.__imgDICT[key].get_PLC_tkIMG(ID)
				self.__tempDICT[ID] = tkIMG
			info = str(self.__tempDICT) +'\n'
			targFile.write(info)
		targFile.write('\n<=======================================================>\n\n')

		self.__tempDICT = {}
		self.__tempLIST = []
		for key in self.__imgDICT.keys():
			self.__tempDICT = {}
			self.__tempLIST = []
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 		= self.__imgDICT[key].get_ID(item, full=False)
				pilIMG	= self.__imgDICT[key].get_PLC_pilIMG(ID)
				self.__tempDICT[ID] = pilIMG
			info = str(self.__tempDICT) +'\n'
			targFile.write(info)
		targFile.write('\n<=======================================================>\n\n')

		self.__tempDICT = {}
		self.__tempLIST = []
		for key in self.__imgDICT.keys():
			self.__tempDICT = {}
			self.__tempLIST = []
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 		= self.__imgDICT[key].get_ID(item, full=False)
				coords	= self.__imgDICT[key].get_PLC_Coords(ID)
				self.__tempDICT[ID] = coords
			info = str(self.__tempDICT) +'\n'
			targFile.write(info)
		targFile.write('\n<=======================================================>\n\n')

		self.__tempDICT = {}
		self.__tempLIST = []
		for key in self.__imgDICT.keys():
			self.__tempDICT = {}
			self.__tempLIST = []
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 		= self.__imgDICT[key].get_ID(item, full=False)
				corners = self.__imgDICT[key].get_PLC_Corners(ID)
				self.__tempDICT[ID] = corners
			info = str(self.__tempDICT) +'\n'
			targFile.write(info)
		targFile.write('\n<=======================================================>\n\n')

		targFile.write('***')
		targFile.close() #DON'T FORGET ABOUT THIS


	def open_lvlFIles(self, ):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == None:
			return
		print('THIS HAPPEND')
		targFile = open(file, 'r')
		tempLIST = []
		for line in targFile:
			line = line.rstrip('\n')
			# print('Original Line;', line)

			ID = re.search("(^PLC#.*)", line)
			if ID != None:
				y = ID.group(1)
				self.__ID_ff.append(y)

				
		print(self.__ID_ff)


		targFile.close()


	def open_imgFiles(self, parent):
		filetypes = (("PNG", "*.png"), ("All Files", "*.*"))
		file = filedialog.askopenfilename(title='Picture Import', filetypes=filetypes, initialdir=self.__pngFiles)
		if file == None:
			return
		newFile = re.search('.*/(.*/.*/.*$)', file)
		file = newFile.group(1)

		group_ID = 'LVL_D#00'+str(self.__IDsNUMB)
		self.__IDsNUMB += 1

		image = self.__iNode.Img_Add(file)
		self.__tkIMG_LIST.append(image[2])
		self.__pilIMG_LIST.append(image[0])
		B1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.drag_drop(group_ID))
		self.__imgKEYL.append(group_ID)
		self.__imgDICT[group_ID] = GUI_Statics(group_ID)
		self.__imgDICT[group_ID].add_IMG(tkIMG=image[2], pilIMG=image[0])
		self.__imgDICT[group_ID].Img_Info(tkIMG=image[2], pilIMG=image[0], fLocation=file)


		B1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1


	def drag_drop(self, group_ID):
		if self.__isDrag == False:
			print('ON')
			self.__isDrag   = True
			self.__IMG = self.__iNode.Img_Place(-50, -50, self.__imgDICT[group_ID].get_tkIMG(), LVD='yes')
			self.__mainApp.bind(('<Motion>'), lambda event, arg=group_ID: self.moveImg(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=group_ID: self.rotation(event, arg))
		else:
			print('OFF')
			self.__isDrag = False
			self.__pilIMG = None
			self.__tkIMG  = None
			Image_Node.Render.delete(self.__IMG)
			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))

	def rotation(self, event, group_ID):
		# print('this sucks')
		self.__lastRotate += 90
		self.__isRotate = True
		oldIMG = self.__IMG
		self.__tkIMG, self.__pilIMG = self.__iNode.Img_Rotate(self.__imgDICT[group_ID].get_pilIMG(), self.__lastRotate)
		self.__IMG = self.__iNode.Img_Place(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1], self.__tkIMG, LVD='yes')
		Image_Node.Render.delete(oldIMG)

	def moveImg(self, event, group_ID):
		# print((event.x, event.y))
		self.__isMoveing = True

		for item in range(len(self.__GRID)):
			if event.x > self.__GRID[item][0] and event.y > self.__GRID[item][1]:
				if event.x < self.__GRID[item][2] and event.y < self.__GRID[item][3]:
					self.__Cur_Square = item

		self.find_Widget()
		if self.__CUR_widget == Image_Node.Render:
			if self.__isDrag == True:
				canvID = Image_Node.Render.find_withtag(self.__IMG)[0]
				# Image_Node.Render.coords(canvID, event.x, event.y)
				Image_Node.Render.coords(canvID, self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1])
				Image_Node.Render.bind(('<Button-1>'), lambda event, arg=group_ID: self.placeImg(event, arg))
		else:
			Image_Node.Render.unbind(('<Button-1>'))
			pass

	def find_Widget(self):
		x,y = self.__mainApp.winfo_pointerxy()
		self.__CUR_widget = self.__mainApp.winfo_containing(x,y)

	def placeImg(self, event, group_ID):
		ID = 'PLC#00'+str(self.__newNUMB)
		self.__newNUMB += 1
		if self.__tkIMG != None:
			self.__tkIMG_LIST.append(self.__tkIMG)
			self.__iNode.Img_Place(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1], self.__tkIMG,
									LVD='yes', tag=[ID, group_ID])
			self.__imgDICT[group_ID].set_ID(ID)
			self.__imgDICT[group_ID].Placed_imgInfo(ID=ID,
													Corners=self.__GRID[self.__Cur_Square],
													Coords=(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1]),
													pilIMG=self.__pilIMG, tkIMG=self.__tkIMG)
			print([group_ID], ':GroupID')
			self.__imgDICT[group_ID].show_PLC_Data()
			print(self.__imgDICT[group_ID].get_ID())
		else:
			self.__tkIMG_LIST.append(self.__imgDICT[group_ID].get_tkIMG())
			self.__iNode.Img_Place(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1],
									self.__imgDICT[group_ID].get_tkIMG(), LVD='yes', tag=[ID, group_ID])
			self.__imgDICT[group_ID].set_ID(ID)
			self.__imgDICT[group_ID].Placed_imgInfo(ID=ID,
													Corners=self.__GRID[self.__Cur_Square],
													Coords=(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1]),
													pilIMG=self.__imgDICT[group_ID].get_pilIMG(), tkIMG=self.__imgDICT[group_ID].get_tkIMG())
			print([group_ID], ':GroupID')
			self.__imgDICT[group_ID].show_PLC_Data()
			print(self.__imgDICT[group_ID].get_ID())


	def deleteImg(self, event):
		x1, y1, x2, y2 = self.__GRID[self.__Cur_Square]
		img = Image_Node.Render.find_overlapping(x1, y1, x2, y2)
		if len(img) > 1 and len(img) < 3: #this is when I don't have the grid up
			Image_Node.Render.delete(img[1])
		elif len(img) > 4:
			Image_Node.Render.delete(img[len(img)-1])

	def mousePosition(self, event): #finds coords & shows them
		#(event.x, event.y) will always be mouse position
		print((event.x, event.y), 'mouse coords')

	def PASS(self):
		pass


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_gridSETUP(self, grid):
		self.__GRID = grid
