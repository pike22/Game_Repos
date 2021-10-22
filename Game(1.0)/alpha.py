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
		self.__weaponRoster 	= ["#sword", "#bow", ]
		self.__projRoster = ['#arrow', ]
		self.__projDict	= {}

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
		self.__Projectiles  = Projectiles()
		self.__Player		= Player_Main(self.__Image, self.__Kinetics)
		self.__Sword		= Sword_Main(self.__Image, self.__Collision_Logic)
		self.__Bow			= Bow_Main(self.__Image, self.__Collision_Logic)

		#yes
		self.__Entities.set_mainApp(self.__mainApp)
		self.__Projectiles.set_Nodes(self.__Image, self.__Kinetics, self.__Collision_Logic)

		'''Collision SETUP'''
		#-------------------#
		"""Entities"""
		self.__Collision_Logic.add_Col_Dict(self.__Player.get_ID(), self.__Player)
		#Static Entities
		self.__Wall = Wall_Main(self.__Image, self.__Collision_Logic)
		
		#Stalfos collision setup
		for item in range(self.__stalfosCount):
			if item < 10:
				ID = "S#00" + str(item)
			elif item >= 10 and item < 100:
				ID = "S#0" + str(item)
			self.__Stal_Roster.append(ID)
			self.__Collision_Logic.add_Col_Dict(tagOrId=ID, obj=Stalfos_Main(self.__Image, self.__Collision_Logic, self.__Kinetics, self.__Timer, ID=ID))

		"""Items"""
		self.__Collision_Logic.add_Col_Dict(self.__Sword.get_ID(), self.__Sword)
		self.__Collision_Logic.add_Col_Dict(self.__Bow.get_ID(), self.__Bow)

		"""Projectiles"""
		self.__Collision_Logic.add_Col_Dict(self.__projDict['#arrow'].get_ID(), self.__projDict['#arrow'])


		#temp val
		self.__loopCount = 33
		self.__Seconds   = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self): #Set Renders HERE
		self.__Image.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width)

		#mass set_Render() !!!Render was made Static Var!!!
		#leave enemies out of this for now
		# self.__Collision_Logic.set_Render(self.__Image.get_Render())
		# self.__Kinetics.set_Render(self.__Image.get_Render())
		# self.__Player.set_Render(self.__Image.get_Render())
		# self.__Sword.set_Render(self.__Image.get_Render())

	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			self.__mainApp.destroy()

	def GamesetUP(self):
		#Bellow is Entity set up
		self.__Player.player_setUP(x=2, y=3)
		# self.__Player.Player_Print()
		self.__Sword.Sword_setUP()
		# self.__Sword.Sword_Print()
		self.__Bow.Bow_setUP()
		# self.__Bow.Bow_Print()
		self.__Player.set_Weapons(sword=self.__Sword, bow=self.__Bow, )

		#__ENEMY Setup__#
		COLDICT = self.__Collision_Logic.get_Col_Dict()
		for item in range(len(self.__Stal_Roster)):
			if self.__Stal_Roster[item] in COLDICT.keys():
				r_Stal = COLDICT[self.__Stal_Roster[item]]
				r_Stal.stalfos_setUP(self.__Sc_Width, self.__Sc_Height)
				# r_Stal.Stalfos_Print()

		#__Border Walls__#
		#for now wall is substituted with Sword2.png
		wall_Height, wall_Width = self.__Wall.get_Size()
		width = self.__Sc_Width / wall_Width
		height = self.__Sc_Height / wall_Height
		for item in range(width):
			self.__Wall.Wall_setUP(wall_Width*(item+1), 0)



		#_Weapon SETUP_#
		self.__projDict['#arrow'] = Arrow_Main()
		self.__projDict['#arrow'].copy_Node(self.__Projectiles)
		self.__Bow.set_ammo(self.__projDict['#arrow'])

		#_CLOCK SETUP_#
		self.__Timer.GameClock()


	#gameLoop def is for the classes use.
	def gameLoop(self):

		#to kill the window
		self.close_window()
		# self.new_Player()

		"""#_calls_#"""

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
				# print('Player_Attack = False, A#132')
				pass
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

		if self.__Sword.get_isActive() == True:
			list1.append(self.__Sword.get_Corners())
		if self.__Bow.get_isActive() == True:
			list1.append(self.__Bow.get_Corners())
		if self.__projDict['#arrow'].get_isActive() == True:
			list1.append(self.__projDict['#arrow'].get_Corners())


		self.__Collision_Logic.add_Collision(list1)

		#Below are representation of object corners
		player 	= 1
		sword 	= self.__Sword.get_itemCount()
		bow		= self.__Bow.get_itemCount()
		proj 	= self.__projDict['#arrow'].get_itemCount()
		#self.__stalfosCount represents number of stalfo's and their corners
		#when more enemies exist create more 'enemyName'Count, then add below.
		for item in range(player + sword + bow + proj + self.__stalfosCount):
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
						# 	pass

					if Col_result[item].get_ID() in self.__Stal_Roster:
						if item == len(Col_result)-1:
							pass
						elif item != len(Col_result)-1:
							if Col_result[item+1].get_group_ID() in self.__weaponRoster:
								Col_result[item].my_Collision(str(Col_result[item+1].get_ID()), Col_result[item+1].get_attack())
							elif Col_result[item+1].get_group_ID() in self.__projRoster:
								Col_result[item].my_Collision(str(Col_result[item+1].get_ID()), Col_result[item+1].get_attack())
								Col_result[item+1].del_Arrow()

					if Col_result[item] == self.__Sword: #weapon will always be last
						#print('Sword')
						pass

		#_Combat_#
		if self.__Sword.get_isActive() == True:
			self.__Sword.Weapon_Active()

		if self.__Bow.get_isActive() == True:
			self.__Bow.Weapon_Active()

		if self.__Bow.get_projActive() == True:
			self.__Bow.proj_Active()

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
