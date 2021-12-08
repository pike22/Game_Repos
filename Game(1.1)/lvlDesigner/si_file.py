import re
from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_statics import GUI_Statics

#for save and import information
class SI_File():
	def __init__(self, iNode, mainApp, eGUI, key):
		#class Calls
		self.__mainApp = mainApp
		self.__iNode = iNode
		self.__eGUI  = eGUI
		self.__Key 	 = key

		#Cur_Img
		self.__placedIMG_tag = []
		self.__pilIMG_LIST	= []
		self.__tkIMG_LIST	= []
		self.__imgDICT = {}

		#FILE VARS
		self.__imgFrame = None
		self.__lvlFILE  = None
		self.__mapFiles = 'E:\Github\Game_Repos_1\Game(1.1)\lvlDesigner\mapSaves'
		self.__pngFiles = 'E:\Github\Game_Repos_1\Game(1.1)\z_Pictures\Walls'

		self.__rotationDICT = {}
		self.__cornersDICT  = {}
		self.__coordDICT	= {}
		self.__fileDICT		= {}
		self.__gID_DICT		= {}
		self.__gIDfile		= []
		self.__IDfile		= []
		self.__tkIMG		= None
		self.__isRotate		= False

		self.__rotateVar = None
		self.__newNUMB	 = 1
		self.__IDsNUMB	 = 1


	def saveFILE(self, imgDICT):
		self.__imgDICT = imgDICT
		filetype = [('Text Document', '*.txt'), ('All Files', '*.*')]
		file = filedialog.asksaveasfile(title='Save Map', filetypes=filetype, defaultextension=filetype, initialdir=self.__mapFiles)

		targFile = open(str(file.name), 'w')

		for key in self.__imgDICT.keys():
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID   = self.__imgDICT[key].get_ID(item, full=False)
				info = str(ID) +'\n'
				targFile.write(info)
				# print(info)
		targFile.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			for item in range(len(self.__imgDICT[key].get_ID())):
				fileLocation = self.__imgDICT[key].get_fileLocation()
				ID 	 = self.__imgDICT[key].get_ID(item, full=False)
				info = str(ID)+'='+str(fileLocation) +'\n'
				targFile.write(info)
				# print(info)
		targFile.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 	 = self.__imgDICT[key].get_ID(item, full=False)
				rotation = self.__imgDICT[key].get_PLC_Rotation(ID)
				info = str(ID)+'=z'+str(rotation) +'\n'
				targFile.write(info)
				# print(info)
		targFile.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 	 = self.__imgDICT[key].get_ID(item, full=False)
				coords	= self.__imgDICT[key].get_PLC_Coords(ID)
				info = str(ID)+'=z'+str(coords) +'\n'
				targFile.write(info)
				# print(info)
		targFile.write('\n<=======================================================>\n\n')

		for key in self.__imgDICT.keys():
			for item in range(len(self.__imgDICT[key].get_ID())):
				ID 	 = self.__imgDICT[key].get_ID(item, full=False)
				info = str(ID)+'='+str(key) +'\n'
				targFile.write(info)
				# print(info)
		targFile.write('\n<=======================================================>\n\n')

		targFile.close() #DON'T FORGET ABOUT THIS


	def open_lvlFIles(self, mainGame=None):
		filetypes = [(("TXT", "*.txt"), ("All Files", "*.*"))]
		if mainGame == None:
			self.__lvlFILE = filedialog.askopenfilename(title='Level Import', filetypes=filetypes, initialdir=self.__mapFiles)
			if self.__lvlFILE == '':
				print('No File Selected')
				return
			targFile = open(self.__lvlFILE, 'r')
		else:
			targFile = open(mainGame, 'r')
		tempLIST = []
		counting = 0
		lastg_ID = None
		seperator = None
		for line in targFile:
			line = line.rstrip('\n')
			# print(line)

			ID = re.search("(^PLC#.{3})", line)
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
					if newRotation == 'None':
						newRotation = None
					else:
						newRotation = int(newRotation)
					self.__rotationDICT[newID] = newRotation

			coords = re.search("=z(.*$)", line)
			if coords != None and seperator == None:
				newCoords = coords.group(1)
				if counting == 3:
					self.__coordDICT[newID] = newCoords

			g_ID = re.search("=(LVL_D#.{3})", line)
			if g_ID != None and seperator == None:
				newg_ID = g_ID.group(1)
				if counting == 4:
					if lastg_ID != None:
						if newg_ID != lastg_ID:
							self.__gIDfile.append(newg_ID)
					else:
						self.__gIDfile.append(newg_ID)
					self.__gID_DICT[newID] = newg_ID
					lastg_ID = newg_ID

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
		# print(self.__gID_DICT)
		# print("^Group ID\n")

		targFile.close()

		image = None
		tkIMG = None
		pilIMG = None
		self.__rotateVar = None
		lastKEY = None
		lenID = re.search("^PLC#(.{3})", self.__IDfile[len(self.__IDfile)-1])
		newlenID = lenID.group(1)
		self.__newNUMB += int(newlenID)
		self.__IDsNUMB += len(self.__gIDfile)
		for item in range(len(self.__IDfile)):
			image = self.__iNode.Img_Add(self.__fileDICT[self.__IDfile[item]])

			self.__rotateVar = self.__rotationDICT[self.__IDfile[item]]
			if self.__rotateVar != None:
				self.__isRotate = True
				tkIMG, pilIMG = self.__iNode.Img_Rotate(image[0], int(self.__rotateVar))
			else:
				self.__isRotate = False
				pass
			# print('-----------------------------------')

			"""#_Coord str to Coord int (tuple)_#"""
			coord = self.__coordDICT[self.__IDfile[item]]

			firstNumb = re.search("([0-9]*[^(,)])", coord)
			if firstNumb != None:
				new_firstNumb = firstNumb.group(1)
			secondNumb = re.search(str(new_firstNumb)+", ([0-9]*[^(,)])", coord)
			if secondNumb != None:
				new_secondNumb = secondNumb.group(1)
			x = int(new_firstNumb)
			y = int(new_secondNumb)
			self.__coordDICT[self.__IDfile[item]] = (x, y)
			self.__cornersDICT[self.__IDfile[item]] = (x, y, x+self.__Key, y+self.__Key)

			# print(self.__IDfile[item], ':', self.__isRotate)
			# print(self.__IDfile[item], ':', self.__fileDICT[self.__IDfile[item]])
			# print(self.__IDfile[item], ':', self.__gID_DICT[self.__IDfile[item]])
			# print(self.__IDfile[item])
			# print('-----------------------------')

			if lastKEY != None:
				if self.__fileDICT[self.__IDfile[item]] != self.__fileDICT[lastKEY]:
					self.__imgDICT = self.__eGUI.buttonFromSave(fileLoc=self.__fileDICT[self.__IDfile[item]], parent=self.__imgFrame, button_ID=self.__gID_DICT[self.__IDfile[item]], MG=mainGame)
			elif lastKEY == None:
				self.__imgDICT = self.__eGUI.buttonFromSave(fileLoc=self.__fileDICT[self.__IDfile[item]], parent=self.__imgFrame, button_ID=self.__gID_DICT[self.__IDfile[item]], MG=mainGame)

			if self.__isRotate == True:
				button_ID = self.__gID_DICT[self.__IDfile[item]]
				ID = self.__IDfile[item]
				Coords=self.__coordDICT[self.__IDfile[item]]
				Corners=self.__cornersDICT[self.__IDfile[item]]
				rotation=self.__rotationDICT[self.__IDfile[item]]
				self.__eGUI.imgINFO(button_ID=button_ID, ID=ID, Coord=Coords, Corner=Corners, tkIMG=tkIMG, rotation=rotation, isRotate=True, fileREAD=(x, y))

				self.__placedIMG_tag.append(self.__IDfile[item])
			else:
				button_ID = self.__gID_DICT[self.__IDfile[item]]
				ID = self.__IDfile[item]
				Coords=self.__coordDICT[self.__IDfile[item]]
				Corners=self.__cornersDICT[self.__IDfile[item]]
				rotation=self.__rotationDICT[self.__IDfile[item]]
				self.__eGUI.imgINFO(button_ID=button_ID, ID=ID, Coord=Coords, Corner=Corners, tkIMG=image[2], rotation=rotation, isRotate=False, fileREAD=(x, y))

				self.__placedIMG_tag.append(self.__IDfile[item])
			lastKEY = self.__IDfile[item] #KEEP THIS LAST IN LOOP

			self.__eGUI.set_Images(self.__imgDICT, self.__newNUMB, self.__IDsNUMB, self.__placedIMG_tag)



	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_imgFrame(self, frame):
		self.__imgFrame = frame

	def get_imgDICT(self):
		return self.__imgDICT
