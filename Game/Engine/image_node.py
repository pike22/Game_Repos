from tkinter import * #requires tk for image work.
from PIL import ImageTk, Image #PIL = Pillow
# from .node import Node

#__Render == Canvas

class Image_Node():
	Render = None
	"""
	Render=Project Global Variable that holds the Canvas object.
	"""
	def __init__(self):
		# Node.__init__(self)
		self.__gridSizeX = 64
		self.__gridSizeY = 64
		self.__Img_list  = [] #0 = PIL_img | #1 = size | #2 = TK_img
		self.__PlaceIMG  = None #this will replace the list varient
		self.__PlaceCOR  = None #this will replace the list varient

	def Img_Add(self, img_Location):
		"""
		The target image is turned into a PIL and TKimage that can be used by
		tkinter. As well as returning the size of the image.

		Parameters
		----------
		img_Location
			the directory that the image file is stored
		"""
		#takes in the initail img
		self.__Img_list = []
		PIL_img = Image.open(str(img_Location))
		self.__Img_list.append(PIL_img)
		self.__Img_list.append(PIL_img.size)

		#converts im to an ImageTk
		self.__Img_list.append(ImageTk.PhotoImage(PIL_img))
		#Eventually a method of storage will be implimented

		## NOTE: self.Img_list == [PIL, size, TK image] in order of 0, 1, 2
		# print(self.__Img_list, 'PIL_img | size | TK_img')
		return self.__Img_list

	def Img_Rotate(self, pilImg, angle, LVD=False):
		"""
		Rotates the given image.

		Parameters
		----------
		pilIMG
			The target image for rotation
		angle
			The planned angle of rotation
		LVD
			Determin if mainGame or LVLDesigner is used
		"""
		# angle %= angle
		if LVD == True:
			pilImg = pilImg.rotate(angle, Image.NEAREST)
			tkImg  = ImageTk.PhotoImage(pilImg)
			return tkImg
		else:
			pilImg = pilImg.rotate(angle, Image.NEAREST)
			tkImg  = ImageTk.PhotoImage(pilImg)
			return tkImg

	def Img_Place(self, x, y, image, LVD='no', tag=None): # !!returns a tuple!! #Tag needs to be a list
		"""
		Places the target image at the given location

		Parameters
		----------
		x, y : tuple int
			Placement cordinants for the image.
		image
			Image to be placed
		LVD
			Determin if mainGame or LVLDesigner is used
		tag : str
			Tag to be attached to the target image.
		"""
		if LVD == 'no':
			Canvas_ID = Image_Node.Render.create_image((x, y), image=image, anchor="nw")
			if tag != None:
				if len(tag) > 1:
					for item in range(len(tag)):
						Image_Node.Render.addtag_withtag(tag[item], Canvas_ID)
				else:
					Image_Node.Render.addtag_withtag(tag, Canvas_ID)
			self.__PlaceIMG = Canvas_ID
			self.__PlaceCOR = (x, y)
			return self.__PlaceCOR

		elif LVD != 'no': #this is for the level designer
			Canvas_ID = Image_Node.Render.create_image((x, y), image=image, anchor="nw")
			if tag != None:
				if len(tag) > 1:
					for item in range(len(tag)):
						Image_Node.Render.addtag_withtag(tag[item], Canvas_ID)
				else:
					Image_Node.Render.addtag_withtag(tag, Canvas_ID)
			self.__PlaceIMG = Canvas_ID
			self.__PlaceCOR = (x, y)
			return self.__PlaceIMG


	def Create_Canvas(self, mainApp, height, width, color='Grey'):
		"""
		Creates the Canvas that will be used for both the mainGame and LVLDesigner

		Parameters
		----------
		mainApp
			tkinters class call variable name
		height
			height of the Canvas
		width
			width of the Canvas
		color
			Color of the Canvas
		"""
		Image_Node.Render = Canvas(mainApp, height=height, width=width, bg=str(color))
		Image_Node.Render.grid(row=0, column=0, rowspan=10)
		Image_Node.Render.grid_propagate(0)

	#def Img_Render(self):
		#this is to render the img for the first time.
		#it will call on to Img_add & Img_place.
		#	(allow for placement based on grid or not grid.)


	"""#|--------------Getters--------------|#"""



	"""#|--------------Setters--------------|#"""
