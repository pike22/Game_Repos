import re
from .image_node import Image_Node

class Collision_Logic():
	"""
	The Logic side of collision is handled here.
	"""
	def __init__(self, statics):
		self.__LVD_Corners	= []
		self.__CollideList	= []
		self.__collision 	= []
		self.__Corners 	 	= []
		self.__Col_Dict  	= {}
		self.__isCollision = False

		#vars for statics
		self.__wallRoster = []
		self.__Statics = statics
		self.__keyA = None
		self.__keyB = None

		#Roster Vars
		self.__stalfosRoster = None
		self.__cpstalfosRost = None
		self.__playerRoster  = None
		self.__staticRoster	 = None
		self.__weaponRoster	 = None
		self.__enemyRoster	 = None
		self.__wallRoster	 = None
		self.__projRoster	 = None

		#obj Parameters
		self.__sideResult = []
		self.__mainOBJ 	  = None
		self.__objA		  = None
		self.__objB		  = None
		self.__objC		  = None
		self.__objD		  = None
		"""OBJECT COORDS"""
		self.__xM, self.__yM = None, None
		self.__xA, self.__yA = None, None
		self.__xB, self.__yB = None, None
		self.__xC, self.__yC = None, None
		"""OBJECT  SIZE"""
		self.__hM, self.__wM = None, None
		self.__hA, self.__wA = None, None
		self.__hB, self.__wB = None, None
		self.__hC, self.__wC = None, None

		#rand var
		self.__Cur_Square = None
		self.__GRID = None
		self.tempL  = []

	'''#_COLLISION DICTIONARY FUNCTIONS_#'''
	#tagOrId == dictionary key
	#object == The keys related class object
	def addColDict(self, tagOrId, obj):
		"""
		Adds an object to the possible collisions dictionary

		Parameters
		----------
		tagOrId : str
			The tag to be used as the key in the Collision Dictionary.
		obj
			The tags class stored as the object in the Collision Dictionary.
		"""
		self.__Col_Dict[tagOrId] = obj

	def delColDict(self, tagOrId):
		"""
		Deletes an object from the possible collisions dictionary.

		Parameters
		----------
		tagOrId : str
			The key and coresponding object to be deleted.
		"""
		del self.__Col_Dict[tagOrId]

	def tagToObj(self, tagOrId):
		"""
		Takes the given tag and returns the object.

		Parameters
		----------
		tagOrId : str
			Given key to return coresponding object.
		"""
		#output == tag's object
		output = self.__Col_Dict[tagOrId]
		return output

	def objToTag(self, obj):
		"""
		Takes the given object and return the key.

		Parameters
		----------
		obj
			Given object to return coresponding key.
		"""
		for key, object in self.__Col_Dict.items():
			if obj == object:
				return key

	def listOfKeys(self):
		"""
		Returns list of keys in the Collision Dictionary.
		"""
		newList = []
		for key in self.__Col_Dict.keys():
			newList.append(key)
		return newList

	def printColDict(self):
		"""
		:meta private:
		"""
		print('Current Collision Dict', self.__Col_Dict)

	'''#_COLLISON CALCULATION FUNCTIONS_#'''
	def add_Collision(self, listofCorners=None, LVD_Corner=None):
		"""
		Combines lists of corners together to be tested for overlapping.

		Parameters
		----------
		listofCorners
			List of Corners to be tested for collision.
		LVD_Corner
			List of Corners to be tested for collision from the level designer.
		"""
		if listofCorners != None:
			self.tempL = []
			for item in range(len(listofCorners)):
				self.tempL.append(listofCorners[item])

		if LVD_Corner != None:
			self.__LVD_Corners.append(LVD_Corner)

		self.__Corners = self.tempL + self.__LVD_Corners


	def ForT_Collision(self, targOBJ=None, x1=None, y1=None, x2=None, y2=None):
		"""
		A simple test function to see if a spacific set of coordinates are overlapping with anything else.
		Returns a list of objects that collide with the given corners.

		Parameters
		----------
		targOBJ : Class Object
			This is used to find the corners of the specified object.
		x1, y1, x2, y2 : tuple int
			Is used to find overlapping in spacific box when the class object isn't avalible.
		"""
		if targOBJ != None:
			x1, y1, x2, y2 = targOBJ.get_Corners()
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)
		# print(collision, 'ForT Collision')
		if len(collision) > 1:
			self.__CollideList = []
			self.__collision   = []
			for count in range(len(collision)):
				# print('item:', item, 'CL#113')
				tag = Image_Node.Render.gettags(collision[count])
				# print(tag, 'tag CL#100')
				self.__collision.append(tag[0])
			# print(self.__collision, 'Colliding') #print Tags of Entity Colliding

			self.oldList = self.__collision
			self.__collision = []
			for count in range(len(self.oldList)-1, -1, -1):
				tagOrId = self.oldList[count]
				if tagOrId not in self.__wallRoster:
					self.__collision.append(tagOrId)
				elif tagOrId in self.__wallRoster and self.__collision != []:
					self.__collision.append(tagOrId)
			# print(self.__collision, 'new Colliding') #print Tags of Entity Colliding


			for count in range(len(self.__collision)):
				tagOrId = self.__collision[count]
				obj = self.__Col_Dict[tagOrId]
				# print(obj.get_Coords(), tagOrId, 'objCoords')
				self.__CollideList.append(obj)

			self.__isCollision = True
			# print(self.__CollideList, 'objList')
			return self.__CollideList

	#use this: .find_overlapping
	# only outputs the last assigned var.
	def Is_Collision(self, item):
		"""
		Is used to compile every entity on screen to see if any of them are collisiding.

		Parameters
		----------
		item
			the nth iteration of a loop
		"""
		# print(item)
		if item == 0:
			self.__CollideList = []
			self.__collision   = []


		x1, y1, x2, y2 = self.__Corners[item]
		# print(self.__Corners[item])
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)


		#this only shows what is colliding.
		if len(collision) > 1:
			self.__CollideList = []
			self.__collision   = []
			for count in range(len(collision)):
				# print('item:', item, 'CL#113')
				tag = Image_Node.Render.gettags(collision[count])
				# print(tag, 'tag CL#115')
				self.__collision.append(tag[0])
			# print(self.__collision, 'Colliding') #print Tags of Entity Colliding

			self.oldList = self.__collision
			self.__collision = []
			for count in range(len(self.oldList)-1, -1, -1):
				tagOrId = self.oldList[count]
				if tagOrId not in self.__wallRoster:
					self.__collision.append(tagOrId)
				elif tagOrId in self.__wallRoster and self.__collision != []:
					self.__collision.append(tagOrId)
			# print(self.__collision, 'new Colliding') #print Tags of Entity Colliding


			for count in range(len(self.__collision)):
				tagOrId = self.__collision[count]
				obj = self.__Col_Dict[tagOrId]
				# print(obj.get_Coords(), tagOrId, 'objCoords')
				self.__CollideList.append(obj)



			self.__isCollision = True
			# print(self.__CollideList, 'objList')
			return self.__CollideList
		else:
			self.__isCollision = False
			return []

	#I want to use this to purly find where objects are in relation to others and push
	#the opposite direction through so that I can do proper knockback/wall collision
	def Side_Calc(self, mainOBJ):
		"""
		This is used to determin what side the main object is acting on the secondary object.

		Parameters
		----------
		mainOBJ
			The object that is used as the base point and returns wich side of the other object the main one is overlapping with.
		"""
		self.__mainOBJ = mainOBJ
		self.__xM, self.__yM = mainOBJ.get_Coords()
		self.__hM, self.__wM = mainOBJ.get_size()


		self.__mainSQ = self.Find_Square(self.__xM+(self.__wM/2), self.__yM+(self.__hM/2))
		self.tempL = []
		self.tempL.append(self.__mainOBJ)
		if len(self.__CollideList) >= 3:
			for obj in self.__CollideList:
				if obj != self.__mainOBJ:
					if self.__mainSQ != None:
						if obj.get_Coords()[0] == self.__GRID[self.__mainSQ][0]:
							if obj.get_Coords()[1] == (self.__GRID[self.__mainSQ][1]-32):
								# print(obj.get_ID(), 'bottom side')
								self.tempL.append(obj)
						if obj.get_Coords()[0] == self.__GRID[self.__mainSQ+1][0]:
							if obj.get_Coords()[1] == self.__GRID[self.__mainSQ+1][1]:
								# print(obj.get_ID(), 'top side')
								self.tempL.append(obj)
						if obj.get_Coords()[0] == (self.__GRID[self.__mainSQ][0]-32):
							if obj.get_Coords()[1] == self.__GRID[self.__mainSQ][1]:
								# print(obj.get_ID(), 'right side')
								self.tempL.append(obj)
						if obj.get_Coords()[0] == (self.__GRID[self.__mainSQ][0]+32):
							if obj.get_Coords()[1] == self.__GRID[self.__mainSQ][1]:
								# print(obj.get_ID(), 'left side')
								self.tempL.append(obj)
					else:
						self.__mainSQ = self.Find_Square((self.__xM+(self.__wM/2)+1), (self.__yM+(self.__hM/2)+1))
						if self.__mainSQ != None:
							if obj.get_Coords()[0] == self.__GRID[self.__mainSQ][0]:
								if obj.get_Coords()[1] == (self.__GRID[self.__mainSQ][1]-32):
									# print(obj.get_ID(), 'bottom side2')
									self.tempL.append(obj)
							if obj.get_Coords()[0] == self.__GRID[self.__mainSQ+1][0]:
								if obj.get_Coords()[1] == self.__GRID[self.__mainSQ+1][1]:
									# print(obj.get_ID(), 'top side2')
									self.tempL.append(obj)
							if obj.get_Coords()[0] == (self.__GRID[self.__mainSQ][0]-32):
								if obj.get_Coords()[1] == self.__GRID[self.__mainSQ][1]:
									# print(obj.get_ID(), 'right side2')
									self.tempL.append(obj)
							if obj.get_Coords()[0] == (self.__GRID[self.__mainSQ][0]+32):
								if obj.get_Coords()[1] == self.__GRID[self.__mainSQ][1]:
									# print(obj.get_ID(), 'left side2')
									self.tempL.append(obj)


			# print(self.__CollideList, 'list 1')
			self.__CollideList = []
			self.__CollideList = self.tempL
			# print(self.__CollideList, 'list 2')


		#Clears the object variables
		self.__objA = None
		self.__objB = None
		self.__objC = None
		self.__objD = None
		for item in range(len(self.__CollideList)):
			#this is object A
			if item == 0:
				if self.__CollideList[0] != self.__mainOBJ:
					self.__objA = self.__CollideList[0]
					self.__xA, self.__yA = self.__CollideList[0].get_Coords()
					self.__hA, self.__wA = self.__CollideList[0].get_size()
				else:
					self.__objA = None
			#this is object B
			elif item == 1:
				if self.__CollideList[1] != self.__mainOBJ:
					self.__objB = self.__CollideList[1]
					self.__xB, self.__yB = self.__CollideList[1].get_Coords()
					self.__hB, self.__wB = self.__CollideList[1].get_size()
				else:
					self.__objB = None
			#this is object C
			elif item == 2:
				if self.__CollideList[2] != self.__mainOBJ:
					self.__objC = self.__CollideList[2]
					self.__xC, self.__yC = self.__CollideList[2].get_Coords()
					self.__hC, self.__wC = self.__CollideList[2].get_size()
				else:
					self.__objC = None
			#this is object D
			elif item == 3:
				if self.__CollideList[3] != self.__mainOBJ:
					self.__objD = self.__CollideList[3]
					self.__xD, self.__yD = self.__CollideList[3].get_Coords()
					self.__hD, self.__wD = self.__CollideList[3].get_size()
				else:
					self.__objD = None

		# self.objPRINTOUT()
		#checks which collision objects are used and "returns" the individual squares collision direction
		self.__sideResult = []
		self.__resultTAG  = []
		"""mainOBJ vs. objA"""
		if self.__objA != None:
			# print(self.__objA, ':objA', self.__objA.get_ID(), ':tagA')
			if (self.__yM+self.__hM) <= self.__yA+(self.__hA*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objA.get_ID())
			elif (self.__yA+self.__hA) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objA.get_ID())
			else:
				if self.__xM > self.__xA:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objA.get_ID())
				elif self.__xM < self.__xA:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objA.get_ID())

		"""mainOBJ vs. objB"""
		if self.__objB != None:
			# print(self.__objB, ':objB', self.__objB.get_ID(), ':tagB')
			if (self.__yM+self.__hM) <= self.__yB+(self.__hB*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objB.get_ID())
			elif (self.__yB+self.__hB) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objB.get_ID())
			else:
				if self.__xM > self.__xB:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objB.get_ID())
				elif self.__xM < self.__xB:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objB.get_ID())

		"""mainOBJ vs. objC"""
		if self.__objC != None:
			# print(self.__objC, ':objC', self.__objC.get_ID(), ':tagC')
			if (self.__yM+self.__hM) <= self.__yC+(self.__hC*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objB.get_ID())
			elif (self.__yC+self.__hC) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objB.get_ID())
			else:
				if self.__xM > self.__xC:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objB.get_ID())
				elif self.__xM < self.__xC:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objB.get_ID())

		"""mainOBJ vs. objD"""
		if self.__objD != None:
			# print(self.__objD, ':objD', self.__objD.get_ID(), ':tagD')
			if (self.__yM+self.__hM) <= self.__yD+(self.__hD*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objD.get_ID())
			elif (self.__yD+self.__hD) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objD.get_ID())
			else:
				if self.__xM > self.__xD:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objD.get_ID())
				elif self.__xM < self.__xD:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objD.get_ID())

		# print(
		# 	'---------------Direction off of Wall---------------\n',
		# 	self.__sideResult, '\t:Given To', self.__mainOBJ.get_ID(), '\n',
		# 	self.__resultTAG,  '\t:Given By', '\n',
		# 	'---------------------------------------------------\n'
		# 	 )
		return self.__sideResult


	def objPRINTOUT(self):
		"""
		:meta private:
		"""
		print(self.__mainOBJ.get_ID(), 'ID')
		print(self.__xM, 'coordx mainOBJ')
		print(self.__yM, 'coordy mainOBJ')
		print(self.__hM, 'height mainOBJ')
		print('--------------------------------------------')
		if self.__objA != None:
			print(self.__objA.get_ID(), 'ID')
			print(self.__xA, 'coordx objA')
			print(self.__yA, 'coordy objA')
			print(self.__hA, 'height objA')
			print('--------------------------------------------')
		if self.__objB != None:
			print(self.__objB.get_ID(), 'ID')
			print(self.__xB, 'coordx objB')
			print(self.__yB, 'coordy objB')
			print(self.__hB, 'height objB')
			print('--------------------------------------------')
		if self.__objC != None:
			print(self.__objC.get_ID(), 'ID')
			print(self.__xC, 'coordx objC')
			print(self.__yC, 'coordy objC')
			print(self.__hC, 'height objC')
			print('--------------------------------------------')
		if self.__objD != None:
			print(self.__objD.get_ID(), 'ID')
			print(self.__xD, 'coordx objD')
			print(self.__yD, 'coordy objD')
			print(self.__hD, 'height objD')
			print('--------------------------------------------')


	def Find_Square(self, x, y):
		"""
		Finds the square that the mouse is in.

		Parameters
		----------
		x : int
			The x cord of my mouse.
		y : int
			The y cord of my mouse.
		"""
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__GRID)):
			if x > self.__GRID[item][0] and y > self.__GRID[item][1]:
				if x < self.__GRID[item][2] and y < self.__GRID[item][3]:
					self.__Cur_Square = item
					return self.__Cur_Square



	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Col_Dict(self):
		"""
		:meta private:
		"""
		return self.__Col_Dict

	def get_isCollision(self):
		"""
		:meta private:
		"""
		return self.__isCollision

	def get_CollideList(self):
		"""
		:meta private:
		"""
		return self.__CollideList

	def reset_objList(self):
		"""
		:meta private:
		"""
		self.__CollideList = []


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_playerRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__playerRoster = Roster

	def set_enemyRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__enemyRoster = Roster

	def set_cpstalfosRost(self, Roster):
		"""
		:meta private:
		"""
		self.__cpstalfosRost = Roster

	def set_stalfosRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__stalfosRoster = Roster

	def set_weaponRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__weaponRoster = Roster

	def set_projRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__projRoster = Roster

	def set_staticRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__staticRoster = Roster

	def set_wallRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__wallRoster = Roster

	def set_grid(self, grid):
		"""
		:meta private:
		"""
		self.__GRID = grid
