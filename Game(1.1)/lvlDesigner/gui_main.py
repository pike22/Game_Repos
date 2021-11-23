from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image #PIL = Pillow
from Engine import *


class GUI_Main():
	def __init__(self, iNode, kNode, mainApp, color):
		self.__ColumnMAX = 3
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1
		self.__iNode  = iNode
		self.__kNode  = kNode
		self.__mainApp= mainApp
		self.__color  = color

		#random vars
		self.__x, self.__y = 0, 0
		self.__CURwidget = None
		self.__Drag 	 = False
		self.__IMG		 = 0


	"""BUTTON PRESS FUNCTIONS"""
	def openFiles(self, parent):
		file = filedialog.askopenfilename(title='Picture Import', filetypes=(("PNG", "*.png"), ("All Files", "*.*")))

		image = self.__iNode.Img_Add(file)
		l1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.drag_drop(image[2], image[0]))
		l1.image = image #places the img inside the button
		# print(self.__Row, 'row')
		# print(self.__Column, 'column')
		l1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1

	def mousePosition(self, event): #finds coords & shows them
		#(event.x, event.y) will always be mouse position
		print((event.x, event.y), 'mouse coords')


	def drag_drop(self, pyImg, pilImg):
		if self.__Drag == False:
			self.__Drag = True
			print('ON')
			self.__IMG = self.__iNode.Img_Place(self.__x, self.__y, pyImg,  LVD='yes')
			self.__mainApp.bind_all(('<Motion>'), lambda event, arg=(self.__IMG, pyImg): self.moveImg(event, arg))
			self.__mainApp.bind_all(('<MouseWheel>'), lambda event, arg=(self.__IMG, pilImg): self.rotation(event, arg))

		else:
			self.__Drag = False
			self.__mainApp.unbind_all(('<Motion>'))
			self.__mainApp.unbind_all(('<MouseWheel>'))
			print('OFF')

	def rotation(self, event, img):
		print('this sucks')
		Image_Node.Render.delete(img[0])
		newIMG = self.__iNode.Img_Rotate(img[1], 90)
		self.__iNode.Img_Place(event.x, event.y, newIMG)



	def moveImg(self, event, img_ID):
		# print((event.x, event.y))
		self.find_Widget()
		if self.__CURwidget == Image_Node.Render:
			Image_Node.Render.coords(img_ID[0], event.x, event.y)
			self.__mainApp.bind_all(('<Button-1>'), lambda event, arg=img_ID[1]: self.placeImg(event, arg))
		else:
			self.__mainApp.unbind_all(('<Button-1>'))

	def find_Widget(self):
	    x,y = self.__mainApp.winfo_pointerxy()
	    self.__CURwidget = self.__mainApp.winfo_containing(x,y)


	def placeImg(self, event, img):
		self.__iNode.Img_Place(event.x, event.y, img)
