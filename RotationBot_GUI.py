# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:42:05 2021

@author: dl
GUI for WoW Rotation Bot
"""

# -----Library Imports-----
from tkinter import *
from tkinter import ttk
from threading import Thread
from win32gui import GetWindowText, GetForegroundWindow

import PIL.Image as Image
import PIL.ImageTk as ImageTk

from os import walk, environ

import tensorflow.lite as tflite
# from tensorflow.lite.python.interpreter import Interpreter
import tensorflow.python.ops.nn_ops as tfnn

environ["CUDA_VISIBLE_DEVICES"] = "-1"

import numpy as np
import cv2
import time
import random

# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim

# -----Style-----
from lib.set_style import set_app_style

# -----Get Mouse Position------
from lib.get_mouse_position import thread_findmouse

# -----Get Settings & Configs -----
from lib.settings import (
    get_settings,
    get_config,
    open_configfile,
    save_file,
    get_settings_json,
    get_config_json,
)

# -----Get Screen Functions-----
from lib.screen_functions import showWA_Pic, screen_record, convert_rbg_to_int

# -----Direckeys-----
from lib.directkeys import PressKey, ReleaseKey, W, A, S, D, dict_hkeys

# -----Setup TKInter Root and App-----
from lib.setup_windows import (
    setup_app,
    setup_root,
    setup_buttons_labels,
    update_output_label,
)

# -----Setup Global Config -> Simplistic use for updateable system variables // not working atm-----
# import lib.config

# -----Main Window-----
root = Tk()
# root = Toplevel()
setup_root(root)

app = Frame(root)
setup_app(app)

# -----Set Logo on Top-----
# fp = open("LogoV3.png", "rb")
# image = PIL.Image.open(fp)
image = Image.open("./logo/LogoV4.png")
image = image.resize((500,170))
photo = ImageTk.PhotoImage(image, master=root)

label = Label(app, image=photo)
label.image = photo
label.grid(row=0, column=0, columnspan=2)

# -----Get Settings for Labels-----
(
    config_filepath,
    WA_Position_Spells,
    WA_Position_CDs,
    WA_Position_Covenant,
    WA_Position_Combat,
    WA_Position_Kick,
    WA_Position_Casting,
    WA_Position_Party,
) = get_settings_json()

Spells_True = IntVar(value=1)
CDs_True = IntVar(value=1)
Covenant_True = IntVar(value=0)
Kick_True = IntVar(value=1)
Healer_True = IntVar(value=0)

# -----Main Rotation-Bot Routine-----
def RotBot_main():
    first_run = True
    global Spells_True
    global CDs_True
    global Covenant_True
    global Kick_True
    global Healer_True
    global Label_Output

    # print(Spells_True.get(), CDs_True.get())

    # -----Get Settings-----
    (
        config_filepath,
        WA_Position_Spells,
        WA_Position_CDs,
        WA_Position_Covenant,
        WA_Position_Combat,
        WA_Position_Kick,
        WA_Position_Casting,
        WA_Position_Party,
    ) = get_settings_json()
    print("RotBot Main Function, Filepath: ", config_filepath)

    (
        icon_dir,
        spells,
        cooldowns,
        hotkeys,
        hotkeys_CDs,
        hotkeys_kick,
        hotkeys_party,
        class_icons,
    ) = get_config_json(config_filepath)

    print(
        icon_dir,
        spells,
        cooldowns,
        hotkeys,
        hotkeys_CDs,
        hotkeys_kick,
        hotkeys_party,
        class_icons,
    )

    # -----Load CNN -----
    filepath = "./saved_models/" + class_icons + "/"

    # Setup TF-Lite Interpreter
    interpreter = tflite.Interpreter(filepath + "model.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    icons_filenames = []
    for (dirpath, dirnames, filenames) in walk(icon_dir):
        icons_filenames.extend(filenames)
        break

    # -----Set IconSize-----
    icon_dim = (56, 56)

    # -----Rotation Loop-----
    while True:

        if stop == 1:
            break

        if GetWindowText(GetForegroundWindow()) != "World of Warcraft":
            print("WoW is not the Focus Window!!")
            update_output_label(Label_Output, "WoW is not the Focus Window!!")
            time.sleep(0.5)
            continue

        # -----Check if Character is in Combat? -> Red (<100) = Combat, Green  (>100) = Not in Combat----
        printscreen = screen_record(WA_Position_Combat[0], WA_Position_Combat[1], 5, 5)
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)

        if printscreen.sum() / 100 < 35 or printscreen.sum() / 100 > 45:
            print("Not in Combat! (Score = ", printscreen.sum() / 100, ")")
            update_output_label(
                Label_Output,
                "Not in Combat! (Score = " + str(printscreen.sum() / 100) + ")",
            )
            time.sleep(random.uniform(0, 0.2))
            continue

        # -----Record Icons using Printscreen-----
        printscreen = screen_record(
            WA_Position_Spells[0],
            WA_Position_Spells[1],
            WA_Position_Spells[2],
            WA_Position_Spells[3],
        )
        printscreen_CDs = screen_record(
            WA_Position_CDs[0],
            WA_Position_CDs[1],
            WA_Position_CDs[2],
            WA_Position_CDs[3],
        )
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
        for sample in [
            printscreen_np.astype(np.float32),
            printscreen_CDs_np.astype(np.float32),
        ]:
            interpreter.set_tensor(input_details[0]["index"], [sample])
            interpreter.invoke()
            predictions = interpreter.get_tensor(output_details[0]["index"])

            pred_class = np.argmax(predictions, axis=1)
            pred_classes.append(pred_class[0])
            # score = tf.nn.softmax(predictions)
            score = tfnn.softmax(predictions)
            print(filenames[pred_class[0]], np.max(score[0]) * 100)

        keys2press, keysCD2press = None, None

        for i in range(len(spells)):
            if icons_filenames[pred_classes[0]].split(".")[0] in spells[i]:
                keys2press = hotkeys[i]
                break

        for i in range(len(cooldowns)):
            if icons_filenames[pred_classes[1]].split(".")[0] in cooldowns[i]:
                keysCD2press = hotkeys_CDs[i]
                break

        update_output_label(
            Label_Output,
            "Hot-Keys pressed: " + str(keys2press) + " " + str(keysCD2press),
        )
        print(keys2press, keysCD2press)

        # -----Select Direct Input Key to press-----
        # -----Kick First if Casting-----
        if printscreen_kick.sum() / 100 > 0:
            print("KICK ACTIVATED!!!")
            update_output_label(Label_Output, "Kick Activated!")
            for key_kick in hotkeys_kick[0]:
                PressKey(dict_hkeys["_" + key_kick])
                time.sleep(random.uniform(0, 0.1))
            for key_kick in hotkeys_kick[0]:
                ReleaseKey(dict_hkeys["_" + key_kick])
                time.sleep(random.uniform(0, 0.05))
            # continue

        # -----Cooldowns First-----
        if CDs_True.get():
            if keysCD2press is not None:
                # print(sh_arr_CDs[0,0])
                for key_CDs in keysCD2press:
                    PressKey(dict_hkeys["_" + key_CDs])
                    time.sleep(random.uniform(0, 0.1))

                for key_CDs in keysCD2press:
                    ReleaseKey(dict_hkeys["_" + key_CDs])
                    time.sleep(random.uniform(0, 0.3))

                continue

        # #-----Spells Third-----
        if Spells_True.get():
            if keys2press is not None:
                # print(sh_arr[0,1])
                key = dict_hkeys["_" + keys2press]
                time.sleep(random.uniform(0, 0.1))
                PressKey(key)
                ReleaseKey(key)
                continue

        time.sleep(random.uniform(0, 0.05))


# -----Actual Bot Main Routine-----
def stop():
    global stop
    stop = 1


def start_RotBot():
    # Assign global variable and initialize value
    global stop
    stop = 0

    # Create and launch a thread
    t = Thread(target=RotBot_main)
    # t = Thread(target = lambda:RotBot_main(filepath=config_filepath))
    t.start()


variables = Spells_True, CDs_True, Kick_True, Covenant_True, Healer_True
setup_buttons_labels(
    app,
    start_RotBot,
    stop,
    [open_configfile, config_filepath],
    variables,
    thread_findmouse,
    WA_Position_Spells,
    WA_Position_CDs,
    WA_Position_Covenant,
)

# -----Setup Output Label; needs to be global so Main-Routine can continously update-----
Label_Output = ttk.Label(master=app, text="  RotBot Output  ", style="L5.TLabel")
Label_Output.grid(row=13, column=0, sticky="n", columnspan=2, rowspan=1)

# -----Style-----
set_app_style(root)
app.mainloop()
