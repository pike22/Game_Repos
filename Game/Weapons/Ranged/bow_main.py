from Engine.timer_node import Timer_Node
from Engine.image_node import Image_Node
from .bow_info import Bow_Info
from .Projectiles import *

class Bow_Main():
	"""
	The main class the does everything that is with a bow.

	Methods
	-------
	init(iNode, cLogic, cNode, kNode)
		This is required when Bow_Main() is called		
	"""
	def __init__(self, iNode, cLogic, cNode, kNode):
		self.__iNode	 = iNode
		self.__cLogic	 = cLogic
		self.__cNode	 = cNode
		self.__kNode	 = kNode
		self.__info		 = Bow_Info()
		self.__ammo		 = None

		'''Bow Parameters'''
		self.__attack	  = 0
		self.__itemCount  = 0
		self.__saveTime   = 0
		self.__isActive   = False

		'''Projectile Parameters'''
		self.__projActive = False
		self.__projCount  = 0
		self.__projID	  = []


	def bow_setUP(self):
		"""
		Basic set up of the bow.
		"""
		#img setup
		Img_info = self.__iNode.Img_Add('z_Pictures/bow_.png')
		self.__info.Image_Data(Size=Img_info[1], PIL_img=Img_info[0], TK_img=Img_info[2], file_Location='z_Pictures/bow_.png')
		self.__info.Bow_Data(2) #check melee_info for well info.

		#self.output = self.Image.

	def use_Bow(self, x, y, direction):
		"""
		Displayes the weapon on screen as well as all of the parameters that go with it. This also creates the corisponding Projectile
		that is rendered then moves soon after. (Explained more in the Projectiles classes)

		Parameters
		---------
		direction : str
			The direction that the attack happens.
		x, y : int
			The coords that the weapon will be placed at.
		"""
		self.__info.set_Coords((x, y))
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		height, width = self.__info.get_size()
		if self.__isActive == False:
			#intial bow render and variable updates
			self.__isActive   = True
			self.__projCount += 1
			self.__itemCount += 1

			#this creates arrow and saves the current state to collision
			self.__ammo = Arrow_Main(self.__iNode, self.__cLogic, self.__cNode, self.__kNode, self.__projCount)
			self.__projID.append(self.__ammo.get_ID())
			self.__cLogic.addColDict(tagOrId=self.__ammo.get_ID(), obj=self.__ammo)

			#this is for what direction the arrow flies
			if direction == 'up':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 90)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
				self.__ammo.use(x, (y-width), 'up', dmgMod=self.__info.get_attackMOD())

			elif direction == 'down':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 270)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
				self.__ammo.use(x, (y+width), 'down', dmgMod=self.__info.get_attackMOD())


			elif direction == 'left':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 180)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
				self.__ammo.use((x-height), y, 'left', dmgMod=self.__info.get_attackMOD())

			elif direction == 'right':
				newIMG = self.__iNode.Img_Rotate(self.__info.get_PILimg(), 0)
				self.__info.set_TKimg(newIMG)
				self.__iNode.Img_Place(x, y, self.__info.get_TKimg(), tag=[ID, group_ID])
				self.__ammo.use((x+height), y, 'right', dmgMod=self.__info.get_attackMOD())

			#finishing the render of the bow
			Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
			self.__info.set_Canvas_ID(Canvas_ID)
			Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
			self.__saveTime = Timer_Node.GameTime

	def Weapon_Active(self):
		"""
		Deactivates the weapon after a set amount of time.
		"""
		if Timer_Node.GameTime == (self.__saveTime+9):
			Image_Node.Render.delete(self.__info.get_ID())
			self.__isActive = False
			self.__itemCount -= 1

	def proj_Active(self, numb=None):
		"""
		Checks if the projectile is active then calls the isActive().

		Parameters
		----------
		numb : int
			The number is pushed into a list to grab the corisponding projectile tag
		"""
		if numb != None:
			if self.__cLogic.tagToObj(self.__projID[numb]).get_isActive() == True:
				self.__cLogic.tagToObj(self.__projID[numb]).isActive()

	def del_item(self):
		"""
		Delets the displayed weapon image on the tkinter window.
		"""
		Image_Node.Render.delete(self.__info.get_ID())
		self.__isActive = False
		# self.__Collision.del_Col_Dict(self.__ammo.get_ID())
		# self.__ammo.del_Arrow()



	def Bow_Print(self):
		"""
		:meta private:
		"""
		#list of prints for start of program(players)
		print('-----------------------------------')
		print('Bow Data:')
		print(self.__info.get_ID(), '\t:ID') #should be None
		print(self.__info.get_Attack_Dmg(), '\t:Attck')
		print('-----------------------------------')
		print('')

		#this may not be needed, depends for now.
	def my_Collision(self):
		"""
		:meta private:
		"""
		pass



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_attackMOD(self):
		"""
		:meta private:
		"""
		return self.__info.get_AttackMOD()

	def get_attack(self):
		"""
		:meta private:
		"""
		return self.__attack

	def get_size(self):
		"""
		:meta private:
		"""
		return self.__info.get_size()

	def get_isActive(self):
		"""
		:meta private:
		"""
		return self.__isActive

	def get_Corners(self):
		"""
		:meta private:
		"""
		return self.__info.get_Corners()

	def get_Coords(self):
		"""
		:meta private:
		"""
		return self.__info.get_Coords()

	def get_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_ID()

	def get_group_ID(self):
		"""
		:meta private:
		"""
		return self.__info.get_group_ID()

	def get_itemCount(self):
		"""
		:meta private:
		"""
		return self.__itemCount


	"""#|---------Projectile-Getters--------|#"""

	def get_projCount(self):
		"""
		:meta private:
		"""
		return self.__projCount

	def get_projID(self, numb=None):
		"""
		:meta private:
		"""
		if numb == None:
			return self.__projID
		else:
			return self.__projID[numb]

	def get_projActive(self, numb=None):
		"""
		:meta private:
		"""
		if numb == None:
			if self.__projID == []:
				return False
		else:
			if self.__projID[numb] in self.__cLogic.listOfKeys():
				return self.__cLogic.tagToObj(self.__projID[numb]).get_isActive()

	def get_projCorners(self, numb=None):
		"""
		:meta private:
		"""
		if numb == None:
			pass
		else:
			return self.__cLogic.tagToObj(self.__projID[numb]).get_Corners()

	def get_projCoords(self, numb=None):
		"""
		:meta private:
		"""
		if numb == None:
			pass
		else:
			return self.__cLogic.tagToObj(self.__projID[numb]).get_Coords()

	def get_projClass(self, numb=None):
		"""
		:meta private:
		"""
		if numb == None:
			pass
		else:
			return self.__cLogic.tagToObj(self.__projID[numb])


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_IsWeapon(self, Fort):
		"""
		:meta private:
		"""
		self.__isActive = Fort

	def set_ammo(self, ammo):
		"""
		:meta private:
		"""
		self.__ammo = ammo
