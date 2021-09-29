#This class is to allow for movement to a given object/entity.

from .node import Node

class Kinetics_Node(Node):
	def __init__(self, iNode):
		Node.__init__(self)
		self.__Speed = None
		self.__Image = iNode
		self.__Render = None


	def x_Kinetics(self, Cur_Coords, img_ID, neg=True):
		x, y = Cur_Coords
		#print(x, y, 'old: (x, y)')
		if neg == True:
			x += 1 * self.__Speed
		else:
			x -= 1 * self.__Speed
		#print(x, y, 'new: (x, y)')
		#print('-----------------')
		self.__Render.coords(img_ID, x, y)
		return (x, y)
		#here will be how I move an object/entity
		#on the x axis.

	def y_Kinetics(self, Cur_Coords, img_ID, neg=True):
		x, y = Cur_Coords
		#print(x, y, 'old: (x, y)')
		if neg == True:
			y += 1 * self.__Speed
		else:
			y -= 1 * self.__Speed
		#print(x, y, 'new: (x, y)')
		#print('-----------------')
		self.__Render.coords(img_ID, x, y)
		return (x, y)
		#here will be how I move an object/entity
		#on the y axis.

	def Knock_Back(self, Cur_Coords, img_ID):#eventually impliment directional based knock back
		x, y = Cur_Coords
		x -= 50
		y -= 50


	#special types of movement may be implimented later
	"""|--------------Getters--------------|#"""
		#this is where a list of getters will
		#go...
	def get_Speed(self):
		return self.__Speed


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will
		#go...
	def set_Speed(self, Speed):
		self.__Speed = Speed

	def set_Render(self, render):
		self.__Render = render
