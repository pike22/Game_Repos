
class Collision_Logic2():
	def __init__(self):
		self.__collision = []
		self.__obj_Col	 = []
		self.__Corners 	 = []
		self.__tag_list  = []
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
	def Is_Collision(self, item):
		self.__collision = []
		self.__obj_Col	 = []
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
			# print(self.__collision, 'Colliding')

			self.__IsCollision = True
			for item in range(len(self.__collision)):
				if item == 0:
					tagOrId = self.__collision[item]
					obj1	= self.__Col_Dict[tagOrId]
					self.__health1, attack1, defense1 = obj1.get_Params()
				elif item == 1:
					tagOrId = self.__collision[item]
					obj2	= self.__Col_Dict[tagOrId]
					self.__health2, attack2, defense2 = obj2.get_Params()

			# if obj1.get_ID() ==

			self.__health1 -= attack2
			print(obj1.get_ID(), 'has', self.__health1, 'health')
			obj1.set_health(self.__health1)



			# for item in range(len(self.__collision)):
			# 	result = self.use_Col_Dict(self.__collision[item])
			# 	self.__obj_Col.append(result)

			# return self.__obj_Col
			# return self.__IsCollision#, self.__collision
		else:
			self.__IsCollision = False
			# return None
			# return self.__IsCollision#, None


		'''#_Collision Process_#'''
	# def Collision_Process(self, ):
	# 	for item in range(len(self.__obj_Col)):
	# 		obj = self.__obj_Col[item]
	# 		health1, attack1, defense1 = obj.get_Params()


		pass


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
