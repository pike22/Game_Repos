
class Projectiles():
	def __init__(self):
		self.__Image 	= None
		self.__Kinetics = None








	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_iNode(self):
		return self.__Image

	def get_kNode(self):
		return self.__Kinetics


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Nodes(self, iNode, kNode):
		self.__Image 	= iNode
		self.__Kinetics = kNode
		print(iNode, "iNode")
		print(self.__Image, 'node?')
