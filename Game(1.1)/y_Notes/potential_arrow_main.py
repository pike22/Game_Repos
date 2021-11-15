from Engine.image_node import Image_Node
from .all_projectile import Projectiles
from .arrow_info import Arrow_Info

#This is my re write!!
class Arrow_Main(Projectiles):
	def __init__(self):
		super().__init__()
		self.__info 	= Arrow_Info()
		self.__ID 		= None
		self.__group_ID = self.__info.get_group_ID()
		self.__Direction = None

		self.__itemCount = 0
		self.__isActive  = False

	def Arrow_setUP(self):
		Img_info = self.get_iNode().Img_Add('z_Pictures/arrowmaybe.png')
		self.__info.set_fileLocation('z_Pictures/arrowmaybe.png')

		self.__itemCount += 1
		self.__ID = "A#00"+str(self.__itemCount)
		self.__info.set_ID(self.__ID)
		self.__info.Image_Data(ID=self.__ID, Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2])

	def use_Arrow(self, x, y, direction, dmgMod):
		self.Arrow_setUP()

		self.get_iNode().Img_Place(x, y, self.__info.get_TKimg(self.__ID), Grid='No', tag=self.__ID)
		self.__isActive = True

		Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0]
		self.__info.set_CanvasID(ID=self.__ID, Canvas_ID=Canvas_ID)
		self.__info.Arrow_Data(attack=2+dmgMod, Coords=(x,y))
		self.__info.set_Corners(ID=self.__ID, Corners=Image_Node.Render.bbox(Canvas_ID))
		Image_Node.Render.addtag_withtag(self.__group_ID, Canvas_ID)

		self.__Direction = direction

	def isActive(self, ID):
		if self.__Direction == 'up':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'up')
			self.__info.set_Coords(ID=ID, new_Coords)
			self.__info.set_Corners(ID=ID, Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'down':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'down')
			self.__info.set_Coords(ID=ID, new_Coords)
			self.__info.set_Corners(ID=ID, Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'left':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'left')
			self.__info.set_Coords(ID=ID, new_Coords)
			self.__info.set_Corners(ID=ID, Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'right':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'right')
			self.__info.set_Coords(ID=ID, new_Coords)
			self.__info.set_Corners(ID=ID, Image_Node.Render.bbox(self.__info.get_ID()))

	def del_Proj(self, ID):
		Image_Node.Render.delete(self.__info.get_canvasID(ID))
		self.__isActive = False
		self.__itemCount -= 1


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_itemCount(self):
		return self.__itemCount

	def get_isActive(self):
		return self.__isActive

	def get_attack(self):
		return self.__info.get_attack()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...


"""------------------------------------------------------------------------------
---------------------------------------------------------------------------------
------------------------------------------------------------------------------"""

#This is the original.
class Arrow_Main(Projectiles):
	def __init__(self):
		super().__init__()
		self.__info 	= Arrow_Info()
		self.__ID 		= self.__info.get_ID()
		self.__group_ID = self.__info.get_group_ID()
		self.__Direction = None

		self.__itemCount = 0
		self.__isActive  = False

	def Arrow_setUP(self):
		#img setup
		Img_info = self.get_iNode().Img_Add('z_Pictures/arrowmaybe.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/arrowmaybe.png')


	def use_Arrow(self, x, y, direction, dmgMod):
		self.Arrow_setUP()
		if self.__isActive == False:
			self.get_iNode().Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=self.__ID)
			self.__isActive = True

			#final half of Arrow_setUP
			Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0] #finds my canvas ID numb.

			self.__info.set_Canvas_ID(Canvas_ID)
			self.__info.Arrow_Data(attack=2+dmgMod, Coords=(x, y)) #check arrow_info for well info.
			self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
			Image_Node.Render.addtag_withtag(self.__group_ID, Canvas_ID)

			#arrow move
			self.__Direction = direction
			self.__itemCount += 1

	def isActive(self):
		# print('hello"')
		if self.__Direction == 'up':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'up')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'down':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'down')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'left':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'left')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))
		elif self.__Direction == 'right':
			new_Coords = self.get_kNode().kinetics(self.__info.get_Coords(), self.__ID, 'right')
			self.__info.set_Coords(new_Coords)
			self.__info.set_Corners(Image_Node.Render.bbox(self.__info.get_ID()))

	def del_Arrow(self):
		Image_Node.Render.delete(self.__info.get_canvasID())
		self.__isActive = False
		self.__itemCount -= 1


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_itemCount(self):
		return self.__itemCount

	def get_isActive(self):
		return self.__isActive

	def get_attack(self):
		return self.__info.get_attack()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...
