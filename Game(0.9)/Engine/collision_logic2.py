
class Collision_Logic2():
	def __init__(self):
		self.__collision = []
		self.__Corners 	 = []
		self.__tag_list  = []
		self.__obj_list	 = []
		self.__key_list	 = []
		self.__Col_Dict  = {}
		self.__list_len	 = 0
		self.__Render	 = None
		self.__IsCollision = False

		'''#_Parameter Math Var_#'''
		self.__health1 = 0
		self.__health2 = 0


	'''#_COLLISION DICTIONARY FUNCTIONS_#'''
	#tagOrId == dictionary key
	#object == The keys related class object
	def add_Col_Dict(self, tagOrId, object):
		self.__Col_Dict[tagOrId] = object

	def del_Col_Dict(self, tagOrId):
		del self.__Col_Dict[tagOrId]

	def use_Col_Dict(self, tagOrId):
		# if tagOrId in self.__Col_Dict.keys():
		# print(self.__Col_Dict[tagOrId])
		output = self.__Col_Dict[tagOrId]
		return output

	def print_Col_Dict(self):
		print('Current Collision Dict', self.__Col_Dict)

	'''#_COLLISON CALCULATION FUNCTIONS_#'''
	def add_Collision(self, listofCorners):
		self.__Corners 	= []
		self.__list_len = 0
		for item in range(len(listofCorners)):
			self.__Corners.append(listofCorners[item])
		self.__list_len = len(self.__Corners)

	#use this: .find_overlapping
	# only outputs the last assigned var.
	# LEO == List of Enemy Objects
	def Is_Collision(self, item, LEO):
		self.__collision = []
		#for item in range(len(self.__Corners)):
			#print(item, 'item')
		x1, y1, x2, y2 = self.__Corners[item]
		collision = self.__Render.find_overlapping(x1, y1, x2, y2)
			#if item == 1:
				# print(collision[0],':ID,', item, ':Item')

		#this only shows what is colliding.
		if len(collision) > 1:
			#print(collision, 'ID', )
			for item in range(len(collision)):
				tag = self.__Render.gettags(collision[item])
				self.__collision.append(tag[0]) #item 0 is the entity_ID, 1 == group_ID
			print(self.__collision, 'Colliding')

			for item in range(len(self.__collision)):
				tagOrId = self.__collision[item]
				print(tagOrId, 'tag')
				obj		= self.__Col_Dict[tagOrId]
				print(obj, 'obj')
				self.__obj_list.append(obj)

			self.__key_list = []
			for item in range(len(self.__collision)):
				tagOrId = self.__collision[item]
				for item in range(len(LEO)):
					#this will be a growing list that goes through each enemy in the roster
					#and find out if the tagOrId is in an enemy then save this for using when needed
					print(tagOrId,'tag')
					if tagOrId in LEO[item].get_ID(ALL=True):
						self.__key_list.append(tagOrId)
						print(self.__key_list, 'key list')



			self.__IsCollision = True
			return self.__obj_list, self.__key_list
			# return self.__IsCollision#, self.__collision
		else:
			self.__IsCollision = False
			return None, None
			# return self.__IsCollision#, None


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
