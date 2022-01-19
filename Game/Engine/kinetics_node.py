#This class is to allow for movement to a given object/entity.

from .node import Node
from .image_node import Image_Node

class Kinetics_Node(Node):
	"""
	This is where motion of objects is handled. Basic motion, knockback, and when hitting a wall or other static object.
	"""
	def __init__(self, iNode):
		Node.__init__(self)
		self.__Speed = None
		self.__Image = iNode


	def kinetics(self, Cur_Coords, img_ID, dir):
		"""
		Handles basic movement.

		Parameters
		----------
		Cur_Coords : tuple int
			The current coordinates of the entity.
		img_ID : tk/PIL image
			the image that will be manipulated with kinetics.
		dir : str
			The direction that will be traveled.
		"""
		x, y = Cur_Coords
		if dir == 'left':
			x -= 1 * self.__Speed
		if dir == 'right':
			x += 1 * self.__Speed
		if dir == 'up':
			y -= 1 * self.__Speed
		if dir == 'down':
			y += 1 * self.__Speed

		Image_Node.Render.coords(img_ID, x, y)
		return (x, y)

	def Knock_Back(self, Cur_Coords, img_ID, dir):#eventually impliment directional based knock back
		"""
		Handles Knock Back from enemies or weapons.

		Parameters
		----------
		Cur_Coords : tuple int
			The current coordinates of the entity.
		img_ID : tk/PIL image
			the image that will be manipulated with kinetics.
		dir : str
			The direction it will be knocked opposite of the side that was hit.
		"""
		x, y = Cur_Coords
		if dir == 'left':
			x -= 1
		elif dir == 'right':
			x += 1
		elif dir == 'up':
			y -= 1
		elif dir == 'down':
			y += 1
		else:
			print('NO DIRECTIONS', dir)
		Image_Node.Render.coords(img_ID, x, y)
		return (x, y)

	def Static_Hit(self, Cur_Coords, img_ID, dir):
		"""
		Handles movment when hitting a wall or other static obejcts.

		Parameters
		----------
		Cur_Coords : tuple int
			The current coordinates of the entity.
		img_ID : tk/PIL image
			the image that will be manipulated with kinetics.
		dir : str
			The direction travel opposite of the side that was hit.
		"""
		# print(Cur_Coords, 'OLD COORDS')
		x, y = Cur_Coords
		if dir == 'left':
			x -= 1 * self.__Speed
			# print((x, y), 'coord, left')
		if dir == 'right':
			x += 1 * self.__Speed
			# print((x, y), 'coord, right')
		if dir == 'up':
			y -= 1 * self.__Speed
			# print((x, y), 'coord, up')
		if dir == 'down':
			y += 1 * self.__Speed
			# print((x, y), 'coord, down')

		Image_Node.Render.coords(img_ID, x, y)
		# print((x, y), 'NEW COORDS')
		return (x, y)
		# return self.kinetics(Cur_Coords, img_ID, dir)



	#special types of movement may be implimented later
	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Speed(self):
		"""
		:meta private:
		"""
		return self.__Speed


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Speed(self, Speed):
		"""
		:meta private:
		"""
		self.__Speed = Speed
