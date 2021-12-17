

# this is for if I want to use a different variaent to the current img place def.
# the difference to this one is in how I push out the return variable because this
# is going to use temporary variables instead of constant ones. What I hope this does
# is prevents haveing to use my current method of finding things.


# !*!*!*!PROBALY WON'T GET USED AT ALL. WHAT I HAVE SHOUD WORK FINE AS LONG AS I ALWAYS PASS A -1 AFTER!*!*!*!.


def Img_Place(self, x, y, image, Grid='yes', tag=None): # !!returns a tuple!!
	if Grid == "yes":
		#x & y are grid coords not percise coords
		# each grid incrament is by 64.
		img_x = (x - 0.5) * self.__gridSizeX
		img_y = (y - 0.5) * self.__gridSizeY


		#print('3:', image)
		#print("coords", img_x, img_y)
		PlaceIMG_list = []
		PlaceCOR_list = []
		Canvas_ID = self.__Render.create_image((img_x, img_y), image=image)
		print(tag, "THIS IS THE TAG")
		if tag != None:
			self.__Render.addtag_withtag(tag, Canvas_ID)
		PlaceIMG_list.append(Canvas_ID)
		PlaceCOR_list.append((img_x, img_y))
		Var_tuple = (PlaceIMG_List, PlaceCOR_list)
		return Var_tuple
		#this will place the img in the tkinter window.
	else: #this is if I want to use spacific coords for placement.
		img_x = x
		img_y = y

		#print('3:', image)
		#print("coords", img_x,',', img_y)
		PlaceIMG_list = []
		PlaceCOR_list = []
		Canvas_ID = self.__Render.create_image((img_x, img_y), image=image)
		print(tag, "THIS IS THE TAG")
		if tag != None:
			self.__Render.addtag_withtag(tag, Canvas_ID)
		PlaceIMG_list.append(Canvas_ID)
		PlaceCOR_list.append((img_x, img_y))
		Var_tuple = (self.__PlaceIMG_List, PlaceCOR_list)
		return Var_tuple




#Collision_Node isn't needed if I don't use my own method for Collision
#!!!!!!*********!!!!!!!
