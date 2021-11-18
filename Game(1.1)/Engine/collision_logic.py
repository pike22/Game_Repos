from .image_node import Image_Node

class Collision_Logic():
	def __init__(self):
		self.__collision = []
		self.__Corners 	 = []
		self.__obj_list	 = []
		self.__Col_Dict  = {}
		self.__isCollision = False

	'''#_COLLISION DICTIONARY FUNCTIONS_#'''
	#tagOrId == dictionary key
	#object == The keys related class object
	def addColDict(self, tagOrId, obj):
		self.__Col_Dict[tagOrId] = obj

	def delColDict(self, tagOrId):
		del self.__Col_Dict[tagOrId]

	def tagToObj(self, tagOrId):
		#output == tag's object
		output = self.__Col_Dict[tagOrId]
		return output

	def objToTag(self, obj):
		for key, object in self.__Col_Dict.items():
			if obj == object:
				return key

	def listOfKeys(self):
		return self.__Col_Dict.keys()

	def printColDict(self):
		print('Current Collision Dict', self.__Col_Dict)

	'''#_COLLISON CALCULATION FUNCTIONS_#'''
	def add_Collision(self, listofCorners):
		self.__Corners 	= []
		for item in range(len(listofCorners)):
			self.__Corners.append(listofCorners[item])

	def ForT_Collision(self, targOBJ):
		x1, y1, x2, y2 = targOBJ.get_Corners()
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)
		# print(collision, 'ForT Collision')

	#use this: .find_overlapping
	# only outputs the last assigned var.
	def Is_Collision(self, item):
		if item == 0:
			self.__collision = []
			self.__obj_list	 = []


		x1, y1, x2, y2 = self.__Corners[item]
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)

		#this only shows what is colliding.
		if len(collision) > 1:
			for item in range(len(collision)):
				# print('item:', item, 'CL#59')
				tag = Image_Node.Render.gettags(collision[item])
				# print(tag, 'tag CL#61')
				if self.__collision == [] or len(self.__collision) == 1:
					self.__collision.append(tag[0]) #item 0 is the entity_ID, 1 == group_ID
			# print(self.__collision, 'Colliding') #print Tags of Entity Colliding

			for item in range(len(self.__collision)):
				tagOrId = self.__collision[item]
				obj		= self.__Col_Dict[tagOrId]
				# print(obj, 'obj')
				# print(tagOrId, 'tag')
				if self.__obj_list == [] or len(self.__obj_list) == 1:
					self.__obj_list.append(obj)

			self.__isCollision = True
			print(self.__obj_list, 'objList')
			return self.__obj_list
		else:
			self.__isCollision = False
			return self.__obj_list

	def Side_Calc(self):
		objA  = None
		objB  = None
		for item in range(len(self.__obj_list)):
			if item == 0:
				objA = self.__obj_list[item]
				# print(objA, "objA")
			elif item == 1:
				objB = self.__obj_list[item]
				# print(objB, 'objB')
			else:
				print("ERROR: CL#81 '3 obj in collision'")
		"""Object A's coords/size"""
		xA, yA = objA.get_Coords()
		height_A, width_A = objA.get_size()

		"""Object B's coords/size"""
		xB, yB = objB.get_Coords()
		height_B, width_B = objB.get_size()

		"""Objects Area"""
		areaA = height_A * width_A
		areaB = height_B * width_B

		if areaA >= 5000 or areaB >= 5000: #this may need ajustments as we go
			if xA >= xB+(width_B*(9/10)):
				# print('right')
				return 'right'
			if xA <= xB-(0.5*width_A):
				# print('left')
				return 'left'
			if yA <= yB:
				# print('top')
				return 'top'
			if yB+height_B >= yA:
				# print('bottom')
				return 'bottom'
		else:
			if yA+(height_A*(3/4)) <= yB:
				# print('top')
				return 'top'
			elif (yB+height_B) <= yA:
				# print('bottom')
				return 'bottom'
			else:
				if xA > xB:
					# print('right')
					return 'right'
				elif xA < xB:
					# print('left')
					return 'left'


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Col_Dict(self):
		return self.__Col_Dict

	def get_isCollision(self):
		return self.__isCollision

	def reset_objList(self):
		self.__obj_list = []


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
