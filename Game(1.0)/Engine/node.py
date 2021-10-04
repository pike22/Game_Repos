class Node():
	def __init__(self):
		self.__Seconds		  = 0
		self.__GameTime 	  = 0
		self.__Frame_Count 	  = 33
		self.__Cur_FrameCount = 0


	def GameClock(self):
		self.__GameTime += 1
		if self.__GameTime == self.__Frame_Count:
			self.__Seconds += 1
			print(self.__Seconds, 'seconds')
			self.__Frame_Count += 33


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Seconds(self):
		return self.__Seconds


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...
