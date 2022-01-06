

class Menu_Main():
	def __init__(self, mainApp, color):
		self.__color	= color
		self.__mainApp  = mainApp
		self.__mainMenu = Menu(mainApp)
		self.__Events	= Menu_Events()

		mainApp.config(menu=self.__mainMenu)


	def file_menu(self, ):
		self.__fileMenu = Menu(self.__mainMenu)
		self.__mainMenu.add_cascade(label='File', menu=self.__fileMenu)
		self.__fileMenu.add_command(label='New...', )#command=COMANDHERE)
		self.__fileMenu.add_seperator()
		self.__fileMenu.add_command(label='Exit', command=self.__mainApp.quit)

	def edit_menu(self, ):
		self.__editMenu = Menu(self.__mainMenu)
		self.__editMenu.add_cascade(label='Edit', menu=self.__editMenu)
