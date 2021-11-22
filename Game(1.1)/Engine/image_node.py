from tkinter import * #requires tk for image work.
from PIL import ImageTk, Image #PIL = Pillow
from .node import Node

#__Render == Canvas
class Image_Node(Node):
	Render = None
	def __init__(self):
		Node.__init__(self)
		self.__gridSizeX = 64
		self.__gridSizeY = 64
		self.__Img_list  = [] #0 = PIL_img | #1 = size | #2 = TK_img
		self.__PlaceIMG_List	= [] # 'item' = Canvas ID for 'item'
		self.__PlaceCOR_List	= [] # 'item' = Cordanate Tuple for 'item' (x, y)
		self.__PlaveCOR  = None #this will replace the list varient

	def Img_Add(self, img_Location):
		#takes in the initail img
		self.__Img_list = []
		PIL_img = Image.open(str(img_Location))
		self.__Img_list.append(PIL_img)
		self.__Img_list.append(PIL_img.size)

		#converts im to an ImageTk
		self.__Img_list.append(ImageTk.PhotoImage(PIL_img))
		#Eventually a method of storage will be implimented

		## NOTE: self.Img_list is PIL, size, TK image in order of 0, 1, 2
		return self.__Img_list

	def Img_Place(self, x, y, image, Grid='yes', LVD='no', tag=None, render=None): # !!returns a tuple!!
		if Grid == "yes":
			if render == None:
				render = Image_Node.Render
				#x & y are grid coords not percise coords
				# each grid incrament is by 64.
				img_x = (x - 0.5) * self.__gridSizeX
				img_y = (y - 0.5) * self.__gridSizeY


				#print('3:', image)
				#print("coords", img_x, img_y)
				Canvas_ID = render.create_image((img_x, img_y), image=image,anchor="nw")
				if tag != None:
					Image_Node.Render.addtag_withtag(tag, Canvas_ID)
				self.__PlaceIMG_List.append(Canvas_ID)
				self.__PlaceCOR_List.append((img_x, img_y))
				return self.__PlaceCOR_List
				#this will place the img in the tkinter window.

		elif Grid != 'yes' and LVD == 'yes':
			img_x = x
			img_y = y

			#print('3:', image)
			#print("coords", img_x,',', img_y)
			Canvas_ID = render.create_image((img_x, img_y), image=image,anchor="nw")
			if tag != None:
				Image_Node.Render.addtag_withtag(tag, Canvas_ID)
			self.__PlaceIMG = Canvas_ID
			self.__PlaceCOR = (img_x, img_y)
			return self.__PlaceIMG

		elif Grid != 'yes': #this is if I want to use spacific coords for placement.
			if render == None:
				render = Image_Node.Render
				img_x = x
				img_y = y

				#print('3:', image)
				#print("coords", img_x,',', img_y)
				Canvas_ID = render.create_image((img_x, img_y), image=image,anchor="nw")
				if tag != None:
					Image_Node.Render.addtag_withtag(tag, Canvas_ID)
				self.__PlaceIMG_List.append(Canvas_ID)
				self.__PlaceCOR_List.append((img_x, img_y))
				return self.__PlaceCOR_List

	def Create_Canvas(self, mainApp, height, width, color='Blue'):
		Image_Node.Render = Canvas(mainApp, height=height, width=width, bg=str(color))
		Image_Node.Render.grid(row=0, column=0)
		Image_Node.Render.grid_propagate(0)

	#def Img_Render(self):
		#this is to render the img for the first time.
		#it will call on to Img_add & Img_place.
		#	(allow for placement based on grid or not grid.)


	"""#|--------------Getters--------------|#"""



	"""#|--------------Setters--------------|#"""
