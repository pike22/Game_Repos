#this will be the parrent class for everything in the Entity folder

class All_Entities():
	def __init__(self):
		self.__mainApp = None
		self.__GameTime = 0


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainApp(self):
		return self.__mainApp

	def get_GameTime(self):
		return self.__GameTime


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_mainApp(self, mainApp):
		self.__mainApp = mainApp

	def save_GT(self, GameTime):
		self.__GameTime = GameTime
