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
			"""!!__HERE__!!"""
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


#def calls
# openFileTest()
# rotateImg()
