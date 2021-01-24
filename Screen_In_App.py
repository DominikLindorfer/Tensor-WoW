# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:55:26 2021

@author: dl
"""

from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
from PIL import ImageGrab

def screen_record(xoff = 260, yoff = 984, wx = 50, wy = 50): 
    printscreen =  np.array(ImageGrab.grab(bbox=(xoff - wx, yoff - wy, xoff + wx, yoff + wy)))
    return printscreen

image = screen_record(1480, 682, 28, 28)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image',printscreen_CDs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image_name = 'bla.jpg'

# image = cv2.imread(image_name)

#Rearrang the color channel
# b,g,r = cv2.split(image)
# img = cv2.merge((r,g,b))

# A root window for displaying objects
root = Tk()  

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im) 

# Put it in the display window
Label(root, image=imgtk).pack() 


# image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
# image = ImageTk.PhotoImage(image=Image.fromarray(image))
label_image = Label(self.detection, image=image)
label_image.image = image
label_image.place(x=0, y=0, anchor="w")


root.mainloop() # Start the GUI
