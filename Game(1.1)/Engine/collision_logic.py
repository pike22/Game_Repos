import re
from .image_node import Image_Node

class Collision_Logic():
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
	def add_Collision(self, listofCorners=None, LVD_Corner=None):
		if listofCorners != None:
			self.tempL = []
			for item in range(len(listofCorners)):
				self.tempL.append(listofCorners[item])

		if LVD_Corner != None:
			self.__LVD_Corners.append(LVD_Corner)

		self.__Corners = self.tempL + self.__LVD_Corners


	def ForT_Collision(self, targOBJ):
		x1, y1, x2, y2 = targOBJ.get_Corners()
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)
		# print(collision, 'ForT Collision')

	#use this: .find_overlapping
	# only outputs the last assigned var.
	def Is_Collision(self, item):
		if item == 0:
			self.__collision = []
			self.__CollideList	 = []


		x1, y1, x2, y2 = self.__Corners[item]
		collision = Image_Node.Render.find_overlapping(x1, y1, x2, y2)


		#this only shows what is colliding.
		if len(collision) > 1:
			self.__collision = []
			for item in range(len(collision)):
				# print('item:', item, 'CL#59')
				tag = Image_Node.Render.gettags(collision[item])
				# print(tag, 'tag CL#70')
				if self.__collision == [] or len(self.__collision) == 1:
					self.__collision.append(tag[0]) #item 0 is the entity_ID, 1 == group_ID
				else:
					self.__collision.append(tag[0])
			# print(self.__collision, 'Colliding') #print Tags of Entity Colliding

			self.oldList = self.__collision
			self.__collision = []
			for item in range(len(self.oldList)-1, -1, -1):
				tagOrId = self.oldList[item]
				if tagOrId not in self.__wallRoster:
					self.__collision.append(tagOrId)
				elif tagOrId in self.__wallRoster and self.__collision != []:
					self.__collision.append(tagOrId)
			print(self.__collision, 'new Colliding') #print Tags of Entity Colliding


			for item in range(len(self.__collision)):
				tagOrId = self.__collision[item]
				obj = self.__Col_Dict[tagOrId]


				if self.__CollideList == [] or len(self.__CollideList) == 1:
					self.__CollideList.append(obj)
				else:
					self.__CollideList.append(obj)


			self.__isCollision = True
			# print(self.__CollideList, 'objList')
			return self.__CollideList
		else:
			self.__isCollision = False
			return self.__CollideList

	#I want to use this to purly find where objects are in relation to others and push
	#the opposite direction through so that I can do proper knockback/wall collision
	def Side_Calc(self, mainOBJ):
		self.__mainOBJ = mainOBJ
		self.__xM, self.__yM = mainOBJ.get_Coords()
		self.__hM, self.__wM = mainOBJ.get_size()

		#Here I want to remake the self.__CollideList to only have the mainOBJ and any objects
		#directly above, below, right or left of the mainOBJ.
		#This should fix the strange edge case
		self.__mainSQ = self.Find_Square(self.__xM+(self.__hM/2), self.__yM+(self.__wM/2))
		self.tempL = []
		self.tempL.append(self.__mainOBJ)
		if len(self.__CollideList) >= 3:
			for obj in self.__CollideList:
				if obj != self.__mainOBJ:
					# objSQ = self.Find_Square(obj.get_Coords()[0]+(obj.get_size()[0]/2), obj.get_Coords()[1]+(obj.get_size()[1]/2))
					# print(obj.get_Coords())
					# print((self.__GRID[mainSQ+1][0], self.__GRID[mainSQ+1][1]))
					if self.__mainSQ != None:
						# print(  self.__GRID[self.__mainSQ+1][0], self.__GRID[self.__mainSQ+1][1],  'top\n',
						# 		self.__GRID[self.__mainSQ-1][0], self.__GRID[self.__mainSQ-1][1],  'bottom\n',
						# 		(self.__GRID[self.__mainSQ][0]-32), self.__GRID[self.__mainSQ][1], 'left\n',
						# 		(self.__GRID[self.__mainSQ][0]+32), self.__GRID[self.__mainSQ][1], 'right\n')

						if obj.get_Coords()[0] == self.__GRID[self.__mainSQ-1][0]:
							if obj.get_Coords()[1] == self.__GRID[self.__mainSQ-1][1]:
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
			# print(self.__CollideList)
			self.__CollideList = self.tempL
			# print(self.__CollideList)


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
		# print(self.__objB, 'ForT objA')
		if self.__objA != None:
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
		# print(self.__objB, 'ForT objB')
		if self.__objB != None:
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
		# print(self.__objC, 'ForT objC')
		if self.__objC != None:
			if (self.__yM+self.__hM) <= self.__yC+(self.__hC*0.2):
				self.__sideResult.append('top')
				self.__resultTAG.append(self.__objC.get_ID())
			elif (self.__yC+self.__hC) <= self.__yM+(self.__hM*0.2):
				self.__sideResult.append('bottom')
				self.__resultTAG.append(self.__objC.get_ID())
			else:
				if self.__xM > self.__xC:
					self.__sideResult.append('right')
					self.__resultTAG.append(self.__objC.get_ID())
				elif self.__xM < self.__xC:
					self.__sideResult.append('left')
					self.__resultTAG.append(self.__objC.get_ID())

		"""mainOBJ vs. objD"""
		# print(self.__objD, 'ForT objD')
		if self.__objD != None:
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


		# print('-----------------result---------------------\n', self.__sideResult, '\n', self.__resultTAG, '\n--------------------------------------------\n\n')
		return self.__sideResult


	def objPRINTOUT(self):
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
		#this is staple for when I need to know what square my mouse is in.
		for item in range(len(self.__GRID)):
			if x > self.__GRID[item][0] and y > self.__GRID[item][1]:
				if x < self.__GRID[item][2] and y < self.__GRID[item][3]:
					self.__Cur_Square = item
					return self.__Cur_Square



	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Col_Dict(self):
		return self.__Col_Dict

	def get_isCollision(self):
		return self.__isCollision

	def reset_objList(self):
		self.__CollideList = []


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_playerRoster(self, Roster):
		self.__playerRoster = Roster

	def set_enemyRoster(self, Roster):
		self.__enemyRoster = Roster

	def set_stalfosRoster(self, Roster):
		self.__stalfosRoster = Roster

	def set_weaponRoster(self, Roster):
		self.__weaponRoster = Roster

	def set_projRoster(self, Roster):
		self.__projRoster = Roster

	def set_staticRoster(self, Roster):
		self.__staticRoster = Roster

	def set_wallRoster(self, Roster):
		self.__wallRoster = Roster

	def set_grid(self, grid):
		self.__GRID = grid
