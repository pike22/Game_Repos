import re
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .button_main import Button_Main
from .plc_imgmain import PLC_ImgMain

#for save and import information
class SI_Files():
	"""
	File *save* and *import* happens here in *SI_Files*

	Methods
	-------
	init(iNode, mainApp, color, eGUI, key)
		This is required when SI_Files() is called
	"""
	def __init__(self, iNode, mainApp, color, eGUI, key):
		#class Calls
		self.__mainApp = mainApp
		self.__iNode = iNode
		self.__color = color
		self.__eGUI  = eGUI
		self.__Key 	 = key

		#SI_FILES VARS
		self.__ColumnMAX = 4
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1

		self.__imgFrame	  = None
		self.__saveLVL	  = None
		self.__importLVL  = None

		self.__mapFiles = 'E:\Github\Game_Repos_1\Game\lvlDesigner\mapSaves'
		self.__loadFile = 'E:\Github\Game_Repos_1\Game\lvlDesigner\ButtonLoadOut'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game\z_Pictures\Walls'

		#WRITE FILE VARS
		self.__buttonDICT = {} #this is for the buttons
		self.__imgDICT	  = {} #this is for the images

		'''#READ FILE VARS'''

		#imageVARS
		self.__PLCI_Tag = []
		self.__PLCI_Tk  = []

		#mapSaves
		self.__fileID 	= []
		self.__fileLOC  = {}
		self.__fileROT  = {}
		self.__filePOS  = {}

		#buttonSaves
		self.__bfileID  = []
		self.__bfileLOC = {}

		#OTHER VARS
		self.list 		  = []
		self.__tkIMG	  = None
		self.__isRotate	  = False
		self.__ID_count   = 1
		self.__bID_count  = 1
		self.__stepCount  = 0
		self.__lastRotate = 0


	def Save_File(self, imgDICT):
		"""
		Takes what is on the canvas and converts the information into a txt file.

		Parameters
		----------
		imgDICT : dict
			Grabs a dictionary that holds all of the current images on the canvas and the related object.

		Methods
		-------
		:ref:`Save_Line`
		:ref:`Save_List`
		:ref:`Save_Dict`
		"""
		self.__imgDICT = imgDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Map', filetypes=filetype, defaultextension=filetype, initialdir=self.__mapFiles)
		if file == '' or file == None:
			print('No File Selected')
			return

		self.__saveLVL = open(str(file.name), 'w')

		self.__stepCount = 0
		self.Save_Line(file=self.__saveLVL, function=self.Save_List, dict=self.__imgDICT)
		self.Save_Line(file=self.__saveLVL, function=self.Save_Dict, dict=self.__imgDICT)
		self.Save_Line(file=self.__saveLVL, function=self.Save_Dict, dict=self.__imgDICT)
		self.Save_Line(file=self.__saveLVL, function=self.Save_Dict, dict=self.__imgDICT)

		self.__saveLVL.close() #DON'T FORGET ABOUT THIS

	def Read_File(self, mainGame=None):
		"""
		Opens a txt file that will be read and then generated onto the canvas. *Used for Game and LVLDesigner*.

		Parameters
		----------
		mainGame
			Determins if its placing the map to the level designer or the Game.

		Methods
		-------
		:ref:`Read_Line`
		:ref:`Read_List`
		:ref:`Read_Dict`
		:ref:`INIT_lvlFile`
		"""
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		if mainGame == None:
			file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
			if file == '':
				print('No File Selected')
				return
			self.__importLVL = open(file, 'r')
		else:
			self.__importLVL = open(mainGame, 'r')

		self.__stepCount = 0
		self.__fileID 	 = []
		self.__fileLOC   = {}
		self.__fileROT   = {}
		self.__filePOS   = {}
		#clear all list/dict used below
		self.Read_Line(file=self.__importLVL, function=self.Read_List, listName=self.__fileID)
		self.Read_Line(file=self.__importLVL, function=self.Read_Dict, fileTypes='LVD Maps')
		self.Read_Line(file=self.__importLVL, function=self.Read_Dict, fileTypes='LVD Maps')
		self.Read_Line(file=self.__importLVL, function=self.Read_Dict, fileTypes='LVD Maps')

		self.__importLVL.close()
		self.INIT_lvlFile(mainGame)
		#this splits for easy use of the second half during boot up

	def INIT_lvlFile(self, mainGame):
		"""
		Takes the strings read in Read_File and converts the strings in the neccisary variable type to be managed in python.

		Parameters
		----------
		mainGame
			Unused inside this function.

		Attributes
		----------
		image
			recreating the TK and PIL images.
		tkIMG
			The rotated version of the TK image.
		Coord, firstNumb, secondNumb : str
			String versions of the Coordinants.
		x, y : int
			Integer of the Coordinants.
		tag : str
			String of the ID name for an image.
		"""
		# print(self.__fileID)
		# print(self.__fileLOC)
		# print(self.__fileROT)
		# print(self.__filePOS)
		for tag in self.__fileID:
			#PULLS IN IMAGE AND ROTATES IF NEEDED
			image = self.__iNode.Img_Add(self.__fileLOC[tag])
			tkIMG = self.__iNode.Img_Rotate(image[0], int(self.__fileROT[tag]))

			#COORDS & CORNERS FROM FILE
			coord = self.__filePOS[tag]
			firstNumb = re.search("([0-9]*[^(,)])", coord)
			if firstNumb != None:
				new_firstNumb = firstNumb.group(1)
			secondNumb = re.search(str(new_firstNumb)+", ([0-9]*[^(,)])", coord)
			if secondNumb != None:
				new_secondNumb = secondNumb.group(1)
			x = int(new_firstNumb)
			y = int(new_secondNumb)
			self.__filePOS[tag] = (x, y)

			#PLACES THE IMAGES
			self.__imgDICT[tag] = PLC_ImgMain(tag, None)
			self.__imgDICT[tag].Image_Info(self.__fileLOC[tag], image[1], (x, y), self.__fileROT[tag])
			self.__iNode.Img_Place(x, y, tkIMG, LVD='yes', tag=[tag, self.__imgDICT[tag].get_group_ID()])
			self.__PLCI_Tag.append(tag)
			self.__PLCI_Tk.append(tkIMG)


		#INFO TO GUI_EVENT
		if self.__fileID != []:
			lastID  = re.search("^LVD#W(.{4})", self.__fileID[-1])
			lastID2 = lastID.group(1)
			self.__ID_count += int(lastID2)+1

		# lastBID  = re.search("^LVD#B(.{4})", self.__bIDfile[len(self.__bIDfile)-1])
		# lastBID2 = lastBID.group(1)
		# self.__bID_count += int(lastBID2)+1

		self.__eGUI.File_Images(self.__buttonDICT, self.__imgDICT, self.__PLCI_Tag, self.__PLCI_Tk, self.__bID_count, self.__ID_count)
		self.__eGUI.set_RC_Info(self.__Row, self.__Column)



	def Save_ButtonSet(self, buttonDICT):
		"""
		This saves the current Button Set to a selected file.

		Parameters
		----------
		buttonDICT : dict
			This is a dictionary that holds a set of keys and the relating python class object that holds all the buttons info.

		Methods
		-------
		:ref:`Save_Line`
		:ref:`Save_List`
		:ref:`Save_Dict`
		"""
		self.__buttonDICT = buttonDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Load Out', filetypes=filetype, defaultextension=filetype, initialdir=self.__loadFile)
		if file == '':
			print('No File Selected')
			return
		self.__saveButton = open(str(file.name), 'w')

		self.__stepCount = 0
		self.Save_Line(self.__saveButton, self.Save_List, self.__buttonDICT)
		self.Save_Line(self.__saveButton, self.Save_Dict, self.__buttonDICT)

		self.__saveButton.close() #DON'T FORGET ABOUT THIS
	def Clear_ButtonSet(self, Change=False): #make this a clean only, add parameter to switch between (clear only) and (clear then new)
		"""
		Clears the current button set. Unless Change is set to True, then it will call Button_Set()


		"""
		#this clears the current buttons to make way for the new set.
		for widget in self.__imgFrame.grid_slaves():
			widget.destroy()
		self.__buttonDICT.clear()
		self.__Row = 0
		self.__Column = 0
		self.__bID_count = 0

		if Change == True:
			self.Button_Set()
		#this splits for easy use of the second half during boot up

	def Button_Set(self, DefaultBS=None):
		"""
		Creates the button set from the file selected.

		Parameters
		----------
		DefaultBS
			The default button set when the level designer is run.

		Methods
		-------
		:ref:`Read_File`
		:ref:`Read_List`
		:ref:`Read_Dict`
		"""
		if DefaultBS == None:
			filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
			file = filedialog.askopenfilename(title='Button Import', filetypes=filetypes, initialdir=self.__loadFile)
			if file == '':
				print('No File Selected')
				return
			else:
				self.__importButtons = open(file, 'r')
		else:
			self.__importButtons = open(DefaultBS, 'r')

		self.__stepCount = 0
		self.__bfileID 	 = []
		self.__bfileLOC  = {}
		#clear all list/dict used below
		self.Read_Line(file=self.__importButtons, function=self.Read_List, listName=self.__bfileID)
		self.Read_Line(file=self.__importButtons, function=self.Read_Dict, fileTypes='Button Sets')

		self.__importButtons.close()


		for tag in self.__bfileID:
			# print(tag, 'button')

			#CREATES BUTTON FROM SAVE FILE
			self.Create_Button(self.__bfileLOC[tag], self.__imgFrame, button_ID=tag)
			# print(self.__bfileLOC[tag])

		if self.__bfileID != []:
			lastBID  = re.search("^LVD#B(.{3})", self.__bfileID[-1])
			lastBID2 = lastBID.group(1)
			self.__bID_count += int(lastBID2)+1

			# print(self.__bID_count, 'button id #')
			self.__eGUI.set_bIDcount(self.__bID_count)

	'''<========================================================================>
	#*************************#ShortCut Functions#******************************#
	<========================================================================>'''
	def Create_Button(self, fileLoc, parent, button_ID, mainGame=None):
		"""
		Creates the buttons from the given info.

		Parameters
		----------
		fileLoc
			File Location.
		parent
			The widget that the buttons will be placed in.
		button_ID
			The tag that will be associated with the button.
		mainGame
			Determins if the buttons are actually placed or not.
			NOTE: might get removed, existed for a previousely neccisary code that has since changed.

		Attributes
		----------
		Image
			The image created using :ref:`Img_Add`
		widget_ID
			Tkinter ID for the button.
		button_ID : str
			Tag of the button.
		"""
		image = self.__iNode.Img_Add(fileLoc)
		if mainGame == None:
			widget_ID = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.__eGUI.Drag_Drop(button_ID))
		else:
			widget_ID = None
		self.__buttonDICT[button_ID] = Button_Main(button_ID, widget_ID)
		self.__buttonDICT[button_ID].Image_Info(fileLoc=fileLoc, tkIMG=image[2], pilIMG=image[0], size=image[1])

		#Place Button
		if mainGame == None:
			widget_ID.grid(row=self.__Row, column=self.__Column)
			if self.__Column <= self.__ColumnMAX:
				self.__Column += 1
			else:
				self.__Column = 0
				self.__Row	  +=1
			self.__eGUI.set_RC_Info(column=self.__Column, row=self.__Row)
		self.__eGUI.set_buttonDICT(self.__buttonDICT)

	'''===================READ LINE FUNCTION==================='''
	#fileType is defaulted in the func called before this one
	def Read_List(self, curLine, listName):
		"""
		Reads the txt file's lines and puts its contents into a list.

		Parameters
		----------
		curLine : str
			The current line that is being read.
		listName
			The name of the list that *curLine* is being appended to.
		"""
		listName.append(curLine)
		# print(IDtype)

	#fileType is defaulted in the func called before this one
	def Read_Dict(self, curLine, step, Type):
		"""
		Reads the txt file's lines and puts its contents into a dictionary.

		Parameters
		----------
		curLine : str
			The current line that is being read.
		Type : str
			To switch between if reading a button file or map file.
		step : ints
			The numbered block of text that the reader is on.
		"""
		if Type == 'LVD Maps':
			if re.search("(^LVD#W.{4})", curLine) != None:
				if step == 1:
					if re.search("=(.*/.*/.*$)", curLine) != None:
						self.__fileLOC[re.search("(^LVD#W.{4})", curLine).group(1)] = re.search("=(.*/.*/.*$)", curLine).group(1)
						# print(self.__fileLOC)
				elif step == 2:
					if re.search("=z(.*$)", curLine) != None:
						self.__fileROT[re.search("(^LVD#W.{4})", curLine).group(1)] = re.search("=z(.*$)", curLine).group(1)
						# print(self.__fileROT)
				elif step == 3:
					if re.search("=z(.*$)", curLine) != None:
						self.__filePOS[re.search("(^LVD#W.{4})", curLine).group(1)] = re.search("=z(.*$)", curLine).group(1)
						# print(self.__filePOS)
		else:
			if re.search("(^LVD#B.{3})", curLine) != None:
				if step == 1:
					if re.search("=(.*/.*/.*$)", curLine) != None:
						self.__bfileLOC[re.search("(^LVD#B.{3})", curLine).group(1)] = re.search("=(.*/.*/.*$)", curLine).group(1)

	def Read_Line(self, file, function, fileTypes=None, listName=None):
		"""
		The Reader of the file. A for loop reads each line of the txt file and appropriately sets up the list and dictionaries.

		Parameters
		----------
		file : txt
			The seleced file to be read.
		function
			Another class function will get passed through.
		fileTypes
			To determin if tkinter is reading a button file or a map file.
		listName
			The named list that the associated keys will be appended to.

		Attributes
		----------
		line : str
			The current line being read from the file.
		"""
		for line in file:
			line = line.rstrip('\n')
			# print(line)

			step = re.search("(^<.*$)", line)
			if step != None:
				self.__stepCount += 1
				# print('step:', self.__stepCount)
				return
			else:
				if self.__stepCount == 0:
					if line != '':
						if listName != None:
							function(line, listName)
				elif self.__stepCount == 1 or self.__stepCount == 2 or self.__stepCount == 3:
					if line != '':
						if fileTypes != None:
							function(line, self.__stepCount, fileTypes)
				# print(line)

	def Save_List(self, file, key):
		"""
		Saves the **key** to the named file as a *str* for each key in imgDICT.keys().

		Parameters
		----------
		file : txt
			The text file that the info will be wirtten to.
		key : str
			The tag that will be saved to the text file.
		"""
		info = str(key)+'\n'
		file.write(info)
		if key == self.list[-1]:
			print('lastKEY', key)
			self.__stepCount += 1
			return

	def Save_Dict(self, file, key, dict, step):
		"""
		Saves the **key** and data to the named file as a *str* with the **dict[key].get_info**.
		Each step has a different parameter to save.

		Parameters
		----------
		file : txt
			The text file that the info will be wirtten to.
		key : str
			The current tag that will be used as a key for the dictionary.
		dict
			The Dictionary that uses the :noindex:*key* to get info from a python class object.
		step : int
			A number to determin which section the :ref:`Save_Line` is on.
		"""
		# print('saveDICT call', key)
		#Location
		if step == 1:
			info = str(key)+'='+str(dict[key].get_fileLoc())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY', key)
				self.__stepCount += 1
				return
		#Rotation
		elif step == 2:
			info = str(key)+'=z'+str(dict[key].get_rotation())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY')
				self.__stepCount += 1
				return
		#Position
		elif step == 3:
			info = str(key)+'=z'+str(dict[key].get_Coords())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY')
				self.__stepCount += 1
				return

	def Save_Line(self, file, function, dict):
		"""
		Uses a for loop to set up a list of keys and another for loop to process through the given info.

		Parameters
		----------
		file : txt
			The text file that the info will be wirtten to.
		function
			The class function that is passed through to this function.
		dict
			The dictionary passed for the required info.
		"""
		for key in dict.keys():
			self.list.append(key)
		for key in dict.keys():
			# print('step:', self.__stepCount)
			if self.__stepCount == 0:
				function(file, key)
			else:
				function(file, key, dict, self.__stepCount)
		file.write('\n<=======================================================>\n\n')

	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imgDICT(self):
		"""
		:meta private:
		"""
		return self.__imgDICT


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_imgFrame(self, frame):
		"""
		:meta private:
		"""
		self.__imgFrame = frame
