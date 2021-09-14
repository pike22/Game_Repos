from PIL import ImageTk, Image
from z_Pictures import *
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *

class Alpha():
	def __init__(self):
		self.__Sc_Width	 = 992
		self.__Sc_Height = 608
		self.__version	 = "(Stab Simulator) BETAv.0.9"
		self.__numLoop	 = 0
		self.__FPS		 = 1000 / 30
		self.__GameTime	 = 0
		self.__listTags = None

		#this will be a growing list of group tags. It is hard set to refer here for spacific groups
		#enemy based parameters
		self.__enemyRoster	= ["#stalfos", ]
		self.__stalfosCount = 1 #create one for each enemy
		#weapon based Parameters
		self.__weaponRoster = ["#sword", ]

		#below is class Calling
		self.__mainApp		= Tk()
		self.__Image		= Image_Node() #calls to other classes called need self.Img_Node
		self.__Player		= Player_Main(self.__Image)
		self.__Stalfos		= Stalfos_Main(self.__Image)
		self.__Sword		= Sword_Main(self.__Image)

		#the list in Collision Logic will increase as needed
		#collision logic v2.
		self.__Collision_Logic = Collision_Logic2()
		self.__COllision_Node = Collision_Node()
		self.__list1 = []

		#temp val
		self.__loopCount = 33
		self.__Seconds   = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self):
		self.__Image.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width)

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

		#Setting classes into the collision Logic class
		self.__Player.set_Collision_Logic(self.__Collision_Logic)
		self.__Stalfos.set_Collision_Logic(self.__Collision_Logic)


		#this is for the start of the game timer.
		self.__GameTime += 1 #it is the in game clock

	def find_Entity(self, tagOrId): #the goal is to associate tags with the correct entity class.
	#is currently being hard coded. Later imprvements needed.
		if tagOrId == self.__Player.get_ID():
			print('player')
			return_tagOrId = self.__Player
			return return_tagOrId
		elif tagOrId == self.__Stalfos.get_ID2(0): #0 for list[0]
			print('stalfos')
			return_tagOrId = self.__Stalfos
			return return_tagOrId
		# elif tagOrId == self.__Sword.get_ID(): #temporarly turned off
			# print('sword')
			# return_tagOrId = self.__Sword
			# return return_tagOrId


	#gameLoop def is for the classes use.
	def gameLoop(self):

		#this loop will call itself again after the alloted amount of time.
		#therefor creating the game loop
		def loop():
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

			#_player calls_#
			self.__Player.Movement_Controll()
			self.__Player.Player_Attack()
			self.__Player.test_Coords()


			#_Collision Logic functions_#
			"""!!#_Version 2 of Collision logic_#!!"""
			self.__Collision_Logic.set_Render(self.__Image.get_Render())
			c2_Player  = self.__Player.get_Corners() #Always item 0
			c2_Stalfos = self.__Stalfos.get_Corners()
			#only one should be here (IGNORE MULTIPLAYER)
			self.__list1 = []
			self.__list1 = [c2_Player]
			for item in range(len(c2_Stalfos)):
				self.__list1.append(c2_Stalfos[item])

			#self.__stalfosCount represents stalfos corners
			if self.__Sword.get_IsWeapon() == True:
				Sword = 1
				self.__list1.append(self.__Sword.get_Corners())
			else:
				Sword = 0

			self.__Collision_Logic.add_Collision(self.__list1)

			#player represents the players Corners
			player = 1
			#when more enemies exist create more 'enemyName'Count, then add below.
			for item in range(player + Sword + self.__stalfosCount):
				Collision_ForT, what_Collides = self.__Collision_Logic.Is_Collision(item)

				#this shall continue inside of the collision_node
				#Collision doesn't need to clutter the main loop.
				
				#A, B are the two subjects for what is colliding
				if Collision_ForT != None:
					A, B = what_Collides
					A = self.find_Entity(A)
					B = self.find_Entity(B)



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
