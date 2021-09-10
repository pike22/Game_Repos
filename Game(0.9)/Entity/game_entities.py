#this will be the parrent class for everything in the Entity folder

class Game_Entities():
	def __init__(self):
		self.__Collision_Box = None
		self.__file_Location = None
		self.__img_center = None
		self.__Cur_Coords = None #constantly saves current coords
		self.__imgPIL_ID	= None
		self.__imgTK_ID	= None
		self.__img_size	= None #(x, y)tuple of height, width
		self.__ID			= None
