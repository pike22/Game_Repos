
class Projectiles():
	def __init__(self):
		self.__Image 	 = None
		self.__Kinetics  = None
		self.__Collision = None








	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_iNode(self):
		return self.__Image

	def get_kNode(self):
		return self.__Kinetics

	def get_cNode(self):
		return self.__Collision

	def copy_Node(self, obj):
		self.__Image 	 = obj.get_iNode()
		self.__Kinetics  = obj.get_kNode()
		self.__Collision = obj.get_cNode()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Nodes(self, iNode, kNode, cNode):
		self.__Image 	= iNode
		self.__Kinetics = kNode
		self.__Collision= cNode
