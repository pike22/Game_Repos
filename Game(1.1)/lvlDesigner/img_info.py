
class IMG_Info():
	def __init__(self, group_ID):
		#engine based Parameters.
		self.__file_Location = None
		self.__Canvas_ID	= None
		self.__group_ID		= str(group_ID)
		self.__ID			= []
		self.__imgPIL_ID	= None
		self.__imgTK_ID		= None
		self.__img_size		= None #(x, y)tuple of height, width
		self.__Corners		= None #(x1, y1, x2, y2) tuple
		self.__Coords 		= None

		#save to txt
		self.__PLC_Corners = {}
		self.__PLC_Coords  = {}
		self.__PLC_pilIMG  = {}
		self.__PLC_tkIMG   = {}


	def Image_Data(self, Size=None, PIL_img=None, TK_img=None, file_Location=None):
		self.__file_Location	= file_Location
		self.__imgPIL_ID		= PIL_img
		self.__imgTK_ID			= TK_img
		self.__img_size			= Size

	def Item_Data(self, Coords=None):
		self.__Coords = Coords

	def Placed_imgData(self, ID, Corners, Coords, pilIMG, tkIMG):
		self.__PLC_Corners[ID] = Corners
		self.__PLC_Coords[ID]  = Coords
		self.__PLC_pilIMG[ID]  = pilIMG
		self.__PLC_tkIMG[ID]   = tkIMG


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...

	def get_TKimg(self):
		return self.__imgTK_ID

	def get_Coords(self):
		return self.__Coords

	def get_Size(self):
		return self.__img_size

	def get_Corners(self):
		return self.__Corners

	def get_fileLocation(self):
		return self.__file_Location

	def get_ID(self, item=None, full=True):
		if full == True:
			return self.__ID
		else:
			return self.__ID[item]

	def get_group_ID(self):
		return self.__group_ID

	def show_PLC_Data(self, ):
		print(	self.__PLC_Coords, '\n',
				self.__PLC_Corners, '\n',
				self.__PLC_tkIMG, '\n',
				self.__PLC_pilIMG, '\n'	)

	def get_PLC_tkIMG(self, key):
		# print(self.__PLC_tkIMG[key], 'tk')
		return self.__PLC_tkIMG[key]

	def get_PLC_pilIMG(self, key):
		# print(self.__PLC_pilIMG[key], 'pil')
		return self.__PLC_pilIMG[key]

	def get_PLC_Coords(self, key):
		# print(self.__PLC_Coords[key], 'Coords')
		return self.__PLC_Coords[key]

	def	get_PLC_Corners(self, key):
		# print(self.__PLC_Corners[key], 'Corners')
		return self.__PLC_Corners[key]



	"""|--------------Setters--------------|#"""
	def set_Coords(self, Coords):
		self.__Coords = Coords

	def set_Canvas_ID(self, Canvas_ID):
		self.__Canvas_ID = Canvas_ID

	def set_Corners(self, bbox):
		self.__Corners = bbox

	def set_ID(self, ID):
		self.__ID.append(str(ID))
