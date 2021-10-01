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
		'''#_Enemy Variables_#''' #include a list of tags for each enemy
		self.__enemyRoster	= ["#stalfos", ]

			#_Stalfos_#
		self.__Stal_Roster	= []
		self.__stalfosCount = 2

		'''#_Weapon Parameters_#'''
		self.__weaponRoster = ["#sword", ]

		#collision logic v2.
		self.__Collision_Logic = Collision_Logic()
		self.__Collision_Node  = Collision_Node()

		#below is class Calling
		self.__mainApp		= Tk()
		self.__Node 		= Node()
		self.__Image		= Image_Node() #calls to other classes called need self.Img_Node
		self.__kinetics		= Kinetics_Node(self.__Image)
		self.__Player		= Player_Main(self.__Image, self.__Collision_Logic, self.__kinetics)
		self.__Sword		= Sword_Main(self.__Image)


		'''Collision SETUP'''
		self.__Collision_Logic.add_Col_Dict(self.__Player.get_ID(), self.__Player)

		# self.__Stalfos = Stalfos_Main(self.__Image, self.__Collision_Logic)
		for item in range(self.__stalfosCount):
			if item < 10:
				ID = "S#00" + str(item)
			elif item >= 10 and item < 100:
				ID = "S#0" + str(item)
			self.__Stal_Roster.append(ID)
			self.__Collision_Logic.add_Col_Dict(tagOrId=ID, obj=Stalfos_Main(self.__Image, self.__Collision_Logic, self.__kinetics, ID=ID))

		#temp val
		self.__loopCount = 33
		self.__Seconds   = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self): #Set Renders HERE
		self.__Image.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width)

		#mass set_Render()
		#leave enemies out of this for now
		self.__Collision_Logic.set_Render(self.__Image.get_Render())
		self.__kinetics.set_Render(self.__Image.get_Render())
		self.__Player.set_Render(self.__Image.get_Render())
		self.__Sword.set_Render(self.__Image.get_Render())

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
		self.__Sword.Sword_setUP()
		# self.__Sword.Sword_Print()

		#__ENEMY Setup__#
		COLDICT = self.__Collision_Logic.get_Col_Dict()
		for item in range(len(self.__Stal_Roster)):
			if self.__Stal_Roster[item] in COLDICT.keys():
				r_Stal = COLDICT[self.__Stal_Roster[item]]
				r_Stal.stalfos_initial_setUP(self.__Sc_Width, self.__Sc_Height)
				r_Stal.Stalfos_Print()

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
				self.give_gameTime(self.__Seconds)
				print(str(self.__Seconds), 'SECOND')
				self.__loopCount += 33

			#_calls_#

			#_loop Debug_#
			# self.debug_Col_Dict() #workes

			#_player calls_#
			output = self.__Player.get_isAlive()
			if output == True:
				self.__Player.Movement_Controll()
				self.__Player.Player_Attack()
				self.__Player.test_Coords()
			else:
				print("dead?")

			#_Collision Logic functions_#
			"""!!#_Version 2 of Collision logic_#!!"""
			#_COL_Dict is set up inside the alpha.__init__()

			#only one Player should be here (IGNORE MULTIPLAYER)
			list1 = []
			list1 = [self.__Player.get_Corners()]
			for item in range(len(self.__Stal_Roster)):
				c_Stal = self.__Collision_Logic.tag_to_obj(self.__Stal_Roster[item]) #c_Stal == stalfos obj
				list1.append(c_Stal.get_Corners())

			#self.__stalfosCount represents number of stalfo's and their corners
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
				Col_result = self.__Collision_Logic.Is_Collision(item)


				if Col_result != None:
					Col_Dict = self.__Collision_Logic.get_Col_Dict() #this may not be needed
					for item in range(len(Col_result)):
						# print('obj', Col_result[item+1])
						if Col_result[item] == self.__Player: #player is always checked first
							if Col_result[item+1].get_group_ID() in self.__enemyRoster:
								var = self.__Player.my_Collision('Enemy', Col_result[item+1].get_attack())
								# if var == True:
								# 	pass
							elif Col_result[item+1].get_group_ID() in self.__weaponRoster:
								self.__Player.my_Collision('Weapon', Col_result[item+1].get_attack())
							# print('player')
						if Col_result[item].get_ID() in self.__Stal_Roster:
							if item == len(Col_result)-1:
								pass
							elif item != len(Col_result)-1:
								if Col_result[item+1].get_group_ID() in self.__weaponRoster:
									Col_result[item].my_Collision('Weapon', Col_result[item+1].get_attack())
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

	def give_gameTime(self, GameTime):
		self.__Player.save_GT(GameTime)
		self.__Sword.save_GT(GameTime)

	#this is a function call for test prints to make sure things work
	def Testing_Debug(self):
		self.find_all_Tags()


#puts the above class to action
Game = Alpha()
print('') #to make it easier to read in the command promt
Game.set_MainCanvas()
Game.tk_windowSETUP()
Game.GamesetUP()
Game.Testing_Debug()
Game.gameLoop()
Game.get_mainAPP().mainloop()
