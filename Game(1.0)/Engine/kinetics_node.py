#This class is to allow for movement to a given object/entity.

from .node import Node

class Kinetics_Node(Node):
	def __init__(self, iNode):
		Node.__init__(self)
		self.__Speed = None
		self.__Image = iNode
		self.__Render = None


	def kinetics(self, Cur_Coords, img_ID, direction):
		x, y = Cur_Coords
		if direction == 'left':
			x -= 1 * self.__Speed
		if direction == 'right':
			x += 1 * self.__Speed
		if direction == 'up':
			y -= 1 * self.__Speed
		if direction == 'down':
			y += 1 * self.__Speed

		self.__Render.coords(img_ID, x, y)
		return (x, y)

	def Knock_Back(self, Cur_Coords, img_ID, direction):#eventually impliment directional based knock back
		x, y = Cur_Coords
		if direction == 'left':
			x -= 50
		elif direction == 'right':
			x += 50
		else:
			x += 100
		return (x, y)


	#special types of movement may be implimented later
	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Speed(self):
		return self.__Speed


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Speed(self, Speed):
		self.__Speed = Speed

	def set_Render(self, render):
		self.__Render = render
