# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:42:05 2021

@author: dl
GUI for WoW Rotation Bot
"""

#-----Library Imports-----
from tkinter import * 
from threading import Thread
from win32gui import GetWindowText, GetForegroundWindow

import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk

from tensorflow.keras.models import load_model
import tensorflow as tf

from os import walk


#-----Style-----
from lib.set_style import set_app_style

#-----Get Mouse Position------
from lib.get_mouse_position import thread_findmouse

#-----Get Settings & Configs -----
from lib.settings import get_Settings, get_config, open_configfile, save_file

#-----Get Screen Functions-----
from lib.screen_functions import showWA_Pic, screen_record, convert_rbg_to_int 

#-----Direckeys-----
from lib.directkeys import PressKey, ReleaseKey, W, A, S, D, dict_hkeys

#-----Setup TKInter Root and App-----
from lib.setup_windows import setup_app, setup_root, setup_buttons

#-----Setup Global Config -> Simplistic use for updateable system variables // not working atm-----
# import lib.config

#-----Main Window-----
root = Tk()
setup_root(root)

app = Frame(root)
setup_app(app)

# -----Set Logo on Top-----
fp = open("LogoV3.png","rb")
image = PIL.Image.open(fp)
photo = PIL.ImageTk.PhotoImage(image)

label = Label(app, image = photo)
label.image = photo
label.grid(row=0, column=0, columnspan = 2)

config_filepath = "C:/Users/Dominik/Programs/WoW-RotBot/Config/Config_Brewmaster.dat"
settings_path = "C:/Users/Dominik/Programs/WoW-RotBot/Settings.dat"

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
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim



WA_Position_Spells = [1480, 584, 28, 28]
WA_Position_CDs = [1480, 682, 28, 28]
WA_Position_Covenant = [1480, 782, 28, 28]
WA_Position_Combat = [1480, 832, 5, 5]
WA_Position_Kick = [1517, 832, 5, 5]
WA_Position_Spells, WA_Position_CDs, WA_Position_Covenant, WA_Position_Combat, WA_Position_Kick, WA_Position_Casting, WA_Position_Party = get_Settings(settings_path)

Spells_True = IntVar(value=1)
CDs_True = IntVar(value=1)
Covenant_True = IntVar(value=0)
Kick_True = IntVar(value=0)
Healer_True = IntVar(value=0)
   
def RotBot_main():
    #-----Main Rotation-Bot Routine-----
    first_run = True
    global config_filepath
    # config_filepath = filepath
    global WA_Position_Spells
    global WA_Position_CDs
    global WA_Position_Covenant
    global Spells_True
    global CDs_True
    global Covenant_True
    global Kick_True
    global Healer_True
    
    #-----Load CNN -----
    class_icons = "Monk/"
    filepath = './saved_model_icons/' + class_icons
    model = load_model(filepath, compile = True)

    print("RotBot Main Function, Filepath: ", config_filepath)

    icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party = get_config(config_filepath)
    print(icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party)
    
    #-----Set Directory-----
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Paladin/"
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Monk/"
    
    #-----List of Icons-----
    # spells = ["bloodboil", "deathanddecay", "deathcoil", "deathstrike", "heartstrike", "marrowrend"]
    # spells = ["bladeofjustice", "judgement", "templarsverdict", "wakeofashes", "hammerofwrath", "crusaderstrike", "flashheal"]
    # spells = ["blessedhammer", "divinetoll", "judgement", "avengersshield", "hammerofwrath", "consecration"]
    # spells = ["Tigerpalm" , "Blackout", "Kegsmash", "Rushingjadewind", "Cranekick", "Breath"]
    
    icons_filenames = []
    for (dirpath, dirnames, filenames) in walk(icon_dir):
        icons_filenames.extend(filenames)
        break 
    
    icons = []
    for spell in spells:
        icon = cv2.imread(icon_dir + spell + ".jpg", 0)
        
        if icon is None:
            print("Can't read: ", spell)
            return False

        icons.append(icon)
    
    # cooldowns = ["ardentdefender", "avengingwrath", "shieldofvengeance", "acientkings", "wordofglory", "seraphim", "peacebloom"]
    # cooldowns = ["Healingelixir", "Blackox", "Purifying", "Niuzao", "Celestial", "Weaponsoforder", "Fortifyingbrew", "Legkick", "peacebloom", "Touchofdeath"]
    icons_CDs = []
    for spell in cooldowns:
        icon = cv2.imread(icon_dir + spell + ".jpg", 0)
        
        if icon is None:
            print("Can't read: ", spell)
            return False
        
        icons_CDs.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    icons_covenant = []
    for spell in covenant:
        icons_covenant.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    # print("Icons: ")

    # for icon in icons:
    #     if icon == None:
    #         print("Cant Read an Icon!!!")
    #         return 1

    # for icon in icons_CDs:
    #     if icon == None:
    #         print("Cant Read an Icon!!!")
    #         return 1
    
    print(icons, icons_CDs, icons_covenant)
    
    hotkeys = np.array(hotkeys)
    hotkeys_CDs = np.array(hotkeys_CDs)
    hotkeys_covenant = np.array(hotkeys_covenant)
    hotkeys_party = np.array(hotkeys_party)
    
    print(hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_party)
    print(type(hotkeys))
    
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
        
        if(GetWindowText(GetForegroundWindow()) != "World of Warcraft"):
            print("WoW is not the Focus Window!!")
            time.sleep(0.5)
            continue


        #-----Read Screen and Compare to Icons-----
        
        #-----Check if Character is in Combat? -> Red (<100) = Combat, Green  (>100) = Not in Combat----
        # printscreen = screen_record(1493, 798, 5, 5)
        printscreen = screen_record(WA_Position_Combat[0], WA_Position_Combat[1], 5, 5)
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        
        if(printscreen.sum()/100 < 35 or printscreen.sum()/100 > 45):
            print("Not in Combat! (Score = ", printscreen.sum()/100, ")")
            time.sleep(random.uniform(0,0.2))
            continue

        print("(Score = ", printscreen.sum()/100, ")")



        #-----Resize Images to icon_dim-----
        # printscreen = screen_record(1480, 580, 28, 28)
        printscreen = screen_record(WA_Position_Spells[0], WA_Position_Spells[1], WA_Position_Spells[2], WA_Position_Spells[3])
        # printscreen = cv2.resize(printscreen, icon_dim, interpolation = cv2.INTER_LINEAR)
        # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
        # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('image',printscreen)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        printscreen_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
        # printscreen_CDs = cv2.cvtColor(printscreen_CDs, cv2.COLOR_BGR2RGB)

        printscreen_np = np.asarray(printscreen)
        printscreen_np = printscreen_np / 255.0
        
        printscreen_CDs_np = np.asarray(printscreen_CDs)
        printscreen_CDs_np = printscreen_CDs_np / 255.0

        printscreen_array = np.array([printscreen_np, printscreen_CDs_np])

        printscreen_kick = screen_record(WA_Position_Kick[0], WA_Position_Kick[1], 5, 5)
        printscreen_kick = cv2.cvtColor(printscreen_kick, cv2.COLOR_BGR2GRAY)
        # print("Shapes: ", printscreen.shape, augmented_icons_np.shape)
        # # Convert into Numpy array and Predict some Samples
        # samples_to_predict = np.array(samples_to_predict)
        # print(samples_to_predict.shape)
        predictions = model.predict(printscreen_array)

        classes = np.argmax(predictions, axis = 1)
        score = tf.nn.softmax(predictions)

        for i in range(len(classes)):
            print(icons_filenames[classes[i]], np.max(score[i])*100)
            

        print(spells)
        print(cooldowns) 
        keys2press, keysCD2press = None, None

        for i in range(len(spells)):
            if icons_filenames[classes[0]].split('.')[0] in spells[i]:
                keys2press = hotkeys[i]
                break
        
        for i in range(len(cooldowns)):
            if icons_filenames[classes[1]].split('.')[0] in cooldowns[i]:
                keysCD2press = hotkeys_CDs[i]
                break

        print(keys2press, keysCD2press)

        #-----Select Direct Input Key to press-----
        #-----Kick First if Casting-----
        if(printscreen_kick.sum()/100 == 226):
            print("KICK ACTIVATED!!!")
            for key_kick in hotkeys_kick[0]:
                PressKey(dict_hkeys["_" + key_kick])
                time.sleep(random.uniform(0,0.1))
            for key_kick in hotkeys_kick[0]:
                ReleaseKey(dict_hkeys["_" + key_kick]) 
                time.sleep(random.uniform(0,0.1))
        
        #-----Cooldowns First-----
        if(CDs_True.get()):
            if keysCD2press is not None:
                # print(sh_arr_CDs[0,0])
                for key_CDs in keysCD2press:
                    PressKey(dict_hkeys["_" + key_CDs])
                    time.sleep(random.uniform(0,0.5))
                    
                for key_CDs in keysCD2press:
                    ReleaseKey(dict_hkeys["_" + key_CDs]) 
                    time.sleep(random.uniform(0,0.5))
        
        # #-----Spells Third-----
        if(Spells_True.get()):
            if keys2press is not None:
                # print(sh_arr[0,1])
                key = dict_hkeys["_" + keys2press]
                time.sleep(random.uniform(0,0.5)) 
                PressKey(key)
                ReleaseKey(key)
        
        time.sleep(random.uniform(0,0.4))


def start_RotBot():
    # Assign global variable and initialize value
    global stop
    stop = 0
    
    global config_filepath
    # config_filepath = lib.config.config_filepath
    # global lib.config.config_filepath
    global WA_Position_Spells
    global WA_Position_CDs
    global WA_Position_Covenant
    # print(config_filepath, lib.config.config_filepath)
    # Create and launch a thread 
    t = Thread(target = RotBot_main)
    # t = Thread(target = lambda:RotBot_main(filepath=config_filepath))
    # t = Thread(target = lambda:RotBot_main(filepath=lib.config.config_filepath))
    t.start()

# #-----Show the Weak-Aura Image in the App-----
# #-----Find WA Position on Screen (click on anchor in the middle)-----
# from pynput import mouse    

# def on_move(x, y):
#     Label_WAPosition["text"] = 'Pointer moved to {0}'.format((x, y))
#     print('Pointer moved to {0}'.format((x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))




WA_Position = WA_Position_Covenant
WA_img = screen_record(WA_Position[0], WA_Position[1], WA_Position[2], WA_Position[3])
WA_img = cv2.cvtColor(WA_img, cv2.COLOR_BGR2GRAY)

WA_img = PIL.Image.fromarray(WA_img)
WA_img = ImageTk.PhotoImage(image=WA_img) 

def Get_SSIM_values():
    #-----Main Rotation-Bot Routine-----
    global config_filepath
    global WA_Position_Spells
    global WA_Position_CDs
    
    icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs = get_config(config_filepath)
    print(icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs)

    icons = []
    for spell in spells:
        icons.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    icons_CDs = []
    for spell in cooldowns:
        icons_CDs.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    hotkeys = np.array(hotkeys)
    hotkeys_CDs = np.array(hotkeys_CDs)
    
    #-----Set IconSize-----
    icon_dim = (56,56)
        
    while True:
        if stop == 1:
            break
        
        #-----Read Screen and Compare to Icons-----
        
        #-----Resize Images to icon_dim-----
        printscreen = screen_record(WA_Position_Spells[0], WA_Position_Spells[1], WA_Position_Spells[2], WA_Position_Spells[3])
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        
        printscreen_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
        printscreen_CDs = cv2.cvtColor(printscreen_CDs, cv2.COLOR_BGR2GRAY)
            
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
        
        print(sh_arr)
        print(sh_arr_CDs)
        time.sleep(0.5)
        

# def start_Get_SSIM_values():
#     # Assign global variable and initialize value
#     global stop
#     stop = 0
    
#     global config_filepath
#     global WA_Position_Spells
#     WA_Position_Spells = WA_Position
    
#     global WA_Position_CDs
#     WA_Position_CDs = WA_Position
    
#     # Create and launch a thread 
#     t = Thread(target = Get_SSIM_values)
#     t.start()
# from tkinter import font as tkFont
# helv36 = tkFont.Font(family='Helvetica', size=20, weight='bold')
# 
# Button_GetSSIM = Button(app,
#                       width=10,
#                       height=5,
#                       bg="#00FF00",
#                       fg="Black", 
#                       text="Start",
#                       font = helv36,
#                       command=start_Get_SSIM_values)
# Button_GetSSIM.grid(row=11, column=0)

# root = tk.Tk()

# def change_pic(labelname):
#  photo1 = ImageTk.PhotoImage(Image.open("demo.jpg"))
#  labelname.configure(image=photo1)
#  print "updated"

# vlabel=tk.Label(root)
# photo = ImageTk.PhotoImage(Image.open('cardframe.jpg'))
# vlabel.configure(image=photo)
# vlabel.pack()
# b2=tk.Button(root,text="Capture",command=lambda:change_pic(vlabel))
# b2.pack()
# root.mainloop()

from tkinter import font as tkFont
helv36 = tkFont.Font(family='Helvetica', size=20, weight='bold')

def var_states():
   print("%d %d %d" % (Spells_True.get(), CDs_True.get(), Covenant_True.get()))


from tkinter import ttk

# Button(app, text='Get What to use', command=var_states).grid(row=6, column=1, columnspan = 2)

# Button_WAPosition = Button(master=app, text="Get WA Position", command=thread_findmouse)
# Button_WAPosition.grid(row=1, column=0, sticky="nsew")

# Button_move_WASpellsleft = Button(master=app, text="left", command=move_WAleft)
# Button_move_WASpellsleft.grid(row=4, column=1, sticky="nsew")
# Button_move_WASpellsright = Button(master=app, text="right", command=move_WAright)
# Button_move_WASpellsright.grid(row=5, column=1, sticky="nsew")
# Button_move_WASpellsup = Button(master=app, text="up", command=move_WAup)
# Button_move_WASpellsup.grid(row=4, column=2, sticky="nsew")
# Button_move_WASpellsdown = Button(master=app, text="down", command=move_WAdown)
# Button_move_WASpellsdown.grid(row=5, column=2, sticky="nsew")


#-----Labels-----
# Label_Utilities = ttk.Label(master=app, text="  Utilities  ", bg = "White", font = 'Cambria 16 underline')
Label_Utilities = ttk.Label(master=app, text="  Utilities  ", style = "L2.TLabel")
Label_Utilities. grid(row=2, column=0, sticky="n")
Label_WAPosition = ttk.Label(master=app, text="WeakAura Position on Screen", style = "L3.TLabel")
Label_WAPosition.grid(row=10, column=0, sticky="n")

Label_Filepath_Config = ttk.Label(master=app, text="Config File Path", style = "L3.TLabel", wraplength=200)
Label_Filepath_Config.grid(row=3, column=1, sticky="n", rowspan = 2)

showWA = lambda:showWA_Pic(label_showWA_Spells, label_showWA_CDs, label_showWA_Covenant, WA_Position_Spells, WA_Position_CDs, WA_Position_Covenant)
variables = Spells_True, CDs_True, Kick_True, Covenant_True, Healer_True
setup_buttons(app, start_RotBot, stop, [open_configfile, config_filepath, Label_Filepath_Config], variables, showWA, thread_findmouse)


# Label_WAPosition = Label(master=app, text="WeakAura Position on Screen")
# Label_WAPosition.grid(row=1, column=1)
# Label_WA_curPosition = Label(master=app)
# Label_WA_curPosition["text"] = 'Position: {0}'.format(WA_Position)
# Label_WA_curPosition.grid(row=10, column=1)

frame_WAs = Frame(app)
frame_WAs.configure(bg='White')
frame_WAs.grid(row=5, column=1, rowspan = 6)

Label_Spells = ttk.Label(master=frame_WAs, text="Spells:      ", style = "L4.TLabel")
Label_Spells.grid(row=0, column=0, sticky="w", rowspan = 2)

Label_CDs = ttk.Label(master=frame_WAs, text="Cooldowns:      ", style = "L4.TLabel")
Label_CDs.grid(row=2, column=0, sticky="w", rowspan = 2)

Label_Covenant = ttk.Label(master=frame_WAs, text="Covenant:      ", style = "L4.TLabel")
Label_Covenant.grid(row=4, column=0, sticky="w", rowspan = 2)

label_showWA_Spells = Label(frame_WAs, image = WA_img, bg = "White")
label_showWA_Spells.image = WA_img
label_showWA_Spells.grid(row=0, column=1, rowspan = 2, sticky="e") 

label_showWA_CDs = Label(frame_WAs, image = WA_img, bg = "White")
label_showWA_CDs.image = WA_img
label_showWA_CDs.grid(row=2, column=1, rowspan = 2, sticky="nsew") 

label_showWA_Covenant = Label(frame_WAs, image = WA_img, bg = "White")
label_showWA_Covenant.image = WA_img
label_showWA_Covenant.grid(row=4, column=1, rowspan = 2, sticky="nsew") 



# Label_Spells = ttk.Label(master=app, text="Spells -> ", style = "L3.TLabel")
# Label_Spells.grid(row=5, column=1, sticky="n", rowspan = 2)

# label_showWA_Spells = Label(app, image = WA_img, bg = "White")
# label_showWA_Spells.image = WA_img
# label_showWA_Spells.grid(row=5, column=2, rowspan = 2, sticky="nsew") 

# label_showWA_CDs = Label(app, image = WA_img, bg = "White")
# label_showWA_CDs.image = WA_img
# label_showWA_CDs.grid(row=7, column=1, rowspan = 2, sticky="nsew") 

# label_showWA_Covenant = Label(app, image = WA_img, bg = "White")
# label_showWA_Covenant.image = WA_img
# label_showWA_Covenant.grid(row=9, column=1, rowspan = 2, sticky="nsew") 
    
#-----Entries-----

#-----Style-----
set_app_style(root)
app.mainloop() 





# filenames = ['Abominationlimb.jpg', 'Antimagicshell.jpg', 'Bloodboil.jpg', 'Bloodboil_color.jpg', 'Blooddrinker.jpg', 'Bloodtap.jpg', 'Bonestorm.jpg', 'Consumption.jpg', 'Dancingruneweapon.jpg', 'Deathanddecay.jpg', 'Deathscaress.jpg', 'Deathsdue.jpg', 'Deathstrike.jpg', 'Empowerruneweapon.jpg', 'Hearthstrike.jpg', 'Iceboundfortitude.jpg', 'Lichborn.jpg', 'Markoofblood.jpg', 'Marrowend.jpg', 'peacebloom.jpg', 'Raisedead.jpg', 'Runetap.jpg', 'Shackletheunworthy.jpg', 'Swarmingmist.jpg', 'Tombstone.jpg', 'Vampiricblood.jpg']
# files = []
# # Load the Pictures

# i = 0
# for f in filesnames:
#     fp = open(mypath + f,"rb")
#     image = PIL.Image.open(fp)
#     files.append(np.asarray(image))








