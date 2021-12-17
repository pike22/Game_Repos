def use_Bow(self, x, y, direction):
		ID = self.__info.get_ID()
		group_ID = self.__info.get_group_ID()
		height, width = self.__info.get_size()
		if self.__isActive == False:
			self.__Image.Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=ID)
			self.__cLogic.add_Col_Dict(self.__ammo.get_ID(), self.__ammo)

			if direction == 'up':
				self.__ammo.use_Arrow(x, (y-width), 'up', dmgMod=self.__info.get_attackMOD())
			elif direction == 'down':
				self.__ammo.use_Arrow(x, (y+width), 'down', dmgMod=self.__info.get_attackMOD())
			elif direction == 'right':
				self.__ammo.use_Arrow((x+height), y, 'right', dmgMod=self.__info.get_attackMOD())
			elif direction == 'left':
				self.__ammo.use_Arrow((x-height), y, 'left', dmgMod=self.__info.get_attackMOD())


			Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
			self.__info.set_Canvas_ID(Canvas_ID)
			Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
			self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
			self.__saveTime = Timer_Node.GameTime
			self.__isActive = True
			self.__projActive = True
			self.__itemCount += 1

def use_Bow(self, x, y, direction):
	ID = self.__info.get_ID()
	group_ID = self.__info.get_group_ID()
	height, width = self.__info.get_size()
	if self.__isActive == False:
		#intial bow render and variable updates
		self.__Image.Img_Place(x, y, self.__info.get_TKimg(), Grid='No', tag=ID)
		self.__projActive = True
		self.__isActive   = True
		self.__projCount += 1
		self.__itemCount += 1

		#this creates arrow and saves the current state to collision
		self.__ammo = Arrow_Main(self.__cLogic, self.__cNode, self.__projCount)
		self.__cLogic.add_Col_Dict(tagOrId=self.__ammo.get_ID(), obj=self.__ammo)

		#this is for what direction the arrow flies
		if direction == 'up':
			self.__ammo.use(x, (y-width), 'up', dmgMod=self.__info.get_attackMOD())
		elif direction == 'down':
			self.__ammo.use(x, (y+width), 'down', dmgMod=self.__info.get_attackMOD())
		elif direction == 'right':
			self.__ammo.use((x+height), y, 'right', dmgMod=self.__info.get_attackMOD())
		elif direction == 'left':
			self.__ammo.use((x-height), y, 'left', dmgMod=self.__info.get_attackMOD())

		#finishing the render of the bow
		Canvas_ID = Image_Node.Render.find_withtag(ID)[0] #finds my canvas ID numb.
		self.__info.set_Canvas_ID(Canvas_ID)
		Image_Node.Render.addtag_withtag(group_ID, Canvas_ID)
		self.__info.set_Corners(Image_Node.Render.bbox(Canvas_ID))
		self.__saveTime = Timer_Node.GameTime
