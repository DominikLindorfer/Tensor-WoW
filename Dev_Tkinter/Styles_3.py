# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:44:36 2021

@author: dl
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:42:05 2021

@author: dl
GUI for WoW Rotation Bot
"""
from tkinter import * 
from threading import Thread
from win32gui import GetWindowText, GetForegroundWindow
from ttkthemes import ThemedStyle

#-----Main Window-----
root = Tk()
root.title("WoW Rot Bot")
root.geometry("500x520")

# root.configure(bg='Grey')
app = Frame(root)
app.configure(bg='White')
app.grid()

col_count = 10
row_count = 10

for col in range(col_count):
    app.grid_columnconfigure(col, weight=1, minsize=200)

for row in range(row_count):
    app.grid_rowconfigure(row, weight=1, minsize=25)

# #-----Set Logo on Top-----
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk

fp = open("LogoV3.png","rb")
image = PIL.Image.open(fp)
photo = PIL.ImageTk.PhotoImage(image)

label = Label(app, image = photo)
label.image = photo
label.grid(row=0, column=0, columnspan = 2)

def start_RotBot():
    return
def stop():
    return
def thread_findmouse():
    return
def open_configfile():
    return

def showWA_Pic():
    return

Spells_True = IntVar(value=1)
CDs_True = IntVar(value=1)
Covenant_True = IntVar(value=1)
Kick_True = IntVar(value=1)

import tkinter as tk
from tkinter import ttk
#-----Buttons-----        
Button_Start = ttk.Button(app, text="Start", command=start_RotBot, style="L.TButton")
# Button_Stop = ttk.Button(app, bg="Red", fg="Black", text="Stop", command=stop)
Button_Stop = ttk.Button(app, text="Stop", command=stop, style="L.TButton")
Button_Start.grid(row=1, column=0,sticky="nsew", padx=2, pady=2)
Button_Stop.grid(row=1, column=1,sticky="nsew", padx=2, pady=2)

Button_WAPosition = ttk.Button(master=app, text="Get WA Position", command=thread_findmouse)
Button_WAPosition.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
Button_OpenConfigFile = ttk.Button(app, text="Open Config File", command=open_configfile)
Button_OpenConfigFile.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

ttk.Checkbutton(app, text="Enable Spells", variable=Spells_True, style='Red.TCheckbutton').grid(row=5, column=1, sticky="w")
ttk.Checkbutton(app, text="Enable CDs", variable=CDs_True, style='Red.TCheckbutton').grid(row=6, column=1, sticky="w")
ttk.Checkbutton(app, text="Enable Covenant", variable=Covenant_True, style='Red.TCheckbutton').grid(row=7, column=1, sticky="w")
ttk.Checkbutton(app, text="Enable Kick", variable=Covenant_True, style='Red.TCheckbutton').grid(row=8, column=1, sticky="w")

Button_showWA_Pic = ttk.Button(master=app, text="Get WA Pictures", command=lambda:showWA_Pic(label_showWA_Spells, label_showWA_CDs, label_showWA_Covenant, WA_Position_Spells, WA_Position_CDs, WA_Position_Covenant))
Button_showWA_Pic.grid(row=10, column=0, sticky="nsew", padx=2, pady=2)



#-----Labels-----
Label_WAPosition = Label(master=app, text="WeakAura Position on Screen", bg = "White")
Label_WAPosition.grid(row=3, column=0, sticky="nsew")
Label_Filepath_Config = Label(master=app, text="Config File Path", bg = "White")
Label_Filepath_Config.grid(row=3, column=1, sticky="nsew")

Label_Utilities = Label(master=app, text="Utilities", bg = "White", font = 'helvetica 12 underline')
Label_Utilities. grid(row=4, column=1, sticky="w")

WA_img = []

label_showWA_Spells = Label(app, image = WA_img, bg = "White")
# label_showWA_Spells.image = WA_img
label_showWA_Spells.grid(row=4, column=0, rowspan = 2, sticky="nsew") 

label_showWA_CDs = Label(app, image = WA_img, bg = "White")
# label_showWA_CDs.image = WA_img
label_showWA_CDs.grid(row=6, column=0, rowspan = 2, sticky="nsew") 

label_showWA_Covenant = Label(app, image = WA_img, bg = "White")
# label_showWA_Covenant.image = WA_img
label_showWA_Covenant.grid(row=8, column=0, rowspan = 2, sticky="nsew") 
    
#-----Entries-----

style2 = ttk.Style()
style2.configure('D.TButton', background='Black', foreground='Red', darkcolor   ='Red', padding=10)

# style3 = ttk.Style()
# style3.configure('Red.TCheckbutton', background='White', foreground='Red')

style = ThemedStyle(root)
style.theme_names()
style.theme_use('arc')  # white style
style.configure('L.TButton', background='White', foreground='Black', font = 'Cambria 20')
style.configure('TButton', background='White', foreground='Black', font = 'Cambria 14')
style.configure('Red.TCheckbutton', background='White', foreground='Black', font = 'Cambria 12')
# style.configure('TButton', foreground='Black')

app.mainloop() 
