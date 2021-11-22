from tkinter import *
from tkinter import filedialog
from Engine import *


class GUI_Main():
	def __init__(self, iNode, mainApp, color):
		self.__ColumnMAX = 2
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1
		self.__iNode  = iNode
		self.__mainApp= mainApp
		self.__color  = color

		#random vars
		self.__Drag = False
		self.__x, self.__y = 0, 0

	"""BUTTON PRESS FUNCTIONS"""
	def openFiles(self, parent, parent2):
		file = filedialog.askopenfilename(title='Picture Import', filetypes=(("PNG", "*.png"), ("All Files", "*.*")))

		image = self.__iNode.Img_Add(file)
		l1 = Button(parent, image=image[2], bg=self.__color, activebackground=self.__color, command=lambda:self.drag_drop(image[2], parent2))
		l1.image = image #places the img inside the button
		# print(self.__Row, 'row')
		# print(self.__Column, 'column')
		l1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1


	def mousePosition(self, event):
		print((event.x, event.y), 'mouse coords')
		self.__x, self.__y = event.x, event.y

	def drag_drop(self, img, parent):
		if self.__Drag == False:
			self.__Drag = True
			Image_Node.Render.bind_all(('<Button-1>'), self.mousePosition)
			img = self.__iNode.Img_Place(self.__x, self.__y, img, Grid='no', LVD='yes', render=parent)

			Image_Node.Render.bind_all(('<Motion>'), lambda event, arg=img: self.moveImg(event, arg))

		else:
			self.__TPress = False
			Image_Node.Render.unbind_all(('<Motion>'))
			print('no more')

	def moveImg(self, event, img_ID):
		print((event.x, event.y))

		Image_Node.Render.coords(img_ID, event.x, event.y)

	def placeHold(self):
		print('Place Holding')
