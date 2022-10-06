# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:58:06 2021

@author: dl
"""


# Import module  
from tkinter import *
  
# Create object  
root = Tk() 
  
# Adjust size  
root.geometry("500x500") 
  
# Specify Grid 
Grid.rowconfigure(root,0,weight=1) 
Grid.columnconfigure(root,0,weight=1) 
  
Grid.rowconfigure(root,1,weight=1) 
  
# Create Buttons 
button_1 = Button(root,text="Button 1") 
button_2 = Button(root,text="Button 2") 
  
# Set grid 
button_1.grid(row=0,column=0,sticky="NSEW") 
button_2.grid(row=1,column=0,sticky="NSEW") 
  
# Execute tkinter 
root.mainloop()
