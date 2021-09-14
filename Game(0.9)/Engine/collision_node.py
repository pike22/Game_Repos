from .node import Node

class Collision_Node(Node):
	def __init__(self):
		Node.__init__(self)
		pass

	def Func_A(self): #name this latter.
		#the goal of this func is to take in the entities that are under collision.
			#first gather basic params from each
				#-- Health, Deffence, Damage.
			#second manipulate the params based on the senario.
				#-- for now this just means if Player collide with Stalfos
				#-- Player losses health based on Stalfos's dmg param
				#-- focus on basic Idea, worry about Deffence later 
		pass
