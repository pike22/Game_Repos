from .sword_info import Sword_Info

class Sword_Main():
	def __init__(self, iNode):
		self.__Image	= iNode
		self.__info		= Sword_Info()

		self.__timeSave	 = 0
		self.__Curr_GT   = 0
		self.__active	 = False


	def Sword_setUP(self):
		#img setup
		ID = "W#S001"
		group_ID = "#sword"
		self.__info.set_group_ID(group_ID)
		Img_info = self.__Image.Img_Add('z_Pictures/notasword.png')
		self.__info.Image_Data(Size=Img_info[1], ID=ID , PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/notasword.png')
		self.__info.Sword_Data(2) #check melee_info for well info.

		#self.output = self.Image.

	def use_Sword(self, x, y):
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		if self.__active == False:
			img_list, img_coords = self.__Image.Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=ID)

			Canvas_ID = self.__Image.get_Render().find_withtag(ID)[0] #finds my canvas ID numb.
			self.__info.set_Canvas_ID(Canvas_ID)
			self.__Image.get_Render().addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(self.__Image.get_Render().bbox(Canvas_ID))
			self.__timeSave = self.__Curr_GT
			self.__active = True

	def Weapon_Active(self):
		if self.__Curr_GT == (self.__timeSave+1):
			#print("work?") #answer: YES
			render = self.__Image.get_Render()
			render.delete(self.__info.get_ID())
			self.__active = False

	def del_Sword(self):
		render = self.__Image.get_Render()
		render.delete(self.__info.get_ID())
		#self.__info.Data_Wipe() #clears canvas_ID, ID, Corners
		self.__active = False



	def Sword_Print(self):
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Sword Data:')
		print(self.__info.get_ID(), '\t:ID') #should be None
		print(self.__info.get_Attack_Dmg(), '\t:Attck')
		print('-----------------------------------')



	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Attack(self):
		return self.__info.get_Attack_Dmg()

	def get_Curr_GT(self): #bassed on game created seconds
		return self.__Curr_GT

	def get_Size(self):
		return self.__info.get_Size()

	def get_IsWeapon(self):
		return self.__active

	def get_Corners(self):
		return self.__info.get_Corners()

	def get_ID(self):
		return self.__info.get_ID()


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_GameTime(self, Curr_GT):
		self.__Curr_GT = Curr_GT

	def set_IsWeapon(self, Fort):
		self.__active = Fort
