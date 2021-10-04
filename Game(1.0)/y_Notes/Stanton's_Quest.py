#---------------Stanton's Quest--------------------------------#
0: None #is a completed task
0:"Green" #is a task saved for later or put to the back burner.
#Here are some specific notes for the code:

1) None #Alpha.py - I would go through the effort to probably make the variables private.  It sounds like a pain, I know, but it's a good habit to get into.  If you switch to pretty much any other language you'll want that habit.

2) None #Alpha.py - I know it's early, but I'd still make an "enemies" array, and put a stalfos in the first entry of it.  It'll make your life easier going forward.  That'll let you add a loop to your setup to set up all enemies.

3) None #Gameloop and loop are really confusing.  I would do the following:  move the one time setup into gameloop and rename is something like gamesetup.   Create a separate definition "loop" that is the one that's called over and over again.

4) "Later"  #Kinetics_node - Might just make speed private, you already have the getter/setter.  Might want to make a general xy_kinetics method to handle diagonals if you plan to have them.  (I know you get this with your current logic, but it causes 2 redraws, a y and an x.  You could save some processor this way)

5)  #collision_logic - I'd change Possible_Collision to be "add_to_collision", and just have it either append to a list, you may want a dictionary here, because you might want the object as the key (like player), and the collision box as the value.  That'll let you return the exact object that's collided with.

6) #player_main - in movement control, just default moving to false before the if statements.  Then you don't need that long if statement at the bottom.  Might want to add a facing to this to make you able to attack in any direction.

7)  #If you add facing you can really improve player attack for 4 direction attacking


Big picture work:

1)  #Really get melee weapons working well before moving on.  If you add facing that will help.

2)  #I'd work on enemy motion next.  Have the bad guy moving around (without worrying about walls).  Test out some basic patrols (random motion okay) and maybe a controlled chase (pointing at the player).  That gets you early zelda style enemy logic.

3)  #Then I'd add walls and make sure collision doesn't break on this.  If not, awesome, if so, then you'll have to look into "is_intersecting" and see if it's more efficient.


#That should be plenty for the summer!  :)  Feel free to email me if you need anything.

Mr. Stanton
#--------------------------------------------------------------#

#---------------Adding tagsOrID--------------------------------#
from tkinter import *

root = Tk()
canvas = Canvas(root)
canvas.pack()

def printListOfCurrentObjects():
    listOfCanvasItems = canvas.find_all()
    for cID in listOfCanvasItems:
        tagList = canvas.gettags(cID)
        if (len(tagList) > 0):
            print('Item', cID, 'has tag:', tagList[0])

def add_canvas_item(x,y,tag):
    canvas_item_id = canvas.create_oval(x-50,y-50,x+50,y+50, fill='green')
    canvas.addtag_withtag(tag , canvas_item_id)

add_canvas_item(100,100,"bob")    # Test item 1
add_canvas_item(250,150,"alice")    # Test item 2


printListOfCurrentObjects()

root.mainloop()
