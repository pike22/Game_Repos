import keyboard

class Collision_Logic2():
	def __init__(self):
		self.__collision = []
		self.__Corners 	 = []
		self.__list_len	 = 0
		self.__Render	 = None
		self.__IsCollision = False


	def add_Collision(self, listofCorners):
		self.__Corners 	= []
		self.__list_len = 0
		for item in range(len(listofCorners)):
			self.__Corners.append(listofCorners[item])
		self.__list_len = len(self.__Corners)


	def del_Collision(self, ):
		pass #this may not be needed


	def what_Collides(self, collision_list): #only runs when __IsCollision == True
		#for now I will focus on 1-on-1 collision,
		#won't worry about multi-hit fucntionality.
		target_A = collision_list[0]
		target_B = collision_list[1]

		return (target_A, target_B)



	#use this: .find_overlapping
	# only outputs the last assigned var.
	def Is_Collision(self, item):
		self.__collision = []
		#for item in range(len(self.__Corners)):
			#print(item, 'item')
		x1, y1, x2, y2 = self.__Corners[item]
		collision = self.__Render.find_overlapping(x1, y1, x2, y2)
			#if item == 1:
				# print(collision[0],':ID,', item, ':Item')

		#this only shows what is colliding.
		if len(collision) > 1:
			#print(collision, 'ID', )
			for item in range(len(collision)):
				tag = self.__Render.gettags(collision[item])
				self.__collision.append(tag[0]) #item 0 is the entity spacific ID, 1 == group_ID
			print(self.__collision, 'Colliding')

			self.__IsCollision = True
			ForT = self.what_Collides(self.__collision)
			return self.__IsCollision, ForT
		else:
			self.__IsCollision = False
			# return self.__IsCollision
			return None, None




	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	#def get_...


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_Render(self, Render):
		self.__Render = Render
