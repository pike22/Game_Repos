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
			self.__imgDICT = imgDICT
			filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
			file = filedialog.asksaveasfile(title='Save Map', filetypes=filetype, defaultextension=filetype, initialdir=self.__mapFiles)
			if file == '' or file == None:
				print('No File Selected')
				return

			self.__saveLVL = open(str(file.name), 'w')

			self.__stepCount = 0
			self.Save_Line(self.__saveLVL, self.Read_List, self.__fileID)
			self.Save_Line(self.__saveLVL, self.Read_Dict, self.__imgDICT)
			self.Save_Line(self.__saveLVL, self.Read_Dict, self.__imgDICT)
			self.Save_Line(self.__saveLVL, self.Read_Dict, self.__imgDICT)

			self.__saveLVL.close() #DON'T FORGET ABOUT THIS

		# for key in self.__imgDICT.keys():
		# 	info = str(key) +'\n'
		# 	self.__saveLVL.write(info)
		# 	# print(info)
		# self.__saveLVL.write('\n<=======================================================>\n\n')
		#
		# for key in self.__imgDICT.keys():
		# 	fileLocation = self.__imgDICT[key].get_fileLoc()
		# 	info = str(key)+'='+str(fileLocation) +'\n'
		# 	self.__saveLVL.write(info)
		# 	# print(info)
		# self.__saveLVL.write('\n<=======================================================>\n\n')
		#
		# for key in self.__imgDICT.keys():
		# 	rotation = self.__imgDICT[key].get_rotation()
		# 	info = str(key)+'=z'+str(rotation) +'\n'
		# 	self.__saveLVL.write(info)
		# 	# print(info)
		# self.__saveLVL.write('\n<=======================================================>\n\n')
		#
		# for key in self.__imgDICT.keys():
		# 	coords	= self.__imgDICT[key].get_Coords()
		# 	info = str(key)+'=z'+str(coords) +'\n'
		# 	self.__saveLVL.write(info)
		# 	# print(info)
		# self.__saveLVL.write('\n<=======================================================>\n\n')


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

		self.__stepCount = 0
		self.__fileID 	 = []
		self.__fileLOC   = {}
		self.__fileROT   = {}
		self.__filePOS   = {}
		#clear all list/dict used below
		self.Read_Line(self.__importLVL, self.Read_List, self.__fileID)
		self.Read_Line(self.__importLVL, self.Read_Dict, self.__fileID)
		self.Read_Line(self.__importLVL, self.Read_Dict, self.__fileID)
		self.Read_Line(self.__importLVL, self.Read_Dict, self.__fileID)

		self.__importLVL.close()
		self.INIT_lvlFile(mainGame)
		#this splits for easy use of the second half during boot up

	def INIT_lvlFile(self, MG=None):
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



	def save_ImgButtons(self, buttonDICT):
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
		#
		# for key in self.__buttonDICT.keys():
		# 	info = str(key)+'\n'
		# 	self.__saveButton.write(info)
		# 	# print(info)
		# self.__saveButton.write('\n<=======================================================>\n\n')
		#
		# for key in self.__buttonDICT.keys():
		# 	fileLocation = self.__buttonDICT[key].get_fileLoc()
		# 	info = str(key)+'='+str(fileLocation) +'\n'
		# 	self.__saveButton.write(info)
		# 	# print(info)
		# self.__saveButton.write('\n<=======================================================>\n\n')


		self.__saveButton.close() #DON'T FORGET ABOUT THIS

	def Change_ButtonSet(self):
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

		self.Read_ButtonSet(file)
		#this splits for easy use of the second half during boot up
	def Read_ButtonSet(self, mainGame=None):
		if mainGame == None:
			filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
			file = filedialog.askopenfilename(title='Button Import', filetypes=filetypes, initialdir=self.__loadFile)
			if file == '':
				print('No File Selected')
				return
			else:
				self.__importButtons = open(file, 'r')
		else:
			self.__importButtons = open(mainGame, 'r')

		self.__stepCount = 0
		self.__bfileID 	 = []
		self.__bfileLOC  = {}
		#clear all list/dict used below
		self.Read_Line(self.__importButtons, self.Read_List, self.__bfileID)
		self.Read_Line(self.__importButtons, self.Read_Dict, self.__bfileID)

		self.__importButtons.close()


		for tag in self.__bfileID:
			# print(tag, 'button')

			#CREATES BUTTON FROM SAVE FILE
			self.buttonFromFile(self.__bfileLOC[tag], self.__imgFrame, button_ID=tag)
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
	def buttonFromFile(self, fileLoc, parent, button_ID, mainGame=None):
		image = self.__iNode.Img_Add(fileLoc)
		if mainGame == None:
			B = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.__eGUI.Drag_Drop(button_ID))
		else:
			B = None
		self.__buttonDICT[button_ID] = Button_Main(button_ID, B)
		self.__buttonDICT[button_ID].Image_Info(fileLoc=fileLoc, tkIMG=image[2], pilIMG=image[0], size=image[1])

		#Place Button
		if mainGame == None:
			B.grid(row=self.__Row, column=self.__Column)
			if self.__Column <= self.__ColumnMAX:
				self.__Column += 1
			else:
				self.__Column = 0
				self.__Row	  +=1
			self.__eGUI.set_RC_Info(column=self.__Column, row=self.__Row)
		self.__eGUI.set_buttonDICT(self.__buttonDICT)

	'''===================READ LINE FUNCTION==================='''
	#fileType is defaulted in the func called before this one
	def Read_List(self, curLine, IDtype):
		IDtype.append(curLine)
		# print(IDtype)

	#fileType is defaulted in the func called before this one
	def Read_Dict(self, curLine, step, IDtype):
		if IDtype == self.__imgDICT:
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

	def Read_Line(self, file, function, IDtype):
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
						function(line, IDtype)
				elif self.__stepCount == 1 or self.__stepCount == 2 or self.__stepCount == 3:
					if line != '':
						function(line, self.__stepCount, IDtype)
				# print(line)

	def Save_List(self, file, key):
		print('saveLIST call')
		info = str(key)+'\n'
		file.write(info)
		if key == self.list[-1]:
			print('lastKEY', key)
			self.__stepCount += 1
			return

	def Save_Dict(self, file, key, dict, step):
		print('saveDICT call', key)
		#Location
		if step == 1:
			info = str(key)+'='+(dict[key].get_fileLoc())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY', key)
				self.__stepCount += 1
				return
		#Rotation
		elif step == 2:
			info = str(key)+'=z'+(dict[key].get_rotation())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY')
				self.__stepCount += 1
				return
		#Position
		elif step == 3:
			info = str(key)+'=z'+(dict[key].get_Coords())+'\n'
			file.write(info)
			if key == self.list[-1]:
				print('lastKEY')
				self.__stepCount += 1
				return

	def Save_Line(self, file, function, dict):
		for key in dict.keys():
			self.list.append(key)
		for key in dict.keys():
			print('step:', self.__stepCount)
			if self.__stepCount == 0:
				function(file, key)
			else:
				function(file, key, dict, self.__stepCount)
		file.write('\n<=======================================================>\n\n')

	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_imgDICT(self):
		return self.__imgDICT


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_imgFrame(self, frame):
		self.__imgFrame = frame
