#this is will be the logic scrypt for the import frame
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image

#add more to here for more functionality
#class ImportTAB:
    #I can add more here when creating more button functions
#    def __init__(self,IMG_import):
#        self.__IMG_import = filedialog.askopenfilename(initialdir='E:',title='select a file',filetypes=(('png files','*.png'),('All files','*.*')))

#    def IMG_import(self):
#        return self.__IMG_import

PicDict = {1:"hello"}

class PictureLIB:
    #setting up picturesDICT as a open var.
    def __init__(self,PicturesDICT):
        self.__PicturesDICT = PicDict

    #def add_picture(self,PictDict):
        #PicDict =

    def get_PicDict(self):
        return self.__PicturesDICT


Hello = PictureLIB(PicDict)

print(Hello.get_PicDict())
