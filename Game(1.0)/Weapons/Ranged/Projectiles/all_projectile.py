
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

	def copy_Node(self, p):
		self.__Image = p.get_iNode()
		self.__Kinetics = p.get_kNode()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Nodes(self, iNode, kNode):
		self.__Image 	= iNode
		self.__Kinetics = kNode
