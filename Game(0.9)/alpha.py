from PIL import ImageTk, Image
from z_Pictures import *
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *
import keyboard #here for testing reasons

class Alpha():
	def __init__(self):
		self.__Sc_Width	 = 992
		self.__Sc_Height = 608
		self.__version	 = "(Stab Simulator) BETAv.0.9"
		self.__numLoop	 = 0
		self.__FPS		 = 1000 / 30
		self.__GameTime	 = 0
		self.__listTags  = None

		#this will be a growing list of group tags. It is hard set to refer here for spacific groups
		'''#_Enemy Parameters_#'''
		self.__enemyRoster	= ["#stalfos", ]
		self.__stalfosCount = 2 #create one for each enemy
		'''#_Weapon Parameters_#'''
		self.__weaponRoster = ["#sword", ]

		#collision logic v2.
		self.__Collision_Logic = Collision_Logic2()
		self.__Collision_Node  = Collision_Node()

		#below is class Calling
		self.__mainApp		= Tk()
		self.__Image		= Image_Node() #calls to other classes called need self.Img_Node
		self.__Player		= Player_Main(self.__Image, self.__Collision_Logic)
		self.__Stalfos		= Stalfos_Main(self.__Image, self.__Collision_Logic)
		self.__Sword		= Sword_Main(self.__Image)

		'''#_LEO_#''' #List of Enemy Objects
		self.__LEO = [self.__Stalfos, ]

		#temp val
		self.__loopCount = 33
		self.__Seconds   = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self):
		self.__Image.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width)

	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			self.__mainApp.destroy()

	def new_Player(self):
		if keyboard.is_pressed('e') == True:
			self.__Player.player_initial_setUP(x=2, y=3, priority=0)


	def GamesetUP(self):
		#Bellow is Entity set up
		#start Priority with 0
		self.__Player.player_initial_setUP(x=2, y=3, priority=0)
		self.__Player.Player_Print()
		self.__Player.set_Weapon(self.__Sword)
		#requires max screen size, number of wanted stalfos
		self.__Stalfos.stalfos_initial_setUP(self.__Sc_Width, self.__Sc_Height, stalfosCount=self.__stalfosCount, priority=1)
		#self.__Stalfos.Stalfos_Print() this is handled with the stalfos_Main.
		self.__Sword.Sword_setUP()
		self.__Sword.Sword_Print()

		#this is for the start of the game timer.
		self.__GameTime += 1 #it is the in game clock

	#gameLoop def is for the classes use.
	def gameLoop(self):

		#this loop will call itself again after the alloted amount of time.
		#therefor creating the game loop
		def loop():
			#to kill the window
			self.close_window()
			# self.new_Player()

			#the games inner clock
			self.__GameTime += 1 #it is the in game clock
			#print(self.__GameTime)
			#this feeds the sword code the current game loop time
			if self.__GameTime == self.__loopCount:
				self.__Seconds += 1
				self.__Sword.set_GameTime(self.__Seconds)
				print(str(self.__Seconds), 'SECOND')
				self.__loopCount += 33

			#_calls_#

			#_loop Debug_#
			# self.debug_Col_Dict() #workes

			#_player calls_#
			output = self.__Player.alive()
			if output == True:
				self.__Player.Movement_Controll()
				self.__Player.Player_Attack()
				self.__Player.test_Coords()


			#_Collision Logic functions_#
			"""!!#_Version 2 of Collision logic_#!!"""

			#here is where I am setting up the Collision Dictionary.
			self.__Collision_Logic.add_Col_Dict(self.__Player.get_ID(), self.__Player)
			for item in range(len(self.__Stalfos.get_ID(ALL=True))):
				self.__Collision_Logic.add_Col_Dict(self.__Stalfos.get_ID(item=item), self.__Stalfos)

			self.__Collision_Logic.set_Render(self.__Image.get_Render())
			c_Player  = self.__Player.get_Corners() #Always item 0
			c_Stalfos = self.__Stalfos.get_Corners()

			self.__Collision_Logic.set_tag_List(self.__Player.get_ID())
			for item in range(len(self.__Stalfos.get_ID(ALL=True))):
				self.__Collision_Logic.set_tag_List(self.__Stalfos.get_ID(item=item))
			#only one c_Player should be here (IGNORE MULTIPLAYER)
			list1 = []
			list1 = [c_Player]
			for item in range(len(c_Stalfos)):
				list1.append(c_Stalfos[item])

			#self.__stalfosCount represents stalfos corners
			dict = self.__Collision_Logic.get_Col_Dict()
			if self.__Sword.get_IsWeapon() == True:
				Sword = 1
				self.__Collision_Logic.set_tag_List(self.__Sword.get_ID())
				list1.append(self.__Sword.get_Corners())
				if self.__Sword.get_ID() not in dict.keys():
					self.__Collision_Logic.add_Col_Dict(self.__Sword.get_ID(), self.__Sword)
			else:
				Sword = 0
				if self.__Sword.get_ID() in dict.keys():
					self.__Collision_Logic.del_Col_Dict(self.__Sword.get_ID())

			self.__Collision_Logic.add_Collision(list1)

			#player represents the players Corners
			player = 1
			#when more enemies exist create more 'enemyName'Count, then add below.
			for item in range(player + Sword + self.__stalfosCount):
				# Collision_ForT, Collision_List = self.__Collision_Logic.Is_Collision(item)
				Col_result = self.__Collision_Logic.Is_Collision(item)#, self.__LEO)


				if Col_result != None:
					Col_Dict = self.__Collision_Logic.get_Col_Dict() #this may not be needed
					for item in range(len(Col_result)):
						# print('obj', Col_result[item+1])
						if Col_result[item] == self.__Player: #player is always checked first
							if Col_result[item+1].get_group_ID() in self.__enemyRoster:
								self.__Player.my_Collision('Enemy', Col_result[item+1].get_attack())
							elif Col_result[item+1].get_group_ID() in self.__weaponRoster:
								self.__Player.my_Collision('Weapon', Col_result[item+1].get_attack())
							# print('player')
						if Col_result[item] == self.__Stalfos:
							if item == len(Col_result)-1:
								pass
							elif item != len(Col_result)-1:
								if Col_result[item+1].get_group_ID() in self.__weaponRoster:
									self.__Stalfos.my_Collision('Weapon', Col_result[item+1].get_attack(), tag_result[0])
									# print('stalfos')
						if Col_result[item] == self.__Sword: #weapon will always be last
							#print('Sword')
							pass

			#_Combat_#
			if self.__Sword.get_IsWeapon() == True:
				self.__Sword.Weapon_Active()


			self.__mainApp.after(int(self.__FPS), loop)
		loop()




	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp


	"""|--------------Extra Functions--------------|#"""

	def find_all_Tags(self):
		myCanvas = self.__Image.get_Render()
		listOfTags = myCanvas.find_all()
		# print(listOfTags, 'list of tags')
		for item in listOfTags:
			tag = myCanvas.gettags(item)
			if len(tag) > 0:
				print("Item", item, 'Has tag:', tag)

	def debug_Col_Dict(self):
		if keyboard.is_pressed('t'):
			self.__Collision_Logic.print_Col_Dict()
			self.__Collision_Logic.del_Col_Dict(self.__Player.get_ID())
			self.__Collision_Logic.print_Col_Dict()

	#this is a function call for test prints to make sure things work
	def Testing_Debug(self):
		self.find_all_Tags()


#puts the above class to action
Game = Alpha()
Game.set_MainCanvas()
Game.tk_windowSETUP()
Game.GamesetUP()
Game.Testing_Debug()
Game.gameLoop()
Game.get_mainAPP().mainloop()
