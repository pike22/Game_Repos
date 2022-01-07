from tkinter import *
from .si_files import SI_Files
from .gui_events import GUI_Events
from .menu_events import Menu_Events

class Menu_Main():
	def __init__(self, mainApp, color):
		self.__color	= color
		self.__mainApp  = mainApp
		self.__mainMenu = Menu(mainApp)
		self.__Events	= Menu_Events()
		self.__eGUI 	= None
		self.__siFILES  = None

		"""#MENU TABS#"""
		self.__fileMenu = Menu(self.__mainMenu)
		self.__editMenu = Menu(self.__mainMenu)
		self.__nextMenu = Menu(self.__mainMenu)#plcHOLD/quick copy

		mainApp.config(menu=self.__mainMenu)

	def menu_setUP(self, ):
		self.file_menu()
		self.edit_menu()


	def file_menu(self, ):
		self.__mainMenu.add_cascade(label='File', menu=self.__fileMenu)
		self.__fileMenu.add_command(label='New File', )# command=COMMANDHERE)
		self.__fileMenu.add_command(label='Open File', command=self.__siFILES.Read_File)
		self.__fileMenu.add_command(label='Save File', command=lambda:self.__siFILES.Save_File(self.__eGUI.get_imgDICT()))
		self.__fileMenu.add_command(label='----')
		self.__fileMenu.add_command(label='Exit', command=self.__mainApp.quit)

	def edit_menu(self, ):
		self.__mainMenu.add_cascade(label='Edit', menu=self.__editMenu)
		self.__editMenu.add_command(label='plcHOLD', )#command=COMMANDHERE)

	def next_menu(self): #place holder
		self.__mainMenu.add_cascade(label='next', menu=self.__nextMenu)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	#def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_eGUI(self, gui):
		self.__eGUI = gui

	def set_siFILES(self, siFILES):
		self.__siFILES = siFILES
