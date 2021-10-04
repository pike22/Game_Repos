
class Timer_Node():
	def __init__(self, mainApp):
		self.__mainApp		  = mainApp
		self.__Seconds		  = 0
		self.__MSeconds 	  = 0
		self.__Frame_Count 	  = 33
		self.__Cur_FrameCount = 0


	def GameClock(self):
		self.__MSeconds += 1
		if self.__MSeconds == self.__Frame_Count:
			self.__Seconds += 1
			print(self.__Seconds, 'seconds')
			self.__Frame_Count += 33

		self.__mainApp.after(int(self.__FPS), self.GameClock)

	def create_After(self, Time, DEF):

		self.__mainApp.after(int(Time), DEF)


	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Seconds(self):
		return self.__Seconds

	def get_GameTime(self):
		return self.__MSeconds


	"""|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	#def set_...
