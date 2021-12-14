
def Side_Calc(self, mainOBJ):
	objA  = None
	objB  = None
	objC  = None
	self.__sideResult = []
	for item in range(len(self.__CollideList)):
		if item == 0:
			objA = self.__CollideList[item]
			# print(objA, "objA")

		elif item == 1:
			objB = self.__CollideList[item]
			# print(objB, 'objB')

		elif item == 2:
			objC = self.__CollideList[item]
			# print(objC, 'objC')
		else:
			print("ERROR: CL#142" , str(len(self.__CollideList)), "obj in collision")

	self.objParameters(objA, objB, objC)


	# print(self.__xA, 'coordx objA')
	# print(self.__yA, 'coordy objA')
	# print(self.__hA, 'height objA')
	# print('--------------------------------------------')
	# print(self.__xB, 'coordx objB')
	# print(self.__yB, 'coordy objB')
	# print(self.__hB, 'height objB')
	# print('--------------------------------------------')
	# if objC != None:
	# 	print(self.__xC, 'coordx objC')
	# 	print(self.__yC, 'coordy objC')
	# 	print(self.__hC, 'height objC')
	# 	print('--------------------------------------------')
	if (self.__yA+self.__hA) <= self.__yB+(self.__yB*0.02):
		if objC != None:
			if (self.__xA+self.__hA) <= self.__yC+(self.__yC*0.02):
				# print('top 2')
				self.__sideResult.append('top')
		# print('top 1')
		self.__sideResult.append('top')
	elif (self.__yB+self.__hB) <= self.__yA+(self.__yA*0.02):
		if objC != None:
			if (self.__yC+self.__hC) <= self.__yA+(self.__yA*0.02):
				# print('bottom 2')
				self.__sideResult.append('bottom')
		# print('bottom 1')
		self.__sideResult.append('bottom')
	else:
		if self.__xA > self.__xB:
			# print('right')
			self.__sideResult.append('right')
		elif objC != None:
			if self.__xA > self.__xC:
				# print('right')
				self.__sideResult.append('right')
		elif self.__xA < self.__xB:
			# print('left')
			self.__sideResult.append('left')
		elif objC != None:
			if self.__xA < self.__xC:
				# print('left')
				self.__sideResult.append('left')
	print('-----------------result---------------------\n', self.__sideResult, '\n--------------------------------------------')
	return self.__sideResult

def objParameters(self, objA, objB, objC):
	"""Object A's coords/size"""
	if objA != None:
		self.__xA, self.__yA = objA.get_Coords()
		self.__hA, self.__wA = objA.get_size()
		# print(objA.get_ID(), 'ID?')

	"""Object B's coords/size"""
	if objB != None:
		self.__xB, self.__yB = objB.get_Coords()
		self.__hB, self.__wB = objB.get_size()
		# print(objB.get_ID(), 'ID?')

	"""Object C's coords/size"""
	if objC != None:
		self.__xC, self.__yC = objC.get_Coords()
		self.__hC, self.__wC = objC.get_size()
		# print(objC.get_ID(), 'ID?')

	"""Objects Area"""
	if objA != None:
		self.__areaA = self.__hA * self.__wA
	if objB != None:
		self.__areaB = self.__hB * self.__wB
	if objC != None:
		self.__areaC = self.__hC * self.__wC
