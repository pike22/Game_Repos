#still haven't decided if I want to use this or not

from .node import Node
from .collision_logic import Collision_Logic

#use this for the games loop collision
class Collision_Node(Node):
	def __init__(self, clNode):
		Node.__init__(self)
		self.__logic = clNode

		#different obj needed for collision node
		self.__stalfosRoster = None
		self.__staticRoster	 = None
		self.__weaponRoster	 = None
		self.__enemyRoster	 = None
		self.__projRoster	 = None

		#COllision Result save
		self.__Result = None
		self.__tempVar= None


	def use_Collision(self, cornerList, totItemCount):
		self.__logic.add_Collision(cornerList)

		self.__Result = None
		for item in range(totItemCount):
			self.__Result = self.__logic.Is_Collision(item)
			# print('-----------', item, '---------:TIME THROUGH LOOP')
			# print(cornerList[item], item,"'s item corner")

		# print('--------------------------------------')
		# print("-------------'result'-----------------")
		# print(self.__Result,'result')
		# print('--------------------------------------')


		"""Col_Dict = self.__logic.get_Col_Dict() #this may not be needed"""
		if self.__Result != None:
			for item in range(len(self.__Result)):
				print('item:', item)
				print('obj', self.__Result[item])
				print('--')

				"""#__# PLAYER COL_LOGIC #__#"""
				if self.__Result[item] == self.__logic.tagToObj('P#001'): #player is always checked first
					side = self.__logic.Side_Calc()
					# print('Player direction:', side)
					if self.__Result[item+1].get_group_ID() in self.__enemyRoster:
						self.__logic.tagToObj('P#001').my_Collision(OSC='Enemy', OSA=self.__Result[item+1].get_attack(), side=side)
					elif self.__Result[item+1].get_group_ID() in self.__weaponRoster:
						self.__Result[item+1].del_item()
					elif self.__Result[item+1].get_group_ID() in self.__staticRoster:
						self.__logic.tagToObj('P#001').my_Collision(OSC='Static', side=side)

				"""#__# STALFOS COL_LOGIC #__#"""
				if self.__Result[item].get_ID() in self.__stalfosRoster:
					if item == len(self.__Result)-1:
						pass
					elif item != len(self.__Result)-1:
						if self.__Result[item+1].get_group_ID() in self.__weaponRoster:
							print(self.__Result[item+1], 'Collision Result')
							self.__Result[item].my_Collision(OSC="Weapon", OSA=self.__Result[item+1].get_attack())
						elif self.__Result[item+1].get_group_ID() in self.__projRoster:
							print(self.__Result[item+1], 'Collision Result')
							self.__Result[item].my_Collision(OSC="Weapon", OSA=self.__Result[item+1].get_attack())
							self.__Result[item+1].del_Proj()

				"""#__# WEAPON COL_LOGIC #__#"""
				if self.__Result[item] == self.__logic.tagToObj('W#S001'): #weapon will always be last
					#print('Sword')
					pass
				if self.__Result[item] == self.__logic.tagToObj('W#B001'):
					#print('Bow')
					pass

				"""#__# STATIC COL_LOGIC #__#"""
				if self.__Result[item] == self.__logic.tagToObj('W#001'):
					print('CN #80')
					if item == len(self.__Result)-1:
						pass
					elif item != len(self.__Result)-1:
						if self.__Result[item+1].get_group_ID() in self.__weaponRoster:
							print('CLANG!!!!!')
					elif item != len(self.__Result)-1:
						print('hell0?')
						if self.__Result[item+1].get_group_ID() in self.__projRoster:
							print(self.__Result[item+1], 'Collision Result')
							self.__Result[item+1].del_Proj()
		# print('--------------------------------------')



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	#def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
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
