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
		self.__isRotate  = False
		self.__isMoving  = False
		self.__isDrag 	 = False
		self.__CUR_w	 = None

		#img Vars
		self.__tkIMG  = None
		self.__pilIMG = None



	"""BUTTON PRESS FUNCTIONS"""
	def openFiles(self, parent):
		file = filedialog.askopenfilename(title='Picture Import', filetypes=(("PNG", "*.png"), ("All Files", "*.*")))

		image = self.__iNode.Img_Add(file)
		self.__tkIMG  = image[2]
		self.__pilIMG = image[0]
		B1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=self.drag_drop)


		B1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1


	def drag_drop(self):
		if self.__isDrag == False:
			print('ON')
			self.__isDrag   = True
			self.__IMG = self.__iNode.Img_Place(-50, -50, self.__tkIMG, LVD='yes')
			self.__mainApp.bind_all(('<Motion>'), self.moveImg)
			self.__mainApp.bind_all(('<MouseWheel>'), self.rotation)
		else:
			print('OFF')
			self.__isDrag = False
			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))

	def rotation(self, event):
		# print('this sucks')
		# Image_Node.Render.delete(self.__IMG)
		self.__isRotate = True
		self.__tkIMG, self.__pilIMG = self.__iNode.Img_Rotate(self.__pilIMG, 90)
		self.__IMG = self.__iNode.Img_Place(event.x, event.y, self.__tkIMG, LVD='yes')

	def moveImg(self, event):
		# print((event.x, event.y))
		self.__isMoveing = True
		self.find_Widget()
		if self.__CUR_w == Image_Node.Render:
			Image_Node.Render.coords(self.__IMG, event.x, event.y)
			self.__mainApp.bind_all(('<Button-1>'), self.placeImg)
		else:
			self.__mainApp.unbind_all(('<Button-1>'))
			pass

	def find_Widget(self):
		x,y = self.__mainApp.winfo_pointerxy()
		self.__CUR_w = self.__mainApp.winfo_containing(x,y)

	def placeImg(self, event):
		self.__iNode.Img_Place(event.x, event.y, self.__tkIMG, LVD='yes')

	def mousePosition(self, event): #finds coords & shows them
		#(event.x, event.y) will always be mouse position
		print((event.x, event.y), 'mouse coords')
