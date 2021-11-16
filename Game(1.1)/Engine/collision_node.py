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


	def use_Collision(self, cornerList, totItemCount):
		self.__logic.add_Collision(cornerList)

		for item in range(totItemCount):
			result = self.__logic.Is_Collision(item)

			"""Col_Dict = self.__logic.get_Col_Dict() #this may not be needed"""
			if result != None:
				for item in range(len(result)):
					# print('obj', result[item])

					"""#__# PLAYER COL_LOGIC #__#"""
					if result[item] == self.__logic.tag_to_obj('P#001'): #player is always checked first
						side = self.__logic.Side_Calc()
						# print('Player direction:', side)
						if result[item+1].get_group_ID() in self.__enemyRoster:
							self.__logic.tag_to_obj('P#001').my_Collision(OSC='Enemy', OSA=result[item+1].get_attack(), side=side)
						elif result[item+1].get_group_ID() in self.__weaponRoster:
							result[item+1].del_item()
						elif result[item+1].get_group_ID() in self.__staticRoster:
							self.__logic.tag_to_obj('P#001').my_Collision(OSC='Static', side=side)

					"""#__# STALFOS COL_LOGIC #__#"""
					if result[item].get_ID() in self.__stalfosRoster:
						if item == len(result)-1:
							pass
						elif item != len(result)-1:
							if result[item+1].get_group_ID() in self.__weaponRoster:
								print(result[item+1], 'Collision Result')
								result[item].my_Collision(OSC="Weapon", OSA=result[item+1].get_attack())
							elif result[item+1].get_group_ID() in self.__projRoster:
								print(result[item+1], 'Collision Result')
								result[item].my_Collision(OSC="Weapon", OSA=result[item+1].get_attack())
								result[item+1].del_Proj()

					"""#__# WEAPON COL_LOGIC #__#"""
					if result[item] == self.__logic.tag_to_obj('W#S001'): #weapon will always be last
						#print('Sword')
						pass
					if result[item] == self.__logic.tag_to_obj('W#B001'):
						#print('Bow')
						pass

					"""#__# STATIC COL_LOGIC #__#"""
					if result[item] == self.__logic.tag_to_obj('W#001'):
						if item == len(result)-1:
							pass
						elif item != len(result)-1:
							if result[item+1].get_group_ID() in self.__projRoster:
								result[item+1].del_Proj()



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
