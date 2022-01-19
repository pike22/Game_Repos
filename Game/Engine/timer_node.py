
class Timer_Node():
	"""
	This is to keep time for an in game clock.

	Parameters
	----------
	GameTime : Static
		Variable that holds the current game time in seconds.
	"""
	GameTime = 0
	def __init__(self, mainApp):
		self.__mainApp		  = mainApp
		self.__Seconds		  = 0
		self.__FPS			  = 1000 / 30
		self.__Frame_Count 	  = 33
		self.__Cur_FrameCount = 0

		'''Temp Var'''
		self.__targTime = 0


	def GameClock(self, OFF=False):
		"""
		Handles game time.

		Parameters
		----------
		OFF
			Prints out time in seconds to command prompt.
		"""
		Timer_Node.GameTime += 1
		if Timer_Node.GameTime == self.__Frame_Count:
			self.__Seconds += 1
			if OFF == True:
				print(self.__Seconds, 'seconds')
			self.__Frame_Count += 33

		self.__mainApp.after(int(self.__FPS), self.GameClock)


	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_Seconds(self):
		"""
		:meta private:
		"""
		return self.__Seconds

	def get_FPS(self):
		"""
		:meta private:
		"""
		return self.__FPS


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	# def set_...
	# 	"""
	# 	:meta private:
	# 	"""
