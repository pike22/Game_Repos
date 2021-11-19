from tkinter import *
from tkinter import filedialog


class GUI_Main():
	def __init__(self, mainApp):
		self.__mainApp = mainApp

		self.__frameList = []
		self.__buttonList= []


	"""FRAME FUNC"""
	def Create_Frame(self, text=None, width=None, height=None, parent=None, bg=None):
		if parent == None:
			tagOrId = LabelFrame(self.__mainApp, text=text, width=width, height=height, bg=None, labelanchor='n')
		else:
			tagOrId = LabelFrame(parent, text=text, width=width, height=height, bg=None, labelanchor='n')
		self.__frameList.append(tagOrId)
		return tagOrId

	def Place_Frame(self, tagOrId, row, column, rowspan=None, columnspan=None):
		if rowspan == None and columnspan == None:
			tagOrId.grid(row=row, column=column)
		elif rowspan != None or columnspan != None:
			tagOrId.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)

		for item in range(len(self.__frameList)):
			self.__frameList[item].grid_propagate(0)


	"""BUTTON FUNC"""
	def Create_Button(self, text=None, width=None, height=None, parent=None, bg=None, command=None):
		if command == None:
			tagOrId = Button(parent, text=text, width=width, height=height, bg=bg)
		else:
			tagOrId = Button(parent, text=text, width=width, height=height, bg=bg, command=command)
		self.__buttonList.append(tagOrId)

	def Place_Button(self, tagOrId, row, column, rowspan=None, columnspan=None):
		if rowspan == None and columnspan == None:
			tagOrId.grid(row=row, column=column)
		elif rowspan != None or columnspan != None:
			tagOrId.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)

		for item in range(len(self__buttonList)):
			self.__buttonList[item].grid_propagate(0)



	"""FileDialog FUNC"""
	def openFiles(self):
		filelocation = filedialog.askopenfilename(title='file?', filetypes = (("Text files", "*.txt*"), ("all files","*.*")))
