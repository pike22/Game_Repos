from Engine.image_node import Image_Node
from .all_projectile import Projectiles
from .arrow_info import Arrow_Info

class Arrow_Main(Projectiles):
	"""
	Controlls everything to do with the arrow.

	Methods
	-------
	init(iNode, cLogic, cNode, kNode, itemCount)
		This is required when Arrow_Main() is called
	"""
	def __init__(self, iNode, cLogic, cNode, kNode, itemCount):
		self.__info 	= Arrow_Info()
		self.__iNode	= iNode
		self.__cLogic	= cLogic
		self.__cNode 	= cNode
		self.__kNode	= kNode
		self.__ID 		= "P#A00"+str(itemCount)
		self.__group_ID = self.__info.get_group_ID()
		self.__Direction = None

		#potential removal
		self.__isActive  = False
		self.__count	 = 0

	def Arrow_setUP(self):
		"""
		Basic arrow tkinter set up.
		"""
		#img setup
		self.__info.set_ID(self.__ID)
		Img_info = self.__iNode.Img_Add('z_Pictures/arrow_.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/arrow_.png')


	def use(self, x, y, direction, dmgMod):
		"""
		Controlls what happens when the arrow is *used*.

		Parameters
		----------
		x, y : int
			The coords where the arrow will be placed first.
		direction : str
			The direction that the arrows will fly.
		dmgMod : int
			The the additional damage that will be delt when the arrow hits its target.
		"""
		self.Arrow_setUP()
		if direction == 'up':
			# print('up')s
			newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 90)
			self.__info.set_TKimg(newIMG)
			self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[self.__ID, self.__info.get_group_ID()])
		elif direction == 'down':
			# print('down')s
			newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 270)
			self.__info.set_TKimg(newIMG)
			self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[self.__ID, self.__info.get_group_ID()])
		elif direction == 'left':
			# print('left')s
			newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 180)
			self.__info.set_TKimg(newIMG)
			self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[self.__ID, self.__info.get_group_ID()])
		elif direction == 'right':
			# print('right') #this is snormal direction
			newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 0)
			self.__info.set_TKimg(newIMG)
			self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[self.__ID, self.__info.get_group_ID()])


		self.__isActive = True

		#final half of Arrow_setUP
		Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0] #finds my canvas ID numb.

		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Arrow_Data(attack=2+dmgMod, Coords=(x, y)) #check arrow_info for well info.
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
		Image_Node.Render.addtag_withtag(self.__group_ID, Canvas_ID)

		#arrow move
		self.__Direction = direction

	def isActive(self):
		"""
		Moves the arrow forward during the game loop.
		"""
		# print('hello"')
		self.__kNode.set_Speed(15)
		if self.__Direction == 'up':
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__ID, 'up')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'down':
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__ID, 'down')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'left':
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__ID, 'left')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'right':
			new_Coords = self.__kNode.kinetics(self.__info.get_Coords(), self.__ID, 'right')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))

	def del_Proj(self):
		"""
		Delets the object when the arrow collides with anything.
		"""
		self.__isActive  = False
		Image_Node.Render.delete(self.__info.get_canvasID())
		self.__cLogic.delColDict(tagOrId=self.__ID)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__info.get_Corners()

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__info.get_Coords()

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__info.get_size()

	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__ID

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__group_ID

	def get_itemCount(self):
		"""
		:meta private:
		"""
		return self.__itemCount

	def get_isActive(self):
		"""
		:meta private:
		"""
		return self.__isActive

	def get_attack(self):
		"""
		:meta private:
		"""
		return self.__info.get_attack()


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...
