from PIL import ImageTk, Image
from lvlDesigner import *
from z_Pictures import *
from colored import fg
from tkinter import *
from Weapons import *
from Engine import *
from Entity import *
import keyboard

class Alpha():
	def __init__(self):
		self.__Sc_Width	 = 1280
		self.__Sc_Height = 800
		self.__version	 = "Stab Simulator [BETAv.1.1]"

		#this will be a growing list of group tags. It is hard set to refer here for spacific groups
		'''#_Player Tags_#'''
		self.__playerRoster = []

		'''#_Enemy Variables_#''' #include a list of tags for each enemy
		self.__enemyRoster	= ["#stalfos", ]

			#_Stalfos_#
		self.__stalfosRoster = []
		self.__stalfosCount  = 1


		'''#_Weapon Parameters_#'''
		self.__weaponRoster	= ["#sword", "#bow", ]
		self.__projRoster	= ['#arrow', ]

		'''#_Static Parameters_#'''
		self.__staticRoster = ['#wall', '#floor', ]
		self.__wallRoster	= []

		#other classes
		self.__MGF = Maps_GetFile()
		#collision logic v2.
		self.__cLogic = Collision_Logic(self.__staticRoster)
		self.__cNode  = Collision_Node(self.__cLogic)

		#below is class Calling
		self.__mainApp		= Tk()
		self.__Node 		= Node()
		self.__tNode		= Timer_Node(self.__mainApp)
		self.__iNode		= Image_Node() #calls to other classes called need self.Img_Node
		self.__kNode		= Kinetics_Node(self.__iNode)
		self.__Entities		= All_Entities()
		self.__Projectiles  = Projectiles()
		self.__Player		= Player_Main(self.__cLogic, self.__cNode, self.__iNode, self.__kNode)
		self.__Sword		= Sword_Main(self.__iNode, self.__cLogic)
		self.__Bow			= Bow_Main(self.__iNode, self.__cLogic, self.__cNode, self.__kNode)

		#from level Designer
		self.__GUI	= GUI_Main(self.__cLogic, self.__iNode, self.__kNode, self.__cNode, self.__mainApp, None)
		self.__GUI.gridSETUP()
		self.__eGUI = self.__GUI.get_eGUI()
		self.__siFILE = self.__GUI.get_siFILE()
		self.__cLogic.set_grid(self.__eGUI.get_grid())

		#yes
		self.__Entities.set_mainApp(self.__mainApp)
		self.__Projectiles.set_Nodes(self.__iNode, self.__kNode, self.__cLogic)

		#Level Location Imports
		self.__levelONE   = self.__MGF.get_levelONE()
		self.__levelTWO   = self.__MGF.get_levelTWO()
		self.__levelTHREE = self.__MGF.get_levelTHREE()
		self.__levelFOUR  = self.__MGF.get_levelFOUR()



		#_#Collision SETUP#_#
		"""Entities"""
		#player
		self.__cLogic.addColDict(tagOrId=self.__Player.get_ID(), obj=self.__Player)
		self.__playerRoster.append(self.__Player.get_ID())
		self.__cNode.set_playerRoster(self.__playerRoster)

		#Static Entities
		self.__imgDICT = None
		self.__cNode.set_staticRoster(self.__staticRoster)

		#Stalfos collision setup
		for item in range(self.__stalfosCount):
			if item < 10:
				ID = "S#00" + str(item)
			elif item >= 10 and item < 100:
				ID = "S#0" + str(item)
			self.__stalfosRoster.append(ID)
			stalMain = Stalfos_Main(self.__iNode, self.__cLogic, self.__cNode, self.__kNode, ID=ID)
			self.__cLogic.addColDict(tagOrId=ID, obj=stalMain)
		self.__cNode.set_stalfosRoster(self.__stalfosRoster)
		self.__cNode.set_enemyRoster(self.__enemyRoster)

		"""Items"""
		self.__cLogic.addColDict(self.__Sword.get_ID(), self.__Sword)
		self.__cLogic.addColDict(self.__Bow.get_ID(), self.__Bow)
		self.__cNode.set_weaponRoster(self.__weaponRoster)

		"""Projectiles"""
		#A func created in collision logic will set up projectiles, and that func will get
		#called inside of the class that uses the projectile.
		#this remains
		self.__cNode.set_projRoster(self.__projRoster)



		#temp val
		self.__loopCount = 33
		self.__Seconds   = 0


	def tk_windowSETUP(self):
		self.__mainApp.title(self.__version)
		self.__mainApp.geometry(str(self.__Sc_Width) + 'x' + str(self.__Sc_Height))

	def set_MainCanvas(self): #Set Renders HERE
		self.__iNode.Create_Canvas(self.__mainApp, self.__Sc_Height, self.__Sc_Width)


	def close_window(self): #putting this on HOLD
		if keyboard.is_pressed('q') == True:
			print('<------------------------->')
			print('<-----------END----------->')
			print('<------------------------->')
			self.__mainApp.destroy()
			return True

	def GamesetUP(self, GC_OFF=False):
		# #__Statics SETUP__#
		# print('temporary shutdwon at GameSetUP')
		self.__siFILE.Read_File(self.__levelFOUR)
		self.__imgDICT = self.__siFILE.get_imgDICT()

		for tag in self.__imgDICT.keys():
			self.__cLogic.addColDict(tagOrId=tag, obj=self.__imgDICT[tag])
			self.__cLogic.add_Collision(LVD_Corner=self.__imgDICT[tag].get_Corners())
			self.__wallRoster.append(tag)
		self.__cNode.set_wallRoster(self.__wallRoster)

		#Bellow is Entity set up
		self.__Player.player_setUP(x=96, y=160)
		# self.__Player.Player_Print()
		self.__Sword.sword_setUP()
		# self.__Sword.Sword_Print()
		self.__Bow.bow_setUP()
		# self.__Bow.Bow_Print()
		self.__Player.set_Weapons(sword=self.__Sword, bow=self.__Bow, )

		#__ENEMY Setup__#
		COLDICT = self.__cLogic.get_Col_Dict()
		for item in range(len(self.__stalfosRoster)):
			if self.__stalfosRoster[item] in COLDICT.keys():
				r_Stal = COLDICT[self.__stalfosRoster[item]]
				r_Stal.stalfos_setUP(self.__Sc_Width, self.__Sc_Height)
				# r_Stal.Stalfos_Print()


		#_Weapon SETUP_#

		#_CLOCK SETUP_#
		self.__tNode.GameClock(GC_OFF)


	#gameLoop def is for the classes use.
	def gameLoop(self):

		#to kill the window
		a = self.close_window()
		if a == True:
			return
		# self.new_Player()


		"""#_loop Debug_#"""
		# self.debug_Col_Dict() #workes

		"""#_Entity Loop Calls_#"""
			#_PLAYER_#
		if self.__Player.get_isAlive() == True:
			self.__Player.Player_MAttack()
			self.__Player.Player_RAttack()
			# self.__cLogic.ForT_Collision(self.__Player)
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
		Col_Dict = self.__cLogic.get_Col_Dict()
		for tag in self.__stalfosRoster:
			stalfos = Col_Dict[tag]
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
		for item in range(len(self.__stalfosRoster)):
			c_Stal = self.__cLogic.tagToObj(self.__stalfosRoster[item]) #c_Stal == stalfos obj
			list1.append(c_Stal.get_Corners())

		if self.__Sword.get_isActive() == True:
			list1.append(self.__Sword.get_Corners())
		if self.__Bow.get_isActive() == True:
			list1.append(self.__Bow.get_Corners())
		for item in range(len(self.__Bow.get_projID())):
			# print(self.__Bow.get_projID(item), 'proj ID, A#189')
			if self.__Bow.get_projActive(item) == True:
				list1.append(self.__Bow.get_projCorners(item))

		self.__cNode.use_Collision(list1, len(list1))



		#_Combat_#
		if self.__Sword.get_isActive() == True:
			self.__Sword.Weapon_Active()

		if self.__Bow.get_isActive() == True:
			self.__Bow.Weapon_Active()

		for item in range(len(self.__Bow.get_projID())):
			if self.__Bow.get_projActive(item) == True:
				self.__Bow.proj_Active(item)

		if self.__Player.get_isHit() == True:
			self.__Player.reset_hit()

		Col_Dict = self.__cLogic.get_Col_Dict()
		for item in range(len(self.__stalfosRoster)):
			result = Col_Dict[self.__stalfosRoster[item]]
			if result.get_isHit() == True:
				print('got hit')
				result.reset_hit()


		self.__mainApp.after(int(self.__tNode.get_FPS()), self.gameLoop)




	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_mainAPP(self):
		return self.__mainApp


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_ForT(self, ForT):#ForT == False or True, ForT
		self.__ForT = ForT



	"""#|--------------Extra Functions--------------|#"""

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
			self.__cLogic.print_Col_Dict()
			self.__cLogic.del_Col_Dict(self.__Player.get_ID())
			self.__cLogic.print_Col_Dict()

	#this is a function call for test prints to make sure things work
	def Testing_Debug(self):
		# self.find_all_Tags()
		# self.debug_Col_Dict()
		# print(Image_Node.Render, 'Render')
		pass


#puts the above class to action
color = fg('light_cyan')
Game = Alpha()
print('----------------------------\n'+color) #to make it easier to read in the command promt
Game.set_MainCanvas()
Game.tk_windowSETUP()
Game.GamesetUP(False)
Game.Testing_Debug()
print('----------------------------')
Game.gameLoop()
Game.get_mainAPP().mainloop()
