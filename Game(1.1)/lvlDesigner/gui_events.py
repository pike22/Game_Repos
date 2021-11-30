from tkinter import *
from Engine import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from .gui_statics import GUI_Statics

class GUI_Events():
	def __init__(self, iNode, kNode, mainApp, color):
		self.__ColumnMAX = 3
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1

		#other classes
		self.__mainApp = mainApp
		self.__iNode = iNode
		self.__kNode = kNode
		self.__color = color

		#GUI vars
		self.__x, self.__y = 0, 0
		self.__lastRotate= 0
		self.__isRotate  = False
		self.__isMoving  = False
		self.__isDrag 	 = False
		self.__CUR_w	 = None

		#img Vars
		self.__pilIMG_LIST	= []
		self.__tkIMG_LIST	= []
		self.__placedIMG 	= []
		self.__imgDICT	 	= {}
		self.__IDsNUMB		= 0
		self.__pilIMG 		= None
		self.__tkIMG 		= None
		self.__IMG = None



	"""BUTTON PRESS FUNCTIONS"""
	def openFiles(self, parent):
		file = filedialog.askopenfilename(title='Picture Import', filetypes=(("PNG", "*.png"), ("All Files", "*.*")))

		ID = 'LVLD#0'+str(self.__IDsNUMB)
		self.__IDsNUMB += 1

		image = self.__iNode.Img_Add(file)
		self.__tkIMG_LIST.append(image[2])
		self.__pilIMG_LIST.append(image[0])
		B1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.drag_drop(ID))
		self.__imgDICT[ID] = GUI_Statics(ID)
		self.__imgDICT[ID].add_IMG(tkIMG=image[2], pilIMG=image[0])
		self.__imgDICT[ID].info_Dump(ID, tkIMG=image[2], pilIMG=image[0], fLocation=file)


		B1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1


	def drag_drop(self, ID):
		if self.__isDrag == False:
			print('ON')
			self.__isDrag   = True
			self.__IMG = self.__iNode.Img_Place(-50, -50, self.__imgDICT[ID].get_tkIMG(), LVD='yes', tag=ID)
			self.__mainApp.bind_all(('<Motion>'), lambda event, arg=ID: self.moveImg(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=ID: self.rotation(event, arg))
		else:
			print('OFF')
			self.__isDrag = False
			self.__pilIMG = None
			self.__tkIMG  = None
			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))

	def rotation(self, event, ID):
		# print('this sucks')
		self.__lastRotate += 90
		self.__isRotate = True
		self.__tkIMG, self.__pilIMG = self.__iNode.Img_Rotate(self.__imgDICT[ID].get_pilIMG(), self.__lastRotate)
		self.__IMG = self.__iNode.Img_Place(event.x, event.y, self.__tkIMG, LVD='yes', tag=ID)

	def moveImg(self, event, ID):
		# print((event.x, event.y))
		self.__isMoveing = True
		self.find_Widget()
		if self.__CUR_w == Image_Node.Render:
			canvID = Image_Node.Render.find_withtag(self.__IMG)[0]
			Image_Node.Render.coords(canvID, event.x, event.y)
			self.__mainApp.bind_all(('<Button-1>'), lambda event, arg=ID: self.placeImg(event, arg))
		else:
			self.__mainApp.unbind_all(('<Button-1>'))
			pass

	def find_Widget(self):
		x,y = self.__mainApp.winfo_pointerxy()
		self.__CUR_w = self.__mainApp.winfo_containing(x,y)

	def placeImg(self, event, ID):
		if self.__tkIMG != None:
			self.__tkIMG_LIST.append(self.__tkIMG)
			self.__iNode.Img_Place(event.x, event.y, self.__tkIMG, LVD='yes', tag=ID)
			# yes = Image_Node.Render.find_withtag(ID)[0]
		else:
			self.__tkIMG_LIST.append(self.__imgDICT[ID].get_tkIMG())
			self.__iNode.Img_Place(event.x, event.y, self.__imgDICT[ID].get_tkIMG(), LVD='yes', tag=ID)

	def mousePosition(self, event): #finds coords & shows them
		#(event.x, event.y) will always be mouse position
		print((event.x, event.y), 'mouse coords')
