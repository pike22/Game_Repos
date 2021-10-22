from .wall_info import Wall_Info

class Wall_Main():
	def __init__(self, iNode, kNode, ID):
		#iNode == Image_Node
		#kNode == Collision_Node

		#----Class Calls----#
		self.__Kinetics	= kNode
		self.__Image	= iNode
		self.__info	 	= Wall_Info()
		self.__ID 		= ID
		self.__Group_ID = self.__info.get_group_ID()


	#seting up Wall bellow
	def Wall_setUP(self, x, y):
		#img setup
		Img_info = self.__Image.Img_Add('z_Pictures/Sword2.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/Sword2.png')
		self.__info.set_ID(ID)

		#placing the img
		img_coords = self.__Image.Img_Place(x, y, self.__info.get_TKimg(), tag=self.__ID)

		#final set of information save to Wall
		Canvas_ID = Image_Node.Render.find_withtag(self.__ID)[0] #finds my canvas self.__ID numb.
		Coords = img_coords[Canvas_ID-1]
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
		print(self.__info.get_Size(), 	'\t\t:Size')
		print(self.__info.get_Coords(), 	'\t\t:Coords')
		print(self.__info.get_Corners(), 	'\t:Corners')
		print('-----------------------------------\n')
