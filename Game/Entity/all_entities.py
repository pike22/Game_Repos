#this will be the parrent class for everything in the Entity folder

class All_Entities():
	"""
	If you see this it means the .rst file wasn't deleted!!
	"""
	def __init__(self):
		self.__mainApp = None


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainApp(self):
		"""
		:meta private:
		"""
		return self.__mainApp

	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_mainApp(self, mainApp):
		"""
		:meta private:
		"""
		self.__mainApp = mainApp
