import re
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .button_main import Button_Main
from .plc_imgmain import PLC_ImgMain

#for save and import information
class SI_Files():
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

		self.__mapFiles = 'E:\Github\Game_Repos_1\Game(1.2)\lvlDesigner\mapSaves'
		self.__loadFile = 'E:\Github\Game_Repos_1\Game(1.2)\lvlDesigner\ButtonLoadOut'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game(1.2)\z_Pictures\Walls'

		#WRITE FILE VARS
		self.__buttonDICT = {} #this is for the buttons
		self.__imgDICT	  = {} #this is for the images

		#READ FILE VARS
		self.__PLCI_Tag = []
		self.__PLCI_Tk  = []

		self.__rotationDICT = {}
		self.__cornersDICT  = {}
		self.__coordDICT	= {}
		self.__fileDICT		= {}
		self.__bID_DICT		= {}
		self.__buttonID		= []
		self.__bIDfile		= []
		self.__IDfile		= []
		self.__tkIMG		= None
		self.__isRotate		= False
		self.__lastRotate 	= 0

		#OTHER VARS
		self.__ID_count  = 1
		self.__bID_count = 1


	def saveFILE(self, imgDICT):
		self.__imgDICT = imgDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Map', filetypes=filetype, defaultextension=filetype, initialdir=self.__mapFiles)

		self.__saveLVL = open(str(file.name), 'w')

		for key in self.__imgDICT.keys():
			info = str(key) +'\n'
			self.__saveLVL.write(info)
			# print(info)
		self.__saveLVL.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			fileLocation = self.__imgDICT[key].get_fileLoc()
			info = str(key)+'='+str(fileLocation) +'\n'
			self.__saveLVL.write(info)
			# print(info)
		self.__saveLVL.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			rotation = self.__imgDICT[key].get_rotation()
			info = str(key)+'=z'+str(rotation) +'\n'
			self.__saveLVL.write(info)
			# print(info)
		self.__saveLVL.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			coords	= self.__imgDICT[key].get_Coords()
			info = str(key)+'=z'+str(coords) +'\n'
			self.__saveLVL.write(info)
			# print(info)
		self.__saveLVL.write('\n<=======================================================>\n\n')

		# for key in self.__imgDICT.keys():
		# 	button_ID = self.__imgDICT[key].get_button_ID()
		# 	info = str(key)+'='+str(button_ID) +'\n'
		# 	self.__saveLVL.write(info)
		# 	# print(info)
		# self.__saveLVL.write('\n<=======================================================>\n\n')

		self.__saveLVL.close() #DON'T FORGET ABOUT THIS


	def Read_File(self, mainGame=None):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		if mainGame == None:
			file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
			if file == '':
				print('No File Selected')
				return
			self.__importLVL = open(file, 'r')
		else:
			self.__importLVL = open(mainGame, 'r')

		tempLIST  = []
		counting  = 0
		lastB_ID  = None
		seperator = None
		newID	  = None
		for line in self.__importLVL:
			line = line.rstrip('\n')
			# print(line)

			ID = re.search("(^LVD#W.{4})", line)
			if ID != None:
				newID = ID.group(1)
				if counting == 0:
					self.__IDfile.append(newID)

			fileLoc = re.search("=(.*/.*/.*$)", line)
			if fileLoc != None:
				newFileLoc = fileLoc.group(1)
				if counting == 1:
					self.__fileDICT[newID] = newFileLoc

			rotation = re.search("=z(.*$)", line)
			if rotation != None:
				newRotation = rotation.group(1)
				if counting == 2:
					newRotation = int(newRotation)
					self.__rotationDICT[newID] = newRotation

			coords = re.search("=z(.*$)", line)
			if coords != None and seperator == None:
				newCoords = coords.group(1)
				if counting == 3:
					self.__coordDICT[newID] = newCoords

			# B_ID = re.search("=(LVD#B.{3})", line)
			# if B_ID != None and seperator == None:
			# 	newB_ID = B_ID.group(1)
			# 	if counting == 4:
			# 		self.__bID_DICT[newID] = newB_ID
			# 		lastB_ID = newB_ID

			seperator = re.search("(^<.*$)", line)
			if seperator != None:
				counting += 1

		# print(self.__IDfile)
		# print("^ID's\n")
		# print(self.__fileDICT)
		# print("^file locations\n")
		# print(self.__rotationDICT)
		# print("^Files Rotation\n")
		# print(self.__coordDICT)
		# print("^Coords\n")
		# print(self.__bID_DICT)
		# print("^Button ID\n")

		self.__importLVL.close()
		self.INIT_lvlFile(mainGame)

	def INIT_lvlFile(self, MG=None):
		lastB_ID = None
		for tag in self.__IDfile:

			#CREATES BUTTON FROM SAVE FILE
			# if lastB_ID != None:
			# 	if self.__bID_DICT[tag] != lastB_ID and self.__bID_DICT[tag] not in self.__bIDfile:
			# 		self.buttonFromFile(self.__fileDICT[tag], self.__imgFrame, button_ID=self.__bID_DICT[tag])#, MG=MG)
			# 		self.__bIDfile.append(self.__bID_DICT[tag])
			# else:
			# 	self.buttonFromFile(self.__fileDICT[tag], self.__imgFrame, button_ID=self.__bID_DICT[tag])#, MG=MG)
			# 	self.__bIDfile.append(self.__bID_DICT[tag])
			# lastB_ID = self.__bID_DICT[tag]

			#PULLS IN IMAGE AND ROTATES IF NEEDED
			image = self.__iNode.Img_Add(self.__fileDICT[tag])
			self.__lastRotate = self.__rotationDICT[tag]
			tkIMG = self.__iNode.Img_Rotate(image[0], int(self.__lastRotate))

			#COORDS & CORNERS FROM FILE
			coord = self.__coordDICT[tag]
			firstNumb = re.search("([0-9]*[^(,)])", coord)
			if firstNumb != None:
				new_firstNumb = firstNumb.group(1)
			secondNumb = re.search(str(new_firstNumb)+", ([0-9]*[^(,)])", coord)
			if secondNumb != None:
				new_secondNumb = secondNumb.group(1)
			x = int(new_firstNumb)
			y = int(new_secondNumb)
			self.__coordDICT[tag] = (x, y)
			self.__cornersDICT[tag] = (x, y, x+self.__Key, y+self.__Key)

			#PLACES THE IMAGES
			self.__imgDICT[tag] = PLC_ImgMain(tag, None)
			self.__imgDICT[tag].Image_Info(self.__buttonDICT[self.__bID_DICT[tag]].get_fileLoc(),
											self.__buttonDICT[self.__bID_DICT[tag]].get_Size(),
											(x, y), self.__lastRotate)
			self.__iNode.Img_Place(x, y, tkIMG, LVD='yes', tag=[tag, self.__imgDICT[tag].get_group_ID()])
			self.__PLCI_Tag.append(tag)
			self.__PLCI_Tk.append(tkIMG)


		#INFO TO GUI_EVENT
		lastID  = re.search("^LVD#W(.{4})", self.__IDfile[-1])
		lastID2 = lastID.group(1)
		self.__ID_count += int(lastID2)+1

		# lastBID  = re.search("^LVD#B(.{4})", self.__bIDfile[len(self.__bIDfile)-1])
		# lastBID2 = lastBID.group(1)
		# self.__bID_count += int(lastBID2)+1

		self.__eGUI.File_Images(self.__buttonDICT, self.__imgDICT, self.__PLCI_Tag, self.__PLCI_Tk, self.__bID_count, self.__ID_count)
		self.__eGUI.set_RC_Info(self.__Row, self.__Column)


	def buttonFromFile(self, fileLoc, parent, button_ID, MG=None):
		image = self.__iNode.Img_Add(fileLoc)
		if MG == None:
			B = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.__eGUI.Drag_Drop(button_ID))
		else:
			B = None
		self.__buttonDICT[button_ID] = Button_Main(button_ID, B)
		self.__buttonDICT[button_ID].Image_Info(fileLoc=fileLoc, tkIMG=image[2], pilIMG=image[0], size=image[1])

		#Place Button
		if MG == None:
			B.grid(row=self.__Row, column=self.__Column)
			if self.__Column <= self.__ColumnMAX:
				self.__Column += 1
			else:
				self.__Column = 0
				self.__Row	  +=1
			self.__eGUI.set_RC_Info(column=self.__Column, row=self.__Row)
		self.__eGUI.set_buttonDICT(self.__buttonDICT)

	def save_ImgButtons(self, buttonDICT):
		self.__buttonDICT = buttonDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Load Out', filetypes=filetype, defaultextension=filetype, initialdir=self.__loadFile)
		if file == '':
			print('No File Selected')
			return
		self.__saveButton = open(str(file.name), 'w')

		for key in self.__buttonDICT.keys():
			info = str(key)+'\n'
			self.__saveButton.write(info)
			# print(info)
		self.__saveButton.write('\n<=======================================================>\n\n')

		for key in self.__buttonDICT.keys():
			fileLocation = self.__buttonDICT[key].get_fileLoc()
			info = str(key)+'='+str(fileLocation) +'\n'
			self.__saveButton.write(info)
			# print(info)
		self.__saveButton.write('\n<=======================================================>\n\n')


		self.__saveButton.close() #DON'T FORGET ABOUT THIS

	def changeLoadout(self, ):
		#this clears the current buttons to make way for the new set.
		for widget in self.__imgFrame.grid_slaves():
			widget.destroy()
		self.__buttonDICT.clear()
		self.__Row = 0
		self.__Column = 0
		self.__bID_count = 0

		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__loadFile)
		if file == '':
			print('No File Selected')
			return

		self.open_ImgButtons(file)





	def open_ImgButtons(self, savedFile=None):
		if savedFile == None:
			filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
			file = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__loadFile)
			if file == '':
				print('No File Selected')
				return
			else:
				self.__importButtons = open(file, 'r')
		else:
			self.__importButtons = open(savedFile, 'r')

		counting = 0
		self.__buttonID = []
		self.__fileDICT = {}
		for line in self.__importButtons:
			line = line.rstrip('\n')
			# print(line)

			ID = re.search("(^LVD#B.{3})", line)
			if ID != None:
				newID = ID.group(1)
				if counting == 0:
					self.__buttonID.append(newID)
			# print(self.__buttonID)


			fileLoc = re.search("=(.*/.*/.*$)", line)
			if fileLoc != None:
				newFileLoc = fileLoc.group(1)
				if counting == 1:
					self.__fileDICT[newID] = newFileLoc
			# print(self.__fileDICT)

			seperator = re.search("(^<.*$)", line)
			if seperator != None:
				counting += 1


		lastB_ID = None
		for tag in self.__buttonID:

			#CREATES BUTTON FROM SAVE FILE
			self.buttonFromFile(self.__fileDICT[tag], self.__imgFrame, button_ID=tag)
			self.__bIDfile.append(tag)

		if self.__bIDfile != []:
			lastBID  = re.search("^LVD#B(.{3})", self.__bIDfile[-1])
			lastBID2 = lastBID.group(1)
			self.__bID_count += int(lastBID2)+1

			self.__eGUI.set_bIDcount(self.__bID_count)



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imgDICT(self):
		return self.__imgDICT


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_imgFrame(self, frame):
		self.__imgFrame = frame
