"""This will be full of test functions, most of which will be coppied from online
   Here is so that I can visualise what they are showcasing."""


#opening files
import tkinter
import tkinter.filedialog

def openFileTest():
	root = tkinter.Tk()


	def display_image():
		f = tkinter.filedialog.askopenfilename(
		parent=root, initialdir='C:/Tutorial',
		title='Choose file')

		new_window = tkinter.Toplevel(root)

		image = tkinter.PhotoImage(file=f)
		l1 = tkinter.Label(new_window, image=image)
		l1.image = image
		l1.pack()


	b1 = tkinter.Button(root, text='Display image', command=display_image)
	b1.pack(fill='x')

	root.mainloop()


#Rotation of printed images
import time
import tkinter
from PIL import Image, ImageTk

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tkinter.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.process_next_frame = self.draw().__next__  # Using "next(self.draw())" doesn't work
        master.after(1, self.process_next_frame)

    def draw(self):
		image = Image.open(self.filename)
		angle = 0
		print(self.process_next_frame)
		while True:
			#"""!!__HERE__!!"""
			tkimage = ImageTk.PhotoImage(image.rotate(angle)) #"""!!__HERE__!!"""
			# ^^The above line is the basis of img rotation, use this to further better combat graphics
			canvas_obj = self.canvas.create_image(250, 250, image=tkimage)
			self.master.after_idle(self.process_next_frame)
			yield
			self.canvas.delete(canvas_obj)
			angle += 1
			angle %= 360
			time.sleep(0.002)

def rotateImg():
	root = tkinter.Tk()
	app = SimpleApp(root, 'z_Pictures/BlueBoy2.png')
	root.mainloop()



from tkinter import *

def changeCursor():
	top = Tk()

	B1 = Button(top, text = "circle", relief = RAISED, \
	   cursor = "circle")
	B2 = Button(top, text = "plus", relief = RAISED, \
	   cursor = "plus")
	B1.pack()
	B2.pack()
	top.mainloop()


# from tkinter import *
# root = Tk()
# canvas = Canvas(root, width=800, height=600)
# canvas.pack()
#
# bg = PhotoImage(file="E:\Github\Game_Repos_1\Game(1.1)\z_Pictures\saki.png")
#
# mapimg = canvas.create_image(0, 0, image=bg, anchor="nw")
#
# gx, gy = 0, 0
# old_event = None
# dragged = False
#
# def drag(event):
# 	global dragged, old_event
# 	old_event = event
# 	dragged = True
#
# def release(event):
# 	global dragged
# 	dragged = False
#
# def moveimg(event):
# 	global mapimg, gx, gy, old_event
# 	if dragged:
# 		gx, gy = gx + (event.x - old_event.x), gy + (event.y - old_event.y)
# 		old_event = event
# 		canvas.coords(mapimg, gx, gy)
#
# root.bind("<Button-1>", drag)
# root.bind("<ButtonRelease-1>", release)
# root.bind("<Motion>", moveimg)
# root.mainloop()

import tkinter as tk
#shows what widget the mouse is in
def print_widget_under_mouse(root):
	x,y = root.winfo_pointerxy()
	widget = root.winfo_containing(x,y)
	print("widget:", widget)
	root.after(1000, print_widget_under_mouse, root)

root = tk.Tk()
label_foo = tk.Label(root, text="Foo", name="label_foo")
label_bar = tk.Label(root, text="Bar", name="label_bar")
button = tk.Button(root, text="Button", name="button")

button.pack(side="bottom")
label_foo.pack(fill="both", expand=True)
label_bar.pack(fill="both", expand=True)

print_widget_under_mouse(root)

root.mainloop()



#def calls
# openFileTest()
# rotateImg()
# changeCursor()
