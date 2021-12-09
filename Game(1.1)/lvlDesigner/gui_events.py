import re
import os
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .button_main import Button_Main
from .plc_imgmain import PLC_ImgMain

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
		self.__lastRotate  = 0
		self.__CUR_widget  = None
		self.__Cur_Square  = None
		self.__CCollision  = False
		self.__isRotate  = False
		self.__isMoving  = False
		self.__isDrag 	 = False
		self.__COORD 	 = []
		self.__GRID 	 = []

		self.__mapFiles = 'E:\Github\Game_Repos_1\Game(1.1)\lvlDesigner\mapSaves'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game(1.1)\z_Pictures\Walls'

		'''#_IMAGE VARIABLES_#'''
		#Button Vars
		self.__buttonDICT= {}
		self.__bID_count = 0

		#PLC_images
		self.__PLCI_Tags = [] #Organizational reasons
		self.__PLCI_Tk	 = [] #so tkinter doesn't start forgeting images
		self.__CurIMG	 = None
		self.__ID_count	 = 0


		#RAND VARS
		self.__timeP = 0


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

		#Create Buttons Name
		if self.__bID_count <= 9:
			button_ID = 'LVD#B00'+str(self.__bID_count)
		elif self.__bID_count > 9 and self.__bID_count <= 99:
			button_ID = 'LVL_D#0'+str(self.__bID_count)
		elif self.__bID_count > 99 and self.__bID_count <= 999:
			button_ID = 'LVL_D#'+str(self.__bID_count)
		else:
			print('ERROR: To Manny Buttons')
		self.__bID_count += 1

		#Create Button
		image = self.__iNode.Img_Add(file)
		B = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.Drag_Drop(button_ID))
		self.__buttonDICT[button_ID] = Button_Main(button_ID)
		self.__buttonDICT[button_ID].Image_Info(fileLoc=file, tkIMG=image[2], pilIMG=image[0], size=image[1])

		#Place Button
		B.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1

	def Drag_Drop(self, button_ID):
		if self.__isDrag == False:
			print("!#_ON_#!")
			self.__isDrag = True
			self.__CurIMG = self.__iNode.Img_Place(-50000, -50000, self.__buttonDICT[button_ID].get_tkIMG(), LVD='yes')
			self.__mainApp.bind(('<Motion>'), lambda event, arg=button_ID: self.moveImg(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=button_ID: self.rotation(event, arg))
		else:
			print('!#_OFF_#!')
			self.__isDrag = False
			self.__isRotate = False
			self.__lastRotate = 0
			Image_Node.Render.delete(self.__IMG)
			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))


	def Rotate(self, event, button_ID):
		self.__lastRotate += 90
		self.__isRotate = True
		oldIMG = self.__CurIMG
		tkIMG = self.__iNode.Img_Rotate(self.__imgDICT[button_ID].get_pilIMG(), self.__lastRotate)
		x, y = self.__COORD[self.__Cur_Square]
		self.__CurIMG = self.__iNode.Img_Place(x, y, tkIMG, LVD='yes')
		Image_Node.Render.delete(oldIMG)

	def Move_Image(self, event, button_ID):
		self.__isMoving = True
		self.Find_Square(event)
		self.Find_Widget()

		if self.__CUR_widget == Image_Node.Render:
			if self.__isDrag == True:
				canvID = Image_Node.Render.find_withtag(self.__CurIMG)[0]
				x, y = self.__COORD[self.__Cur_Square]
				Image_Node.Render.coords(canvID, x, y)
				Image_Node.Render.bind(('<Button-1>'), lambda event, arg=button_ID: self.placeImg(event, arg))

	def Place_Image(self, event, button_ID):
		if self.__ID_count <= 9:
			ID = 'PLCW#00'+str(self.__ID_count)
		elif self.__ID_count > 9 and self.__ID_count <= 99:
			ID = 'PLCW#0'+str(self.__ID_count)
		elif self.__ID_count > 99 and self.__ID_count <= 999:
			ID = 'PLCW#'+str(self.__ID_count)
		else: #add more elif's above if needed
			print('ERROR: To Manny Walls')
		self.__ID_count += 1

		self.Find_Square(event)
		x, y = self.__COORD[self.__Cur_Square]

		self.__PLCI_Tags.append(ID)
		self.__imgDICT[ID] = PLC_ImgMain()
		self.__imgDICT[ID].Image_Info(self.__buttonDICT[button_ID].get_fileLoc(),
									  self.__buttonDICT[button_ID].get_Size(),
									  (x, y), self.__lastRotate)
		self.__iNode.Img_Place(x, y, )
		if no=:
			print(yes)

	def Map_Wipe(self):
		pass

	def Del_Image(self, event):
		pass

	def Del_File(self):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Select to Be Deleted', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == '':
			print('No File Selected')
			return
		os.remove(file)
		print('file Removed')

	def PASS(self):
		pass

	def Find_Widget(self):
		x, y = self.__mainApp.winfo_pointerxy()
		self.__CUR_widget = self.__mainApp.winfo_containing(x, y)

	def Find_Square(self, event):
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__GRID)):
			if event.x > self.__GRID[item][0] and event.y > self.__GRID[item][1]:
				if event.x < self.__GRID[item][2] and event.y < self.__GRID[item][3]:
					self.__Cur_Square = item

	def needNew_Name(self, ): #this was imgINFO from OLDgui_events.py
		pass


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_gridSETUP(self, grid, coord):
		self.__COORD = coord
		self.__GRID = grid

	def set_Images(self, imgDict, newNUMB, IDsNUMB, placedList): #SUBJECT TO CHANGE
		self.__placedIMG_tag = placedList
		self.__imgDICT = imgDict
		self.__newNUMB = newNUMB
		self.__IDsNUMB = IDsNUMB
