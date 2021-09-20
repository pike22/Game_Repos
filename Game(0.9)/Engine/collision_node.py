#still haven't decided if I want to use this or not

from .node import Node
from .collision_logic2 import Collision_Logic2

class Collision_Node(Node):
	def __init__(self):
		Node.__init__(self)
		self.__logic = Collision_Logic2()
		# self.__object1 = None
		# self.__object2 = None


		#_Idea 1_#
	#Capitalise on the ability of the object
	#use the col_obj to gather group ids of everything and use that to compair for ease of use

		#_Idea 2_#
	#this needs to go into the collision logic to have access to the col_dict

	#this will code for 1-to-1 Collision, No more
	# def Setting_Params(self, Col_Obj, item):
	# 	if item == 0:
	# 		self.__object1 = Col_Obj.get_Params()
	# 	elif item == 1:
	# 		self.__object2 = Col_Obj.get_Params()
	#
	# def Calc_Params(self):
	# 	health1, attack1, defense1 = self.__object1
	# 	health2, attack2, defense2 = self.__object2




	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	#def get_...


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
