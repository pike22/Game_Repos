
#---------------Adding tagsOrID--------------------------------#
from tkinter import *

root = Tk()
canvas = Canvas(root)
canvas.pack()

#this gets all of the current tags and sorts them into a list.
def printListOfCurrentObjects():
    listOfCanvasItems = canvas.find_all()
    for cID in listOfCanvasItems:
        tagList = canvas.gettags(cID)
        if (len(tagList) > 0):
            print('Item', cID, 'has tag:', tagList[0])
			
#this is used to create objects and their tags.
def add_canvas_item(x,y,tag):
    canvas_item_id = canvas.create_oval(x-50,y-50,x+50,y+50, fill='green')
    canvas.addtag_withtag(tag , canvas_item_id)

add_canvas_item(100,100,"bob")    # Test item 1
add_canvas_item(250,150,"alice")    # Test item 2


printListOfCurrentObjects()

root.mainloop()
