from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

#imporst for the different scrypts that controll the frames
import importSCR
#import nodesSC

mainApp = Tk()
mainApp.title('Basic Engine')
#mainApp.iconbitmap('E:/Aseprite_Art/FirstTKTUT/pikeLabs_icon.ico')
mainApp.geometry("1920x1080")

#main portion of the code

#   Creation of the frames
#this can't be shrunk with classes
fileProj = LabelFrame(mainApp,text="Project Window",width=300,height=1000)
gameEdit = LabelFrame(mainApp,text='Game View',width=1320,height=800)
outputSC = LabelFrame(mainApp,text='Error Return/output',width=1320,height=200)
nodes = LabelFrame(mainApp,text='Nodes',width=300,height=500,padx=5,pady=5)
Imports = LabelFrame(mainApp,text='Import Pictures',width=300,height=500,padx=10,pady=10)
ImportFrameHOLD = LabelFrame(Imports,text='Imported Images go here',width=280,height=200)


#the below is what places the frames in the correct place
#currently set up for a 1920x1080 screen size and isn't adaptable
fileProj.grid(row=0,column=0,rowspan=6)
gameEdit.grid(row=0,column=1,rowspan=3)
outputSC.grid(row=3,column=1,rowspan=3)
nodes.grid(row=0,column=2,rowspan=2)
Imports.grid(row=2,column=2,rowspan=2)
ImportFrameHOLD.grid(row=1,column=0,columnspan=5)

#   For any additional frames are created they need to be run through this
#      Lineof code,   If the unexpected happens check this line.
#use this to set width and Height that ignore the text inside buttons, frames & ect.
for frame in [fileProj, gameEdit, outputSC, nodes, Imports, ImportFrameHOLD]:
    frame.grid_propagate(0)

#Import Frame GUI size, shape and functionality
Import = Button(Imports, text='Import',width=6,height=2,)#command=)


#import frame GUI positions
Import.grid(row=0,column=0)


#use this to ignore the included insides of buttons or frames
for frame in [Import]:
    frame.grid_propagate(0)

#   GUI interface for the Nodes Frame of the Engin
#these will be used to add temp buttons to format the location

#this will be used to add a node into the node tree below
add_node  = Button(nodes,text='+',width=5,height=2)
#empty space for now but latter I will put something in there latter
temp_button = Button(nodes,state=DISABLED,width=33,height=2,bg='Black')
#this will be a frame made to house the family tree of the nodes
Node_tree = LabelFrame(nodes,text='Node Tree',width=280,height=430)

#this is where I am going to pack the gui of the
#   nodes and the node tree.
add_node.grid(row=0,column=0)
temp_button.grid(row=0,column=1)
Node_tree.grid(row=1,column=0,columnspan=5)

#do not forget this
mainloop()
