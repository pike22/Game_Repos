#still haven't decided if I want to use this or not

from .node import Node
from .collision_logic import Collision_Logic

#use this for the games loop collision
class Collision_Node(Node):
	"""
	The display side of collision is handled here.
	"""
	def __init__(self, clNode):
		Node.__init__(self)
		self.__logic = clNode

		#different obj needed for collision node
		self.__stalfosRoster = None
		self.__cpstalfosRost = None
		self.__playerRoster  = None
		self.__staticRoster	 = None
		self.__weaponRoster	 = None
		self.__enemyRoster	 = None
		self.__wallRoster	 = None
		self.__projRoster	 = None

		#COllision Result save
		self.__Result  = None
		self.__tempVar = None
		self.__wallHIT = None


	def use_Collision(self, cornerList, totItemCount):
		"""
		Takes the list of corners and loops to find any overlapping using the Collision logic function 'Is_Collision'.
		This then uses the returning info to figure out who is overlapping and what to do with that overlapping.
		EX: Two objects collide, player and an enemy, with that we know take that and tell to player to get knocked back because contact damage.

		Parameters
		----------
		cornerList : list
			List of corners to be processed.
		totItemCount : int
			Total number of entities, weaponry, and projectiles on screen
		"""
		self.__logic.add_Collision(listofCorners=cornerList)

		self.__Result = None
		for loopCount in range(totItemCount):
			self.__Result = self.__logic.Is_Collision(loopCount)
			# print('-----------', loopCount, '---------:TIME THROUGH LOOP')
			# print(cornerList[loopCount], loopCount,"'s item corner")

			# if self.__Result != []:
			# 	print('--------------------------------------')
			# 	print("-------------'result'-----------------")
			# 	print(self.__Result)
			# 	print('--------------------------------------')


			"""Col_Dict = self.__logic.get_Col_Dict() #this may not be needed"""
			if self.__Result != []:
				for item in range(len(self.__Result)):
					# print('\titem:', item)
					# print('\ttag: ', self.__Result[item].get_ID())
					# print('----------------------')

					"""#__# PLAYER COL_LOGIC #__#"""
					if self.__Result[item].get_ID() in self.__playerRoster:
						side = self.__logic.Side_Calc(self.__Result[item])
						if len(self.__Result) >= 2:
							if item == 0:
								if self.__Result[item+1].get_group_ID() in self.__weaponRoster:
									self.__Result[item+1].del_item()
								elif self.__Result[item+1].get_group_ID() in self.__staticRoster:
									self.__Result[item].my_Collision(OSC='Static', side=side)
							else:
								if self.__Result[item-1].get_group_ID() in self.__enemyRoster:
									self.__Result[item].my_Collision(OSC='Enemy', OSA=self.__Result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)

					"""#__# STALFOS COL_LOGIC #__#"""
					if self.__Result[item].get_ID() in self.__stalfosRoster:
						side = self.__logic.Side_Calc(self.__Result[item])
						# print('stalfos direction:', side)
						# print(len(self.__Result))
						if len(self.__Result) >= 2:
							if item == 0:
								if self.__Result[item+1].get_group_ID() in self.__staticRoster:
									self.__Result[item].my_Collision(OSC='Static', side=side)
									self.__wallHIT = True
									# print(self.__wallHIT)
							elif item == 1:
								if self.__Result[item-1].get_group_ID() in self.__weaponRoster:
									self.__Result[item].my_Collision(OSC="Weapon", OSA=self.__Result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
								elif self.__Result[item-1].get_group_ID() in self.__projRoster:
									self.__Result[item].my_Collision(OSC="Weapon", OSA=self.__Result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
									self.__Result[item-1].del_Proj()
								elif self.__Result[item-1].get_group_ID() in self.__enemyRoster:
									self.__Result[item].my_Collision(OSC='Friend', side=side)

					if self.__Result[item].get_ID() in self.__cpstalfosRost:
						side = self.__logic.Side_Calc(self.__Result[item])
						# print('stalfos direction:', side)
						# print(len(self.__Result))
						if len(self.__Result) >= 2:
							if item == 0:
								if self.__Result[item+1].get_group_ID() in self.__staticRoster:
									self.__Result[item].my_Collision(OSC='Static', side=side)
									self.__wallHIT = True
									# print(self.__wallHIT)
							elif item == 1:
								if self.__Result[item-1].get_group_ID() in self.__weaponRoster:
									self.__Result[item].my_Collision(OSC="Weapon", OSA=self.__Result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
								elif self.__Result[item-1].get_group_ID() in self.__projRoster:
									self.__Result[item].my_Collision(OSC="Weapon", OSA=self.__Result[item-1].get_attack(), side=side, staticsList=self.__staticRoster)
									self.__Result[item-1].del_Proj()
								elif self.__Result[item-1].get_group_ID() in self.__enemyRoster:
									self.__Result[item].my_Collision(OSC='Friend', side=side)

					"""#__# WEAPON COL_LOGIC #__#"""
					if self.__Result[item] == self.__logic.tagToObj('W#S001'): #weapon will always be last
						#print('Sword')
						pass
					if self.__Result[item] == self.__logic.tagToObj('W#B001'):
						#print('Bow')
						pass

					"""#__# STATIC COL_LOGIC #__#"""
					if self.__Result[item].get_ID() in self.__wallRoster:
						if len(self.__Result) >= 2:
							if item == 0:
								# print('hell0')
								pass
							elif item == 1:
								# print('goodbye')
								# print(self.__Result[item].get_ID(), 'item:',item)
								if self.__Result[item-1].get_group_ID() in self.__weaponRoster:
									print('CLANG!!!!!')
								if self.__Result[item-1].get_group_ID() in self.__projRoster:
									self.__Result[item-1].del_Proj()
							else:
								# print('wut the CN#101')
								pass
		# print('--------------------------------------')



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_playerRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__playerRoster
	#
	# def get_enemyRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__enemyRoster
	#
	# def get_stalfosRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__stalfosRoster
	#
	# def get_weaponRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__weaponRoster
	#
	# def get_projRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__projRoster
	#
	# def get_staticRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__staticRoster
	#
	# def get_wallRoster(self):
	# 	"""
	# 	:meta private:
	# 	"""
	# 	return self.__wallRoster

	def get_wallHIT(self):
		"""
		:meta private:
		"""
		return self.__wallHIT



	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_playerRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__playerRoster = Roster
		self.__logic.set_playerRoster(Roster)

	def set_enemyRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__enemyRoster = Roster
		self.__logic.set_enemyRoster(Roster)

	def set_stalfosRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__stalfosRoster = Roster
		self.__logic.set_stalfosRoster(Roster)

	def set_cpstalfosRost(self, Roster):
		"""
		:meta private:
		"""
		self.__cpstalfosRost = Roster
		self.__logic.set_cpstalfosRost(Roster)

	def set_weaponRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__weaponRoster = Roster
		self.__logic.set_weaponRoster(Roster)

	def set_projRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__projRoster = Roster
		self.__logic.set_projRoster(Roster)

	def set_staticRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__staticRoster = Roster
		self.__logic.set_staticRoster(Roster)

	def set_wallRoster(self, Roster):
		"""
		:meta private:
		"""
		self.__wallRoster = Roster
		self.__logic.set_wallRoster(Roster)
