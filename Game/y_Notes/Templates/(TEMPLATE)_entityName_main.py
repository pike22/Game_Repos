from entityName_info import entityName_Info

class entityName_Main():
	def __init__(self, iNode, kNode):
		#iNode == Image_Node
		#clNode == Collision_Node

		#----Class Calls----#
		self.__kNode		= kNode
		self.__iNode	 	= iNode
		self.__info	 		= entityName_Info()


	#seting up entityName bellow
	def entityName_setUP(self, x, y):
		#img setup
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		Img_info = self.__iNode.Img_Add('z_Pictures/picName.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/picName.png')

		#placing the img
		img_coords = self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=ID)

		#final set of information save to entityName
		Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
		Current_Coords = img_coords[Canvas_ID-1]
		self.__info.set_Canvas_ID(Canvas_ID)
		self.__info.entityName_Data(Cur_Coords=Current_Coords, Speed=0, health=0, defense=0, attack=0) #check entityName_info for well info.
		self.__kNode.set_Speed(self.__info.get_Speed())
		Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))

	def entityName_Print(self):
		#list of prints for start of program(entityNames)
		print('-----------------------------------')
		print('entityName Data:')
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
