from Engine.image_node import Image_Node
from .all_projectile import Projectiles
from .arrow_info import Arrow_Info

class Arrow_Main(Projectiles):
	def __init__(self):
		super().__init__()
		self.__info 	= Arrow_Info()
		self.__ID 		= self.__info.get_ID()
		self.__group_ID = self.__info.get_group_ID()
		self.__Direction = None

		self.__isActive = False

	def Arrow_setUP(self):
		#img setup
		Img_info = self.get_iNode().Img_Add('z_Pictures/arrowmaybe.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/arrowmaybe.png')


	def use_Arrow(self, x, y, direction):
		self.Arrow_setUP()
		if self.__isActive == False:
			self.get_iNode().Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=self.__ID)
			self.__isActive = True

			#final half of Arrow_setUP
			Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0] #finds my canvas ID numb.

			self.__info.set_Canvas_ID(Canvas_ID)
			self.__info.Arrow_Data(attack=2, Coords=(x, y)) #check player_info for well info.
			Image_Node.Render.addtag_withtag(self.__group_ID, Canvas_ID)

			#arrow move
			print(direction, 'direction')
			self.__Direction = direction
			self.isActive()

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
		self.__isActive = False
		Image_Node.Render.delete(self.__info.get_ID())
