from .node import Node

class Collision_Node(Node):
	def __init__(self):
		Node.__init__(self)
		pass

	#this can be used for only 1-on-1 collision, then have a secondary for multiple at once collision.
	def Collision_Result(self, Entity_A, Entity_B): #name this latter.
		health_A, attack_A, defence_A = Entity_A
		health_B, attack_B, defence_B = Entity_B

		



		#the goal of this func is to take in the entities that are under collision.
			#first gather basic params from each
				#-- Health, Deffence, Damage.
			#second manipulate the params based on the senario.
				#-- for now this just means if Player collide with Stalfos
				#-- Player losses health based on Stalfos's dmg param
				#-- focus on basic Idea, worry about Deffence later
