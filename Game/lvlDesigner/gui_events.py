import re
import os
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .button_main import Button_Main
from .plc_imgmain import PLC_ImgMain

class GUI_Events():
	"""
	Most events that happen within the Level Designer are housed here.

	Methods
	-------
	init(iNode, cLogic, kNode, mainApp, color, key)
		What is required when GUI_Events() is called
	"""
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
		self.__isIMG	 = False
		self.__COORD 	 = []
		self.__GRID 	 = []

		self.__mapFiles = 'E:\Github\Game_Repos_1\Game\lvlDesigner\mapSaves'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game\z_Pictures\Walls'

		'''#_IMAGE VARIABLES_#'''
		#Button Vars
		self.__buttonDICT= {}
		self.__bID_count = 0

		#PLC_images
		self.__PLCI_Tag = [] #Organizational reasons
		self.__PLCI_Tk	= [] #so tkinter doesn't start forgeting images
		self.__imgDICT	= {}
		self.__CurIMG	= None
		self.__tkIMG	= None
		self.__ID_count	= 0


		#RAND VARS


	def open_imgFiles(self, parent):
		"""
		This opens a file dialog window and askes for an image file. Then saves that image file to an instance of the Button_Main class
		as well as the button_ID that is created at the same time. The button that is created through this process is now ready to be
		used for creating levels.

		Parameters
		----------
		parent
			This is the tkinter widget that the button will be placed on.

		Attributes
		----------
		filetypes
			The type of file that is going to be requested.
		file/newFile
			The seleced file.
		button_ID : str
			The tag that will be associated with the button.
		newWidget
			tkinters ID for the button created.

		Methods
		-------
		Drag_Drop(button_ID)
			the function called when the button is pressed
		"""
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
			button_ID = 'LVD#B0'+str(self.__bID_count)
		elif self.__bID_count > 99 and self.__bID_count <= 999:
			button_ID = 'LVD#B'+str(self.__bID_count)
		else:
			print('ERROR: To Manny Buttons')
		self.__bID_count += 1
		print(button_ID)

		#Create Button
		image = self.__iNode.Img_Add(file)
		newWidget = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.Drag_Drop(button_ID))
		self.__buttonDICT[button_ID] = Button_Main(button_ID, newWidget)
		self.__buttonDICT[button_ID].Image_Info(fileLoc=file, tkIMG=image[2], pilIMG=image[0], size=image[1])

		#Place Button
		newWidget.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1

	def Drag_Drop(self, button_ID):
		"""
		When flipped on, a image will be created on the mouse position. The image then will be able to be moved around and rotated.
		Before the mouse is clicked.

		Parameters
		----------
		button_ID
			specified button to find the associated info.

		Methods
		-------
		Move_Image(event, button_ID)
			Allows the image to be moved.
		Rotate_Image(event, button_ID)
			Allows the image to be rotated.
		"""
		if self.__isDrag == False:
			print("!#_ON_#!")
			self.__isDrag = True
			self.__CurIMG = self.__iNode.Img_Place(-50, -50, image=self.__buttonDICT[button_ID].get_tkIMG(), LVD='yes')
			self.__mainApp.bind(('<Motion>'), lambda event, arg=button_ID: self.Move_Image(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=button_ID: self.Rotate_Image(event, arg))
		else:
			print('!#_OFF_#!')
			self.__isDrag = False
			self.__isRotate = False
			self.__lastRotate = 0
			self.__tkIMG	= None
			Image_Node.Render.delete(self.__CurIMG)
			self.__mainApp.unbind(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))
			Image_Node.Render.unbind(('<Button-1>'))


	def Rotate_Image(self, event, button_ID):
		"""
		This rotates the image that is currently following the mouse before it would be placed.

		Attributes
		----------
		oldIMG
			A coppy of the Current image before it is manipulated.
		x, y : int
			The x, y coord for where the image is currently.
		"""
		self.__lastRotate += 90
		if self.__lastRotate == 360:
			self.__lastRotate = 0
		self.__isRotate = True
		oldIMG = self.__CurIMG
		self.__tkIMG = self.__iNode.Img_Rotate(self.__buttonDICT[button_ID].get_pilIMG(), self.__lastRotate)
		x, y = self.__COORD[self.__Cur_Square]
		self.__CurIMG = self.__iNode.Img_Place(x, y, self.__tkIMG, LVD='yes')
		Image_Node.Render.delete(oldIMG)

	def Move_Image(self, event, button_ID):
		"""
		This allows the image to follow the mouse position.

		Attributes
		----------
		canvID
			tkinters ID for the image.
		x, y : int
			The x, y coord for where the image is currently.

		Methods
		-------
		Place_Image(event, button_ID)
			Used to place the image.
		Find_Square(event)
			Used to find the square the mouse is in.
		Find_Widget()
			Used to find the widget the mouse is in.
		"""
		self.__isMoving = True
		self.Find_Square(event)
		self.Find_Widget()

		if self.__CUR_widget == Image_Node.Render:
			if self.__isDrag == True:
				canvID = Image_Node.Render.find_withtag(self.__CurIMG)[0]
				x, y = self.__COORD[self.__Cur_Square]
				Image_Node.Render.coords(canvID, x, y)
				Image_Node.Render.bind(('<Button-1>'), lambda event, arg=button_ID: self.Place_Image(event, arg))

	def Place_Image(self, event, button_ID):
		"""
		Places the image that would be following the mouse.

		Attributes
		----------
		ID : str
			The tag associated with the image that was placed.

		Methods
		-------
		PLC_ImgMain(ID, button_ID)
			An instance of this class is created for the image that was just placed.
		Image_Info(fileLoc, Size, Coords, Rotation)
			The file side of the image is saved here.
		Img_Place(x, y, tkIMG, LVD, tag)
			The image is actually placed using iNode.
		"""
		self.Del_Image(event)
		if self.__ID_count <= 9:
			ID = 'LVD#W000'+str(self.__ID_count)
		elif self.__ID_count > 9 and self.__ID_count <= 99:
			ID = 'LVD#W00'+str(self.__ID_count)
		elif self.__ID_count > 99 and self.__ID_count <= 999:
			ID = 'LVD#W0'+str(self.__ID_count)
		elif self.__ID_count > 999 and self.__ID_count <= 9999:
			ID = 'LVD#W'+str(self.__ID_count)
		else: #add more elif's above if needed
			print('ERROR: To Manny Walls')
		self.__ID_count += 1

		self.Find_Square(event)
		x, y = self.__COORD[self.__Cur_Square]

		self.__PLCI_Tag.append(ID)
		self.__PLCI_Tk.append(self.__tkIMG)
		self.__imgDICT[ID] = PLC_ImgMain(ID, button_ID)
		self.__imgDICT[ID].Image_Info(self.__buttonDICT[button_ID].get_fileLoc(),
									  self.__buttonDICT[button_ID].get_Size(),
									  (x, y), self.__lastRotate)
		if self.__tkIMG == None:
			self.__tkIMG = self.__buttonDICT[button_ID].get_tkIMG()

		self.__iNode.Img_Place(x, y, self.__tkIMG, LVD='yes', tag=[ID, self.__imgDICT[ID].get_group_ID()])

	def FindIMG_Button(self):
		"""
		Used to find the ID of the image the mouse is over.

		Methods
		-------
		Find_imgTag(event)
			actually finds the images tag

		:meta private:
		"""
		if self.__isIMG == False:
			print("!#_ON_#!")
			self.__isIMG = True
			self.__mainApp.bind_all("((<Button-1>))", self.Find_imgTag)
		else:
			print('!#_OFF_#!')
			self.__isIMG = False
			self.__mainApp.unbind_all("((<Button-1>))")

	def Find_imgTag(self, event):
		"""
		Finds the tag of the image that the mouse is hovering over.

		:meta private:
		"""
		self.Find_Square(event)

		x1, y1, x2, y2 = self.__GRID[self.__Cur_Square]
		Canvas_ID = Image_Node.Render.find_overlapping(x1+5, y1+5, x2-5, y2-5)
		ID == Image_Node.find_withtag(Canvas_ID)
		print(ID)

	def Map_Wipe(self):
		"""
		Wipes the map clean of all objects placed to the screen.
		TODO: might get moved to si_files/needs to be put into the menu widget.
		"""
		item = len(self.__PLCI_Tag)-1
		while self.__PLCI_Tag != []:
			item -= 1
			if item == 0:
				item = len(self.__PLCI_Tag)-1
			ID = Image_Node.Render.find_withtag(self.__PLCI_Tag[item])
			if ID != ():
				print(self.__PLCI_Tag[item])
				Image_Node.Render.delete(self.__PLCI_Tag[item])
				del self.__imgDICT[self.__PLCI_Tag[item]]
				del self.__PLCI_Tag[item]
			print(self.__PLCI_Tag)


	def Del_Image(self, event):
		"""
		Delets individual image.
		"""
		self.Find_Square(event)

		x1, y1, x2, y2 = self.__GRID[self.__Cur_Square]
		Canvas_ID = Image_Node.Render.find_overlapping(x1+5, y1+5, x2-5, y2-5)
		ID = None
		if self.__PLCI_Tag != []:
			for item in range(len(self.__PLCI_Tag)-1, -1, -1):
				ID = Image_Node.Render.find_withtag(self.__PLCI_Tag[item])
				if ID != ():
					for tuple in Canvas_ID:
						if ID[0] == tuple:
							print(self.__PLCI_Tag[item])
							Image_Node.Render.delete(self.__PLCI_Tag[item])
							del self.__imgDICT[self.__PLCI_Tag[item]]
							del self.__PLCI_Tag[item]

	def Del_File(self):
		"""
		Delets the selected text file.
		"""
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Select to Be Deleted', filetypes=filetypes, initialdir=self.__mapFiles)
		if file == '':
			print('No File Selected')
			return
		os.remove(file)
		print(file, ':File Removed')

	def PASS(self):
		"""
		:meta private:
		"""
		pass

	def Find_Widget(self):
		"""
		Finds the widget that the mouse is in.
		"""
		x, y = self.__mainApp.winfo_pointerxy()
		self.__CUR_widget = self.__mainApp.winfo_containing(x, y)

	def Find_Square(self, event):
		"""
		Finds the square that the mouase is in.
		"""
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__GRID)):
			if event.x > self.__GRID[item][0] and event.y > self.__GRID[item][1]:
				if event.x < self.__GRID[item][2] and event.y < self.__GRID[item][3]:
					self.__Cur_Square = item


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imgDICT(self):
		"""
		:meta private:
		"""
		return self.__imgDICT

	def get_buttonDICT(self):
		"""
		:meta private:
		"""
		return self.__buttonDICT

	def get_grid(self):
		"""
		:meta private:
		"""
		return self.__GRID


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_gridSETUP(self, grid, coord):
		"""
		:meta private:
		"""
		self.__COORD = coord
		self.__GRID = grid

	def set_imgDICT(self, dict):
		"""
		:meta private:
		"""
		self.__imgDICT = dict

	def set_buttonDICT(self, dict):
		"""
		:meta private:
		"""
		self.__buttonDICT = dict

	def set_RC_Info(self, row, column):
		"""
		:meta private:
		"""
		self.__Column = column
		self.__Row 	  = row

	def set_bIDcount(self, count):
		"""
		:meta private:
		"""
		self.__bID_count = count

	def File_Images(self, buttonDICT, imgDict, PLCI_Tag, PLCI_Tk, bID_count, ID_count): #SUBJECT TO CHANGE
		"""
		:meta private:
		"""
		self.__buttonDICT = buttonDICT
		self.__bID_count  = bID_count
		self.__PLCI_Tag   = PLCI_Tag
		self.__ID_count   = ID_count
		self.__PLCI_Tk	  = PLCI_Tk
		self.__imgDICT 	  = imgDict
