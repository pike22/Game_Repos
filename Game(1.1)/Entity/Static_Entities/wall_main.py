from .wall_info import Wall_Info
from Engine import Image_Node

class Wall_Main():
	def __init__(self, iNode, cLogic):
		#iNode == Image_Node
		#cLogic == Collision_Logic

		#----Class Calls----#
		self.__cLogic = cLogic
		self.__iNode	 = iNode
		self.__info	 	 = Wall_Info()
		self.__ID 		 = self.__info.get_ID()
		self.__group_ID  = self.__info.get_group_ID()


	#seting up Wall bellow
	def wall_setUP(self, x, y):
		#img setup
		Img_info = self.__iNode.Img_Add('z_Pictures/MissingIMG.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/MissingIMG.png')

		#placing the img
		img_coords = self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=self.__ID)


		#final set of information save to Wall
		print(self.__ID)
		Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0] #finds my canvas with self.__ID numb.
		Coords = img_coords
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.Wall_Data(Coords=Coords) #check Wall_info for well info.
		Image_Node.Render.addtag_withtag(self.__group_ID, Canvas_ID)
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))

	def Wall_Print(self):
		#list of prints for start of program(Walls)
		print('-----------------------------------')
		print('Wall Data:')
		print(self.__info.get_ID(), '\t:Entity ID')
		print(self.__info.get_Speed(), 	'\t:Speed')
		print(self.__info.get_health(),	'\t:Health')
		print(self.__info.get_defense(),'\t:Defense')
		print(self.__info.get_attack(),	'\t:Attack')
		print('\nParameters:')
		print(self.__info.get_size(), 	'\t\t:Size')
		print(self.__info.get_Coords(), 	'\t\t:Coords')
		print(self.__info.get_Corners(), 	'\t:Corners')
		print('-----------------------------------\n')


	def my_Collision(self):
		pass


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_ID(self):
		return self.__info.get_ID()

	def get_group_ID(self):
		return self.__info.get_group_ID()

	def get_Coords(self):
		return self.__info.get_Coords()

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_size(self):
		return self.__info.get_size()

	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...
