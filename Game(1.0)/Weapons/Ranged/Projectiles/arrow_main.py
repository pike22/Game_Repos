from Engine.image_node import Image_Node
from .all_projectile import Projectiles
from .arrow_info import Arrow_Info

class Arrow_Main(Projectiles):
	def __init__(self):
		super().__init__()
		self.__info 	= Arrow_Info()
		self.__group_ID = self.__info.get_ID()
		self.__ID 		= self.__info.get_group_ID()

		self.__isActive = False

	def Arrow_setUP(self):
		#img setup
		# ID = self.__info.get_ID()
		# group_ID = self.__info.get_group_ID()
		print(self.get_iNode(),'INODE')
		Img_info = self.get_iNode().Img_Add('z_Pictures/arrowmaybe.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/arrowmaybe.png')

		#final set of information save
		Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0] #finds my canvas ID numb.
		Current_Coords = img_coords[Canvas_ID-1]
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Arrow_Data(attack=2) #check player_info for well info.
		Image_Node.Render.addtag_withtag(self.__group_ID, Canvas_ID)

	def use_Arrow(self, x, y):
		self.Arrow_setUP()
		if self.__isActive == False:
			self.get_iNode().Img_place(x, y, self.__info.get_TKimg(), Grid='No', tag=self.__ID)
			self.__isActive = True

	def del_Arrow(self):
		self.__isActive = False
		Image_Node.Render.delete(self.__info.get_ID())
