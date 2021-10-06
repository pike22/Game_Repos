
class Collision_Logic():
	def __init__(self):
		self.__collision = []
		self.__Corners 	 = []
		self.__tag_list  = []
		self.__obj_list	 = []
		self.__key_list	 = []
		self.__Col_Dict  = {}
		self.__Render	 = None
		self.__Direcntion = None
		self.__IsCollision = False

	'''#_COLLISION DICTIONARY FUNCTIONS_#'''
	#tagOrId == dictionary key
	#object == The keys related class object
	def add_Col_Dict(self, tagOrId, obj):
		self.__Col_Dict[tagOrId] = obj

	def del_Col_Dict(self, tagOrId):
		del self.__Col_Dict[tagOrId]

	def tag_to_obj(self, tagOrId):
		output = self.__Col_Dict[tagOrId]
		return output

	def obj_to_tag(self, obj):
		pass

	def print_Col_Dict(self):
		print('Current Collision Dict', self.__Col_Dict)

	'''#_COLLISON CALCULATION FUNCTIONS_#'''
	def add_Collision(self, listofCorners):
		self.__Corners 	= []
		for item in range(len(listofCorners)):
			self.__Corners.append(listofCorners[item])

	#use this: .find_overlapping
	# only outputs the last assigned var.
	def Is_Collision(self, item):
		self.__collision = []
		self.__obj_list  = []

		x1, y1, x2, y2 = self.__Corners[item]
		collision = self.__Render.find_overlapping(x1, y1, x2, y2)

		#this only shows what is colliding.
		if len(collision) > 1:
			for item in range(len(collision)):
				tag = self.__Render.gettags(collision[item])
				self.__collision.append(tag[0]) #item 0 is the entity_ID, 1 == group_ID
			# print(self.__collision, 'Colliding')

			for item in range(len(self.__collision)):
				tagOrId = self.__collision[item]
				obj		= self.__Col_Dict[tagOrId]
				# print(tagOrId, 'tag')
				# print(obj, 'obj')
				self.__obj_list.append(obj)

			self.__IsCollision = True
			return self.__obj_list
		else:
			self.__IsCollision = False
			return None

	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Col_Dict(self):
		return self.__Col_Dict


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Render(self, Render):
		self.__Render = Render

	def set_tag_List(self, tagOrId):
		self.__tag_list.append(tagOrId)
