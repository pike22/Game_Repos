from tkinter import *
from tkinter import filedialog


class GUI_Main():
	def __init__(self):
		self.__ColumnMAX = 4
		self.__Column = 0
		self.__RowMAX = 10
		self.__Row	  = 1

	"""BUTTON PRESS FUNCTIONS"""
	def openFiles(self, parent):
		file = filedialog.askopenfilename(title='Picture Import', filetypes=(("PNG", "*.png"), ("All Files", "*.*")))

		image = PhotoImage(file=file)
		l1 = Label(parent, image=image)
		l1.image = image
		print(self.__Row, 'row')
		print(self.__Column, 'column')
		l1.grid(row=self.__Row, column=self.__Column)
		if self.__Column <= self.__ColumnMAX:
			self.__Column += 1
		else:
			self.__Column = 0
			self.__Row	  +=1
