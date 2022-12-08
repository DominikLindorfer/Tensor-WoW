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
import PIL.ImageGrab as ImageGrab

from os import walk, environ

import tensorflow.lite as tflite
import tensorflow.python.ops.nn_ops as tfnn
environ['CUDA_VISIBLE_DEVICES'] = '-1'

import numpy as np
import cv2
import time
import random

# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
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

# WA_Position_Spells = [1480, 584, 28, 28]
# WA_Position_CDs = [1480, 682, 28, 28]
# WA_Position_Covenant = [1480, 782, 28, 28]
# WA_Position_Combat = [1480, 832, 5, 5]
# WA_Position_Kick = [1517, 832, 5, 5]
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

    # Setup TF-Lite Interpreter 
    interpreter = tflite.Interpreter(filepath + "model.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details() 

    # model = load_model(filepath, compile = True)

    print("RotBot Main Function, Filepath: ", config_filepath)

    icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party = get_config(config_filepath)
    print(icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party)
    
    icons_filenames = []
    for (dirpath, dirnames, filenames) in walk(icon_dir):
        icons_filenames.extend(filenames)
        break 
    
    hotkeys = np.array(hotkeys)
    hotkeys_CDs = np.array(hotkeys_CDs)
    hotkeys_covenant = np.array(hotkeys_covenant)
    hotkeys_party = np.array(hotkeys_party)
    
    print(hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_party)
    
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
        printscreen = screen_record(WA_Position_Combat[0], WA_Position_Combat[1], 5, 5)
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        
        if(printscreen.sum()/100 < 35 or printscreen.sum()/100 > 45):
            print("Not in Combat! (Score = ", printscreen.sum()/100, ")")
            time.sleep(random.uniform(0,0.2))
            continue

        #-----Record Icons using Printscreen-----
        printscreen = screen_record(WA_Position_Spells[0], WA_Position_Spells[1], WA_Position_Spells[2], WA_Position_Spells[3])
        printscreen_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
        # cv2.imshow('image',printscreen)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        printscreen_np = np.asarray(printscreen)
        printscreen_np = printscreen_np / 255.0
        
        printscreen_CDs_np = np.asarray(printscreen_CDs)
        printscreen_CDs_np = printscreen_CDs_np / 255.0

        printscreen_kick = screen_record(WA_Position_Kick[0], WA_Position_Kick[1], 5, 5)
        printscreen_kick = cv2.cvtColor(printscreen_kick, cv2.COLOR_BGR2GRAY)

        # TF Model PredictionsInterpreter 
        pred_classes = []
        for sample in [printscreen_np.astype(np.float32), printscreen_CDs_np.astype(np.float32)]:
            interpreter.set_tensor(input_details[0]["index"], [sample])
            interpreter.invoke()
            predictions = interpreter.get_tensor(output_details[0]["index"])

            pred_class = np.argmax(predictions, axis = 1)
            pred_classes.append(pred_class[0])
            # score = tf.nn.softmax(predictions)
            score = tfnn.softmax(predictions)
            print(filenames[pred_class[0]], np.max(score[0])*100)

        # predictions = model.predict(printscreen_array)
        # classes = np.argmax(predictions, axis = 1)
        # score = tf.nn.softmax(predictions)
        # for i in range(len(classes)):
        #     print(icons_filenames[classes[i]], np.max(score[i])*100)

        print(spells)
        print(cooldowns) 
        keys2press, keysCD2press = None, None

        for i in range(len(spells)):
            if icons_filenames[pred_classes[0]].split('.')[0] in spells[i]:
                keys2press = hotkeys[i]
                break
        
        for i in range(len(cooldowns)):
            if icons_filenames[pred_classes[1]].split('.')[0] in cooldowns[i]:
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

WA_Position = WA_Position_Covenant
WA_img = screen_record(WA_Position[0], WA_Position[1], WA_Position[2], WA_Position[3])
WA_img = cv2.cvtColor(WA_img, cv2.COLOR_BGR2GRAY)

WA_img = PIL.Image.fromarray(WA_img)
WA_img = ImageTk.PhotoImage(image=WA_img) 


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













