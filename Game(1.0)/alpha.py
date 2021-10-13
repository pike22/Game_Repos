from PIL import ImageTk, Image
from z_Pictures import *
from colored import fg
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *
import keyboard #here for testing reasons

class Alpha():
	def __init__(self):
		self.__Sc_Width	 = 992
		self.__Sc_Height = 608
		self.__version	 = "(Stab Simulator) BETAv.1.0"
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
		self.__Timer		= Timer_Node(self.__mainApp)
		self.__Image		= Image_Node() #calls to other classes called need self.Img_Node
		self.__Kinetics		= Kinetics_Node(self.__Image)
		self.__Entities		= All_Entities()
		self.__Player		= Player_Main(self.__Image, self.__Collision_Logic, self.__Kinetics, self.__Timer)
		self.__Sword		= Sword_Main(self.__Image)
		self.__Bow			= Bow_Main(self.__Image)

		#yes
		self.__Entities.set_mainApp(self.__mainApp)

		'''Collision SETUP'''
		self.__Collision_Logic.add_Col_Dict(self.__Player.get_ID(), self.__Player)

		# self.__Stalfos = Stalfos_Main(self.__Image, self.__Collision_Logic)
		for item in range(self.__stalfosCount):
			if item < 10:
				ID = "S#00" + str(item)
			elif item >= 10 and item < 100:
				ID = "S#0" + str(item)
			self.__Stal_Roster.append(ID)
			self.__Collision_Logic.add_Col_Dict(tagOrId=ID, obj=Stalfos_Main(self.__Image, self.__Collision_Logic, self.__Kinetics, self.__Timer, ID=ID))

		#temp val
		self.__loopCount = 33
		self.__Seconds   = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self): #Set Renders HERE
		self.__Image.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width)

		#mass set_Render() Render was made Static Var
		#leave enemies out of this for now
		# self.__Collision_Logic.set_Render(self.__Image.get_Render())
		# self.__Kinetics.set_Render(self.__Image.get_Render())
		# self.__Player.set_Render(self.__Image.get_Render())
		# self.__Sword.set_Render(self.__Image.get_Render())

	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			self.__mainApp.destroy()

	def new_Player(self):
		if keyboard.is_pressed('e') == True:
			self.__Player.player_setUP(x=2, y=3, priority=0)
			self.__Player.set_isAlive(True)


	def GamesetUP(self):
		#Bellow is Entity set up
		#start Priority with 0
		self.__Player.player_setUP(x=2, y=3, priority=0)
		self.__Player.Player_Print() #temp turn off
		self.__Player.set_Weapons(self.__Sword, self.__Bow)
		self.__Sword.Sword_setUP()
		self.__Sword.Sword_Print()
		self.__Bow.Bow_setUP()
		self.__Bow.Bow_Print()

		#_CLOCK SETUP_#
		self.__Timer.GameClock()

		#__ENEMY Setup__#
		COLDICT = self.__Collision_Logic.get_Col_Dict()
		for item in range(len(self.__Stal_Roster)):
			if self.__Stal_Roster[item] in COLDICT.keys():
				r_Stal = COLDICT[self.__Stal_Roster[item]]
				r_Stal.stalfos_setUP(self.__Sc_Width, self.__Sc_Height)
				r_Stal.Stalfos_Print() #temp Turn off

	#gameLoop def is for the classes use.
	def gameLoop(self):

		#this loop will call itself again after the alloted amount of time.
		#therefor creating the game loop
		#to kill the window
		self.close_window()
		# self.new_Player()

		"""#_calls_#"""
		#Pass

		"""#_loop Debug_#"""
		# self.debug_Col_Dict() #workes

		"""#_Entity Loop Calls_#"""
			#_PLAYER_#
		if self.__Player.get_isAlive() == True:
			self.__Player.Player_MAttack()
			self.__Player.Player_RAttack()
			if self.__Player.Player_MAttack() == False and self.__Player.Player_RAttack() == False:
				self.__Player.Movement_Controll()
			else:
				print('ERROR: A#133')
			self.__Player.test_Coords()
		else:
			# print("dead? A#129")
			pass

			#_STALFOS_#
		Col_Dict = self.__Collision_Logic.get_Col_Dict()
		for item in range(len(self.__Stal_Roster)):
			stalfos = Col_Dict[self.__Stal_Roster[item]]
			if stalfos.get_isAlive() == True:
				# stalfos.Movement_Controll()
				stalfos.Stal_Attack()
			else:
				# print('dead? A#140')
				pass

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
		if self.__Sword.get_isActive() == True:
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
					# print('obj', Col_result[item])
					if Col_result[item] == self.__Player: #player is always checked first
						direction = self.__Collision_Logic.Dir_Calc()
						if Col_result[item+1].get_group_ID() in self.__enemyRoster:
							# print('direction:', direction)
							self.__Player.my_Collision('Enemy', Col_result[item+1].get_attack(), direction)
						# elif Col_result[item+1].get_group_ID() in self.__weaponRoster:
						# 	self.__Player.my_Collision('Weapon', Col_result[item+1].get_attack(), direction, DB='')

					if Col_result[item].get_ID() in self.__Stal_Roster:
						if item == len(Col_result)-1:
							pass
						elif item != len(Col_result)-1:
							if Col_result[item+1].get_group_ID() in self.__weaponRoster:
								Col_result[item].my_Collision('Weapon', Col_result[item+1].get_attack())

					if Col_result[item] == self.__Sword: #weapon will always be last
						#print('Sword')
						pass

		#_Combat_#
		if self.__Sword.get_isActive() == True:
			self.__Sword.Weapon_Active()

		if self.__Bow.get_isActive() == True:
			self.__Bow.Weapon_Active()

		if self.__Player.get_isHit() == True:
			self.__Player.reset_hit()

		Col_Dict = self.__Collision_Logic.get_Col_Dict()
		for item in range(len(self.__Stal_Roster)):
			result = Col_Dict[self.__Stal_Roster[item]]
			if result.get_isHit() == True:
				result.reset_hit()


		self.__mainApp.after(int(self.__Timer.get_FPS()), self.gameLoop)




	"""|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp


	"""|--------------Extra Functions--------------|#"""

	def find_all_Tags(self):
		listOfTags = Image_Node.Render.find_all()
		# print(listOfTags, 'list of tags')
		for item in listOfTags:
			tag = Image_Node.Render.gettags(item)
			if len(tag) > 0:
				color = fg('light_cyan')
				print(color + "Item", item, 'Has tag:', tag)

	def debug_Col_Dict(self):
		if keyboard.is_pressed('t'):
			self.__Collision_Logic.print_Col_Dict()
			self.__Collision_Logic.del_Col_Dict(self.__Player.get_ID())
			self.__Collision_Logic.print_Col_Dict()

	#this is a function call for test prints to make sure things work
	def Testing_Debug(self):
		self.find_all_Tags()
		# self.debug_Col_Dict()
		# print(Image_Node.Render, 'Render')


#puts the above class to action
Game = Alpha()
print('----------------------------\n') #to make it easier to read in the command promt
Game.set_MainCanvas()
Game.tk_windowSETUP()
Game.GamesetUP()
Game.Testing_Debug()
print('----------------------------')
Game.gameLoop()
Game.get_mainAPP().mainloop()
