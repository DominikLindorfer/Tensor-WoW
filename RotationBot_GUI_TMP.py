# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:42:05 2021

@author: dl
GUI for WoW Rotation Bot
"""
from tkinter import * 
from threading import Thread

idx = 0

def scanning():
    while True:
        global idx
        idx = idx+1
        print (idx)
        if stop == 1:   
            break   #Break while loop when stop = 1

def start_thread():
    # Assign global variable and initialize value
    global stop
    stop = 0

    # Create and launch a thread 
    t = Thread (target = scanning)
    t.start()

def stop():
    # Assign global variable and set value to stop
    global stop
    stop = 1

root = Tk()
root.title("Title")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan",command=start_thread)
stop = Button(app, text="Stop",command=stop)

#-----Find WA Position on Screen (click on anchor in the middle-----)
from pynput import mouse    
def on_move(x, y):
    Position_Value["text"] = 'Pointer moved to {0}'.format((x, y))
    print('Pointer moved to {0}'.format((x, y)))
    # Position_Value["text"] = "Test"

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# Collect events until released
def find_mouseposition():
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
    # listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    # listener.start()
    
def thread_findmouse():
    # Create and launch a thread 
    t = Thread(target = find_mouseposition)
    t.start()


start.grid()
stop.grid()

FindWA = Button(app, text="FindWA",command = thread_findmouse)
FindWA.grid()
Position_Value = Label(master=app, text="0")
Position_Value.grid(row=0, column=1)

def increase():
    value = int(Position_Value["text"])
    Position_Value["text"] = f"{value + 1}"

def changetext():
    Position_Value["text"] = "Text Changed by Button!"

btn_increase = Button(master=app, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

btn_changetext = Button(master=app, text="ChangeME!", command=changetext)
btn_changetext.grid(row=0, column=3, sticky="nsew")

btn_mp = Button(master=app, text="Mouse Position!", command=thread_findmouse)
btn_mp.grid(row=0, column=4, sticky="nsew")


#-----Simple Text Editor-----
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#-----File Stuff-----
def open_file():

    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )

    if not filepath:
        return
    
    Config_Filepath["text"] = filepath
    print(filepath)
    return filepath

def save_file():

    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

btn_open = tk.Button(app, text="Open", command=open_file)
btn_open.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

Config_Filepath = Label(master=app, text="")
Config_Filepath.grid(row=0, column=5)

app.mainloop() 


#-----Class Structured-----
# from tkinter import Tk, Label, Button

# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")

#         self.label = Label(master, text="This is our first GUI!")
#         self.label.pack()

#         self.greet_button = Button(master, text="Greet", command=self.greet)
#         self.greet_button.pack()

#         self.close_button = Button(master, text="Close", command=master.quit)
#         self.close_button.pack()

#     def greet(self):
#         print("Greetings!")

# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()


# # import tkinter module 
# from tkinter import * 
# from tkinter.ttk import *

# import PIL
# import PIL.Image as Image
# import PIL.ImageTk as ImageTk

# # creating main tkinter window/toplevel 
# master = Tk() 
  
# # this will create a label widget 
# l1 = Label(master, text = "Height") 
# l2 = Label(master, text = "Width") 
  
# # grid method to arrange labels in respective 
# # rows and columns as specified 
# l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
# l2.grid(row = 1, column = 0, sticky = W, pady = 2) 
  
# # entry widgets, used to take entry from user 
# e1 = Entry(master) 
# e2 = Entry(master) 
  
# # this will arrange entry widgets 
# e1.grid(row = 0, column = 1, pady = 2) 
# e2.grid(row = 1, column = 1, pady = 2) 
  
# # checkbutton widget 
# c1 = Checkbutton(master, text = "Preserve") 
# c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 
  
# # adding image (remember image should be PNG and not JPG) 
# #-----Set Logo-----
# fp = open("Logo.jpeg","rb")
# image = PIL.Image.open(fp)
# img1 = PIL.ImageTk.PhotoImage(image)
# # logo = tk.Label(image=photo)
# # img = PhotoImage(file = "Logo.jpeg") 
# # img1 = img.subsample(2, 2) 
  
# # setting image with the help of label 
# Label(master, image = img1).grid(row = 0, column = 2, 
#        columnspan = 2, rowspan = 2, padx = 5, pady = 5) 
  
# # button widget 
# b1 = Button(master, text = "Zoom in") 
# b2 = Button(master, text = "Zoom out") 
  
# # arranging button widgets 
# b1.grid(row = 2, column = 2, sticky = E) 
# b2.grid(row = 2, column = 3, sticky = E) 
  
# # infinite loop which can be terminated  
# # by keyboard or mouse interrupt 
# mainloop() 

# from tkinter import *
# root = Tk()

# frame = Frame(root)

# Button(frame, text="A").pack(side=LEFT, fill=Y)
# Button(frame, text="B").pack(side=TOP, fill=X)
# Button(frame, text="C").pack(side=RIGHT, fill=NONE)
# Button(frame, text="D").pack(side=TOP, fill=BOTH)
# frame.pack()
# # note the top frame does not expand nor does it fill in

# # X or Y directions
# # demo of expand options - best understood by expanding the root widget and seeing the effect on all the three buttons below.
# Label (root, text="Pack Demo of expand").pack()
# Button(root, text="I do not expand").pack()
# Button(root, text="I do not fill x but I expand").pack(expand = 1)
# Button(root, text="I fill x and expand").pack(fill=X, expand=1)
# root.mainloop()
