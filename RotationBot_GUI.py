# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:42:05 2021

@author: dl
GUI for WoW Rotation Bot
"""
from tkinter import * 
from threading import Thread

#-----Main Window-----
root = Tk()
root.title("WoW RotationBot GUI")
root.geometry("500x500")

app = Frame(root)
app.grid()

# #-----Set Logo on Top-----
# import PIL
# import PIL.Image as Image
# import PIL.ImageTk as ImageTk

# fp = open("Logo.jpeg","rb")
# image = PIL.Image.open(fp)
# photo = PIL.ImageTk.PhotoImage(image)
# # logo = Label(image=photo)

# label = Label(root, image = photo)
# label.image = photo
# label.grid(row=0, column=0, columnspan = 1)

# logo.grid(row=0, column=0, columnspan=3)

#-----Find WA Position on Screen (click on anchor in the middle)-----
from pynput import mouse    

def on_move(x, y):
    Label_WAPosition["text"] = 'Pointer moved to {0}'.format((x, y))
    print('Pointer moved to {0}'.format((x, y)))

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
    
def thread_findmouse():
    # Create and launch a thread 
    t = Thread(target = find_mouseposition)
    t.start()

Label_WAPosition = Label(master=app, text="WeakAura Position on Screen")
Label_WAPosition.grid(row=1, column=1)

Button_WAPosition = Button(master=app, text="Get WA Position", command=thread_findmouse)
Button_WAPosition.grid(row=1, column=0, sticky="nsew")

#-----Find Path of the Config File-----
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#-----File Stuff-----
Config_Filepath = "F:/WoW-RotBot/Config.dat"
def open_configfile():

    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )

    if not filepath:
        return
    
    Label_Filepath_Config["text"] = filepath
    global Config_Filepath
    Config_Filepath = filepath
    print(Config_Filepath)
        
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

Button_OpenConfigFile = tk.Button(app, text="Open Config File", command=open_configfile)
Button_OpenConfigFile.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

Label_Filepath_Config = Label(master=app, text="Config File Path")
Label_Filepath_Config.grid(row=2, column=1)


#-----Actual Bot Main Routine-----
def stop():
    # Assign global variable and set value to stop
    global stop
    stop = 1

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

import numpy as np
from PIL import ImageGrab
import cv2
import time
import random
from skimage.measure import compare_ssim
from directkeys import PressKey, ReleaseKey, W, A, S, D, dict_hkeys

#-----Read Screen Image-----
def screen_record_show(xoff = 260, yoff = 984, wx = 50, wy = 50): 
    last_time = time.time()
    while(True):
        # printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        # top = 1920
        # bot = 1080
        # xoff = 260 #960
        # yoff = 984
        # wx = 50
        # wy = 50
        
        printscreen =  np.arra3y(ImageGrab.grab(bbox=(xoff - wx, yoff - wy, xoff + wx, yoff + wy)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def screen_record(xoff = 260, yoff = 984, wx = 50, wy = 50): 
    last_time = time.time()
    printscreen =  np.array(ImageGrab.grab(bbox=(xoff - wx, yoff - wy, xoff + wx, yoff + wy)))
    return printscreen

import os
import ast 

def get_config(Config_Filepath):
   f = open(Config_Filepath, "r")
   f.readline()
   icon_dir = f.readline().rstrip() 
   
   f.readline()
   spells = list(f.readline().rstrip().split(" "))
   f.readline()
   cooldowns = list(f.readline().rstrip().split(" "))
   
   f.readline()
   hotkeys = ast.literal_eval(f.readline().rstrip()) 
   f.readline()
   hotkeys_CDs = ast.literal_eval(f.readline().rstrip()) 
   
   return icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs
   
# ini_list = "[1, 2, 3, 4, 5]"
# # printing initialized string of list and its type 
# print ("initial string", ini_list) 
# print (type(ini_list)) 
# # Converting string to list 
# res = ast.literal_eval(ini_list) 
# # printing final result and its type 
# print ("final list", res) 
# print (type(res)) 

def RotBot_main():
    #-----Main Rotation-Bot Routine-----
    first_run = True
    global Config_Filepath
    
    icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs = get_config(Config_Filepath)
    print(icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs)
    
    #-----Set Directory-----
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Paladin/"
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Monk/"
    
    #-----List of Icons-----
    # spells = ["bloodboil", "deathanddecay", "deathcoil", "deathstrike", "heartstrike", "marrowrend"]
    # spells = ["bladeofjustice", "judgement", "templarsverdict", "wakeofashes", "hammerofwrath", "crusaderstrike", "flashheal"]
    # spells = ["blessedhammer", "divinetoll", "judgement", "avengersshield", "hammerofwrath", "consecration"]
    # spells = ["Tigerpalm" , "Blackout", "Kegsmash", "Rushingjadewind", "Cranekick", "Breath"]
    icons = []
    for spell in spells:
        icons.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    # cooldowns = ["ardentdefender", "avengingwrath", "shieldofvengeance", "acientkings", "wordofglory", "seraphim", "peacebloom"]
    # cooldowns = ["Healingelixir", "Blackox", "Purifying", "Niuzao", "Celestial", "Weaponsoforder", "Fortifyingbrew", "Legkick", "peacebloom", "Touchofdeath"]
    icons_CDs = []
    for spell in cooldowns:
        icons_CDs.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    print()
    print("Icons: ")
    print(icons, icons_CDs)
    
    hotkeys = np.array(hotkeys)
    hotkeys_CDs = np.array(hotkeys_CDs)
    
    print(hotkeys, hotkeys_CDs)
    print(type(hotkeys))
    
    # return True
    #-----List of Hotkeys-----
    # hotkeys = np.array(["3","F","1","2","G","Q"])
    # hotkeys_CDs = np.array([["LSHIFT", "3"], ["LSHIFT", "E"], ["4"], ["LSHIFT", "F"], ["E"],  ["LCONTROL", "3"], []])
    # hotkeys = np.array(["1","2","E","F","4","3"])
    # hotkeys_CDs = np.array([["LCONTROL", "Q"], ["LCONTROL", "E"], ["LALT", "2"], ["LALT", "1"], ["LALT", "3"],  ["LALT", "5"], ["LSHIFT", "4"], ["LSHIFT", "E"], [], ["G"]])
    
    #-----Set IconSize-----
    icon_dim = (56,56)
        
    while True:
        if stop == 1:
            break
        
        # global idx
        # idx = idx+1
        # print (idx)
        
        #-----Read Screen and Compare to Icons-----
        
        #-----Check if Character is in Combat? -> Red (<100) = Combat, Green  (>100) = Not in Combat----
        printscreen = screen_record(1493, 798, 5, 5)
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        if(printscreen.sum()/100 > 100):
            print("Not in Combat! (Score = ", printscreen.sum()/100, ")")
            time.sleep(random.uniform(0,0.2))
            continue
        
        #-----Resize Images to icon_dim-----
        printscreen = screen_record(1480, 580, 28, 28)
        printscreen = cv2.resize(printscreen, icon_dim, interpolation = cv2.INTER_LINEAR)
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('image',printscreen)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        printscreen_CDs = screen_record(1480, 682, 28, 28)
        printscreen_CDs = cv2.cvtColor(printscreen_CDs, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('image',printscreen_CDs)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        if(first_run):
            # printscreen_old = printscreen
            time.sleep(3)
            first_run = False
            
        #-----Compare Screen to saved Icons using SSIM-----
        scores = np.array([])
        scores_CDs = np.array([])
        
        #-----stack ssim_score and hotkeys and sort descending afterwards-----
        for icon in icons:
            (score, diff) = compare_ssim(printscreen, icon, full=True)
            scores = np.append(scores, score)
            # scores = np.concatenate((scores, np.array([[score, numb]])))
            # print("SSIM: {}".format(score))
            
        for icon in icons_CDs:
            (score_CDs, diff) = compare_ssim(printscreen_CDs, icon, full=True)
            scores_CDs = np.append(scores_CDs, score_CDs)
            # scores = np.concatenate((scores, np.array([[score, numb]])))
            # print("SSIM: {}".format(score))
    
        sh_arr = np.stack((scores, hotkeys), axis=1)
        sh_arr = sh_arr[np.argsort(sh_arr[:, 0])][::-1]
        
        sh_arr_CDs = np.stack((scores_CDs, hotkeys_CDs), axis=1)
        sh_arr_CDs = sh_arr_CDs[np.argsort(sh_arr_CDs[:, 0])][::-1]
        
        # # #-----Skip Spell if there is no match-----
        # # if(np.max(sh_arr) < 0.05):eeeeeeeeeeeeeee
        # #     time.sleep(random.uniform(0,0.1))
        # #     # continue
        
        #-----Select Direct Input Key to press-----
        #-----Cooldowns First-----
        if(sh_arr_CDs[0,0] > 0.1):
            print(sh_arr_CDs[0,1])
            for key_CDs in sh_arr_CDs[0,1]:
                PressKey(dict_hkeys["_" + key_CDs])
                time.sleep(random.uniform(0,0.1))
                
            for key_CDs in sh_arr_CDs[0,1]:
                ReleaseKey(dict_hkeys["_" + key_CDs]) 
                time.sleep(random.uniform(0,0.1))
        
        #-----Spells Second-----
        print(sh_arr[0,1])
        key = dict_hkeys["_" + sh_arr[0,1]]
        PressKey(key)
        ReleaseKey(key)
        time.sleep(random.uniform(0,0.3))

def start_RotBot():
    # Assign global variable and initialize value
    global stop
    stop = 0
    
    global Config_Filepath
    # print(Config_Filepath)
    # Create and launch a thread 
    t = Thread(target = RotBot_main)
    t.start()

Button_Start = Button(app, text="Start Scan",command=start_RotBot)
Button_Stop = Button(app, text="Stop",command=stop)

Button_Start.grid(row=3, column=0)
Button_Stop.grid(row=3, column=1)

app.mainloop() 


import os

dir = '.'

# for dirname, _, filenames in os.walk(dir):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
        
f = open("Config.dat", "r")
# print(f.read()) 

f.readline()


for x in f:
    if(x == "-Icon Directory"):
        dir = a
        
    
    print(x) 

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
