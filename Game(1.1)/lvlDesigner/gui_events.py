import re
import os
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_statics import GUI_Statics

class GUI_Events():
	def __init__(self, iNode, cLogic, kNode, mainApp, color, key):
		self.__ColumnMAX = 4
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1
		self.__Key 	  = key

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
		self.__CCollision  =False
		self.__isRotate  = False
		self.__isMoving  = False
		self.__isDrag 	 = False
		self.__GRID 	 = []

		self.__mapFiles = 'E:\Github\Game_Repos_1\Game(1.1)\lvlDesigner\mapSaves'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game(1.1)\z_Pictures\Walls'

		#img Vars
		self.__placedIMG_tag = []
		self.__pilIMG_LIST	= []
		self.__tkIMG_LIST	= []
		self.__imgKEYL		= []
		self.__imgDICT	 	= {}
		self.__IDsNUMB		= 0
		self.__newNUMB		= 0
		self.__pilIMG 		= None
		self.__tkIMG 		= None
		self.__IMG			= None

		#RAND VARS
		self.__topCorner = None
		self.__botCorner = None
		self.__timeP = 0


	def buttonFromSave(self, fileLoc, parent, button_ID, MG=None):
		image = self.__iNode.Img_Add(fileLoc)
		self.__tkIMG_LIST.append(image[2])
		self.__pilIMG_LIST.append(image[0])
		if MG == None:
			B1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.drag_drop(button_ID))
		self.__imgKEYL.append(button_ID)
		self.__imgDICT[button_ID] = GUI_Statics(button_ID)
		self.__imgDICT[button_ID].add_IMG(tkIMG=image[2], pilIMG=image[0])
		self.__imgDICT[button_ID].Img_Info(tkIMG=image[2], pilIMG=image[0], fLocation=fileLoc)
		self.__imgDICT[button_ID].set_Size(image[1])
		fileLoc = re.search(".*/.*/(.*$)", self.__imgDICT[button_ID].get_fileLocation())
		if fileLoc != None:
			name = fileLoc.group(1)
			if name == 'floor.png':
				self.__imgDICT[button_ID].set_PLC_Collision(False)
				self.__imgDICT[button_ID].set_group_ID('#floor')

		if MG == None:
			B1.grid(row=self.__Row, column=self.__Column)
			if self.__Column <= self.__ColumnMAX:
				self.__Column += 1
			else:
				self.__Column = 0
				self.__Row	  +=1

		return self.__imgDICT

	def open_imgFiles(self, parent):
		filetypes = (("PNG", "*.png"), ("All Files", "*.*"))
		file = filedialog.askopenfilename(title='Picture Import', filetypes=filetypes, initialdir=self.__pngFiles)
		if file == '':
			print('No File Selected')
		newFile = re.search('.*/(.*/.*/.*$)', file)
		if newFile != None:
			file = newFile.group(1)
		else:
			return

		if self.__IDsNUMB <= 9:
			button_ID = 'LVL_D#00'+str(self.__IDsNUMB)
		elif self.__newNUMB > 9 and self.__IDsNUMB <= 99:
			button_ID = 'LVL_D#0'+str(self.__IDsNUMB)
		else:
			button_ID = 'LVL_D#'+str(self.__IDsNUMB)
		self.__IDsNUMB += 1

		image = self.__iNode.Img_Add(file)
		self.__tkIMG_LIST.append(image[2])
		self.__pilIMG_LIST.append(image[0])
		B1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.drag_drop(button_ID))
		self.__imgKEYL.append(button_ID)
		# if button_ID in self.__imgDICT.keys():
		# 	g_ID = re.search("LVL_D#(.{3})", button_ID)
		# 	if g_ID != None:
		# 		print(g_ID.group(1))
		self.__imgDICT[button_ID] = GUI_Statics(button_ID)
		self.__imgDICT[button_ID].add_IMG(tkIMG=image[2], pilIMG=image[0])
		self.__imgDICT[button_ID].Img_Info(tkIMG=image[2], pilIMG=image[0], fLocation=file)
		self.__imgDICT[button_ID].set_Size(image[1])
		fileLoc = re.search("=.*/.*/(.*$)", self.__imgDICT[button_ID].get_fileLocation())
		if fileLoc != None:
			name = fileLoc.group(1)
			if name == 'floor.png':
				self.__imgDICT[button_ID].set_PLC_Collision(False)
				self.__imgDICT[button_ID].set_group_ID('#floor')



		B1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1


	def drag_drop(self, button_ID):
		if self.__isDrag == False:
			print('ON')
			self.__isDrag   = True
			self.__IMG = self.__iNode.Img_Place(-50, -50, self.__imgDICT[button_ID].get_tkIMG(), LVD='yes')
			self.__mainApp.bind(('<Motion>'), lambda event, arg=button_ID: self.moveImg(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=button_ID: self.rotation(event, arg))
		else:
			print('OFF')
			self.__lastRotate = 0
			self.__isRotate = False
			self.__isDrag = False
			self.__pilIMG = None
			self.__tkIMG  = None
			Image_Node.Render.delete(self.__IMG)
			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))

	def rotation(self, event, button_ID):
		# print('this sucks')
		self.__lastRotate += 90
		self.__isRotate = True
		oldIMG = self.__IMG
		self.__tkIMG, self.__pilIMG = self.__iNode.Img_Rotate(self.__imgDICT[button_ID].get_pilIMG(), self.__lastRotate)
		self.__IMG = self.__iNode.Img_Place(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1], self.__tkIMG, LVD='yes')
		Image_Node.Render.delete(oldIMG)

	def moveImg(self, event, button_ID):
		# print((event.x, event.y))
		self.__isMoveing = True

		#this is staple for when I need to know what square my mouse is in.
		self.Curent_Square(event)

		self.find_Widget()
		if self.__CUR_widget == Image_Node.Render:
			if self.__isDrag == True:
				canvID = Image_Node.Render.find_withtag(self.__IMG)[0]
				# Image_Node.Render.coords(canvID, event.x, event.y)
				Image_Node.Render.coords(canvID, self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1])
				Image_Node.Render.bind(('<Button-1>'), lambda event, arg=button_ID: self.placeImg(event, arg))
		else:
			Image_Node.Render.unbind(('<Button-1>'))
			pass

	def find_Widget(self):
		x,y = self.__mainApp.winfo_pointerxy()
		self.__CUR_widget = self.__mainApp.winfo_containing(x,y)

	def placeImg(self, event, button_ID):
		if self.__newNUMB <= 9:
			ID = 'PLC#00'+str(self.__newNUMB)
		elif self.__newNUMB > 9 and self.__newNUMB <= 99:
			ID = 'PLC#0'+str(self.__newNUMB)
		else:
			ID = 'PLC#'+str(self.__newNUMB)
		self.__newNUMB += 1

		self.__placedIMG_tag.append(ID)
		self.imgINFO(button_ID=button_ID, ID=ID, rotation=self.__lastRotate, isRotate=self.__isRotate, tkIMG=self.__tkIMG)


		# print(button_ID, ':GroupID')
		# self.__imgDICT[button_ID].show_PLC_Data()
		# print('ids', self.__imgDICT[button_ID].get_ID())


	def fullCLear(self):
		item = len(self.__placedIMG_tag)-1
		while self.__placedIMG_tag != []:
			item -= 1
			if item == 0:
				item = len(self.__placedIMG_tag)-1
			ID = Image_Node.Render.find_withtag(self.__placedIMG_tag[item])
			if ID != ():
				for key in self.__imgDICT.keys():
					keyID = self.__imgDICT[key].get_ID(full=True)
					if keyID != []:
						if self.__placedIMG_tag[item] == self.__imgDICT[key].get_ID(len(keyID)-1, full=False):
							self.__imgDICT[key].del_Placed(self.__placedIMG_tag[item])
							Image_Node.Render.delete(ID)
							del self.__placedIMG_tag[item]
					else:
						pass



	def deleteImg(self, event):
		# print('Delete?') #This is so I know it is at least working
		#incase of imeadiate delete
		#this is staple for when I need to know what square my mouse is in.
		self.Curent_Square(event)

		x1, y1, x2, y2 = self.__GRID[self.__Cur_Square]
		Canvas_ID = Image_Node.Render.find_overlapping(x1, y1, x2, y2)
		ID = None
		saveForDel = None
		for item in range(len(self.__placedIMG_tag)-1, -1, -1):
			ID = Image_Node.Render.find_withtag(self.__placedIMG_tag[item])
			if ID != ():
				if self.__isDrag == False and len(Canvas_ID) > 4:
					if ID[0] == Canvas_ID[4]:
						for keys in self.__imgDICT.keys():
							keysTag = self.__imgDICT[keys].get_ID()
							for myTag in range(len(keysTag)-1, -1, -1):
								if self.__placedIMG_tag[item] == keysTag[myTag]:
									self.__imgDICT[keys].del_Placed(keysTag[myTag])
									Image_Node.Render.delete(ID)
									del self.__placedIMG_tag[item]
									return

				elif len(Canvas_ID) >= 1:
					ID = Image_Node.Render.find_withtag(self.__placedIMG_tag[item])
					if ID == Canvas_ID:
						for keys in self.__imgDICT.keys():
							keysTag = self.__imgDICT[keys].get_ID()
							for myTag in range(len(keysTag)-1, -1, -1):
								if self.__placedIMG_tag[item] == keysTag[myTag]:
									self.__imgDICT[keys].del_Placed(keysTag[myTag])
									Image_Node.Render.delete(ID)
									del self.__placedIMG_tag[item]
									return
	def del_file(self):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Select to Be Deleted', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == '':
			print('No File Selected')
			return
		os.remove(file)
		print('file Removed')

	def mousePosition(self, event): #finds coords & shows them
		#(event.x, event.y) will always be mouse position
		print((event.x, event.y), 'mouse coords')

	def PASS(self):
		pass


	"""THESE ARE THE SIMPLIFY FUNCTIONS"""
	def Curent_Square(self, event):
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__GRID)):
			if event.x > self.__GRID[item][0] and event.y > self.__GRID[item][1]:
				if event.x < self.__GRID[item][2] and event.y < self.__GRID[item][3]:
					self.__Cur_Square = item

	def imgINFO(self, button_ID, ID, Corner=None, Coord=None, rotation=None, Collision=True, tkIMG=None, isRotate=False, fileREAD=None):
		if tkIMG != None:
			if fileREAD != None:
				self.__tkIMG_LIST.append(tkIMG)
				x, y = fileREAD
				self.__iNode.Img_Place(x, y, tkIMG, LVD='yes', tag=[ID, str(self.__imgDICT[button_ID].get_group_ID())])
				self.__imgDICT[button_ID].set_ID(ID)
				if isRotate == True:
					self.__imgDICT[button_ID].Placed_imgInfo(ID=ID, Corners=Corner, Coords=Coord, rotation=rotation)
				else:
					self.__imgDICT[button_ID].Placed_imgInfo(ID=ID, Corners=Corner, Coords=Coord, rotation=None)

			else:
				self.__tkIMG_LIST.append(tkIMG)
				self.__iNode.Img_Place(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1], tkIMG, LVD='yes', tag=[ID, str(self.__imgDICT[button_ID].get_group_ID())])
				self.__imgDICT[button_ID].set_ID(ID)
				if isRotate == True:
					self.__imgDICT[button_ID].Placed_imgInfo(ID=ID,	Corners=self.__GRID[self.__Cur_Square], Coords=(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1]), rotation=self.__lastRotate)
				else:
					self.__imgDICT[button_ID].Placed_imgInfo(ID=ID,	Corners=self.__GRID[self.__Cur_Square], Coords=(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1]), rotation=None)
		else:
			self.__tkIMG_LIST.append(self.__imgDICT[button_ID].get_tkIMG())
			self.__iNode.Img_Place(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1], self.__imgDICT[button_ID].get_tkIMG(), LVD='yes', tag=[ID, str(self.__imgDICT[button_ID].get_group_ID())])
			self.__imgDICT[button_ID].set_ID(ID)
			self.__placedIMG_tag.append(ID)
			if isRotate == True:
				self.__imgDICT[button_ID].Placed_imgInfo(ID=ID,	Corners=self.__GRID[self.__Cur_Square], Coords=(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1]), rotation=self.__lastRotate)
			else:
				self.__imgDICT[button_ID].Placed_imgInfo(ID=ID,	Corners=self.__GRID[self.__Cur_Square], Coords=(self.__GRID[self.__Cur_Square][0], self.__GRID[self.__Cur_Square][1]), rotation=None)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imgDICT(self):
		return self.__imgDICT


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_gridSETUP(self, grid):
		self.__GRID = grid

	def set_Images(self, imgDict, newNUMB, IDsNUMB, placedList):
		self.__placedIMG_tag = placedList
		self.__imgDICT = imgDict
		self.__newNUMB = newNUMB
		self.__IDsNUMB = IDsNUMB
