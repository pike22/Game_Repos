#this will be the parrent class for everything in the Entity folder

class All_Entities():
	def __init__(self):
		self.__mainApp = None


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainApp(self):
		return self.__mainApp


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_mainApp(self, mainApp):
		self.__mainApp = mainApp
