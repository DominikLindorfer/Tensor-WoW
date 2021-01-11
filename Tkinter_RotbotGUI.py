#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:28:39 2021

@author: lindorfer
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk
# from tkinter import *  

main_window = tk.Tk()
main_window.title("Rotbot GUI")
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10,
    height=10
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry(fg="yellow", bg="blue", width=50)

#-----Set Logo-----
fp = open("Logo.jpeg","rb")
image = PIL.Image.open(fp)
photo = PIL.ImageTk.PhotoImage(image)
logo = tk.Label(image=photo)

logo.pack()
button.pack()
label.pack()
entry.pack()

main_window.mainloop()
