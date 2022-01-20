
class Projectiles():
	"""
	Is the parrent class to the Projectiles and there for sets up the variables that would be the same acrossed all files in the
	Projectiles folder.		
	"""
	def __init__(self):
		self.__Image 	 = None
		self.__Kinetics  = None
		self.__Collision = None

	# def Func_Name(params):
	#	blah blah blah


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_iNode(self):
		"""
		:meta private:
		"""
		return self.__Image

	def get_kNode(self):
		"""
		:meta private:
		"""
		return self.__Kinetics

	def get_cNode(self):
		"""
		:meta private:
		"""
		return self.__Collision

	def copy_Node(self, obj):
		"""
		:meta private:
		"""
		self.__Image 	 = obj.get_iNode()
		self.__Kinetics  = obj.get_kNode()
		self.__Collision = obj.get_cNode()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Nodes(self, iNode, kNode, cNode):
		"""
		:meta private:
		"""
		self.__Image 	= iNode
		self.__Kinetics = kNode
		self.__Collision= cNode
