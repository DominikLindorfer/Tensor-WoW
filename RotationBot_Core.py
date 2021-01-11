# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:21:32 2020

@author: dl

Simplistic Rotation Bot for Worl1d of Warcraft
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import random
from skimage.measure import compare_ssim
from directkeys import PressKey, ReleaseKey, W, A, S, D, dict_hkeys

# #-----Find WA Position on Screen (click on anchor in the middle-----)
# from pynput import mouse    
# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))

# # Collect events until released
# def find_mouseposition():
#     with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#         listener.join()
        
# def print_image_summary(image, labels):
    
#     print('--------------')
#     print('Image Details:')
#     print('--------------')
#     print(f'Image dimensions: {image.shape}')
#     print('Channels:')
    
#     if len(labels) == 1:
#         image = image[..., np.newaxis]
        
#     for i, lab in enumerate(labels):
#         min_val = np.min(image[:,:,i])
#         max_val = np.max(image[:,:,i])
#         print(f'{lab} : min={min_val:.4f}, max={max_val:.4f}')

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


def RotBot_main():
    #-----Main Rotation-Bot Routine-----
    first_run = True
    # find_mouseposition()
    
    #-----Set Directory-----
    icon_dir = "F:/WoWAddonDev/WoWIcons/Paladin/"
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Monk/"
    
    #-----List of Icons-----
    # spells = ["bloodboil", "deathanddecay", "deathcoil", "deathstrike", "heartstrike", "marrowrend"]
    # spells = ["bladeofjustice", "judgement", "templarsverdict", "wakeofashes", "hammerofwrath", "crusaderstrike", "flashheal"]
    spells = ["blessedhammer", "divinetoll", "judgement", "avengersshield", "hammerofwrath", "consecration"]
    # spells = ["Tigerpalm" , "Blackout", "Kegsmash", "Rushingjadewind", "Cranekick", "Breath"]
    icons = []
    for spell in spells:
        icons.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    cooldowns = ["ardentdefender", "avengingwrath", "shieldofvengeance", "acientkings", "wordofglory", "seraphim", "peacebloom"]
    # cooldowns = ["Healingelixir", "Blackox", "Purifying", "Niuzao", "Celestial", "Weaponsoforder", "Fortifyingbrew", "Legkick", "peacebloom", "Touchofdeath"]
    icons_CDs = []
    for spell in cooldowns:
        icons_CDs.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    #-----List of Hotkeys-----
    hotkeys = np.array(["3","F","1","2","G","Q"])
    hotkeys_CDs = np.array([["LSHIFT", "3"], ["LSHIFT", "E"], ["4"], ["LSHIFT", "F"], ["E"],  ["LCONTROL", "3"], []])
    # hotkeys = np.array(["1","2","E","F","4","3"])
    # hotkeys_CDs = np.array([["LCONTROL", "Q"], ["LCONTROL", "E"], ["LALT", "2"], ["LALT", "1"], ["LALT", "3"],  ["LALT", "5"], ["LSHIFT", "4"], ["LSHIFT", "E"], [], ["G"]])
    
    #-----Set IconSize-----
    icon_dim = (56,56)
    
    
    # rec_screen = np.array([[]])
    
    # tv = icons[2]
    # tv[:,:,(0,1)]=0
    # cv2.imshow('image', tv)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    #     printscreen = screen_record(1480, 580, 28, 28)
    # # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
    # printscreen =cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
    # # printscreen = screen_record(1493, 798, 5, 5)gggggggggg
    # # printscreen.sum()/100
    
    # # # printscreen = cv2.resize(printscreen, icon_dim, interpolation = cv2.INTER_LINEAR)
    # # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image', printscreen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    
    # printscreen = screen_record(1480, 682, 28, 28)
    # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
    # # printscreen = screen_record(1493, 798, 5, 5)
    # # printscreen.sum()/100
    
    # # # printscreen = cv2.resize(printscreen, icon_dim, interpolation = cv2.INTER_LINEAR)
    # # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image', printscreen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
        
    # # compare_ssim(printscreen, icons[2], full=False)
    
    # for icon in icons:
    #     print(compare_ssim(printscreen, icon, gaussian_weights=False, multichannel = False, full=False))
    
    # for icon in icons_CDs:
    #     print(compare_ssim(printscreen, icon, gaussian_weights=False, multichannel = False, full=False))
    # # # rec_screen = np.append(rec_screen, cur_screen)
    
    # # #-----Compare Screen to saved Icons using SSIM-----
    # scores = np.array([])
    
    # #-----stack ssim_score and hotkeys and sort descending afterwards-----
    # for icon in icons:
    #     (score, diff) = compare_ssim(printscreen, icon, full=True)
    #     scores = np.append(scores, score)
    #     # scores = np.concatenate((scores, np.array([[score, numb]])))
    #     # print("SSIM: {}".format(score))
    
    while stop != 1:
        
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
        
        # print(scores)
        # print(scores_CDs)
        # time.sleep(2)

# (score, diff) = compare_ssim(res_img1, res_img2, full=True)
# diff = (diff * 255).astype("uint8")
# print("SSIM: {}".format(score))




# img1 = cv2.imread('F:/WoWAddonDev/WoWIcons/bloodboil.jpg', 0)
# img2 = cv2.imread('F:/WoWAddonDev/Screenshots/Bloodboil_Screen.png', 0)
# img3 = cv2.imread('F:/WoWAddonDev/WoWIcons/deathstrike.jpg', 0)

# img1.shape
# img2.shape

# dim = (56,56)
# res_img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_LINEAR)
# res_img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_LINEAR)

# cv2.imshow('window',cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

# # cv2.imshow('window',img1)
# # cv2.waitKey(0) # waits until a key is pressed
# # cv2.destroyAllWindows() # destroys the window showing image

# # cv2.imshow('window',img2)
# # cv2.waitKey(0) # waits until a key is pressed
# # cv2.destroyAllWindows() # destroys the window showing image

# (score, diff) = compare_ssim(res_img1, res_img2, full=True)
# diff = (diff * 255).astype("uint8")
# print("SSIM: {}".format(score))

# (score1, diff1) = compare_ssim(res_img2, img3, full=True)
# diff1 = (diff1 * 255).astype("uint8")
# print("SSIM: {}".format(score1))


# image_rgb = cv2.imread('F:/WoWAddonDev/Screenshots/pencils.jpeg')
# image_rgb = cv2.imread('F:/WoWAddonDev/Screenshots/Bloodboil_Screen.png')
# print_image_summary(image_rgb, ['R', 'G', 'B'])

# # cv2.imshow('window',image_rgb)
# # cv2.waitKey(0) # waits until a key is pressed
# # cv2.destroyAllWindows() # destroys the window showing image


# import matplotlib.pyplot as plt
# import numpy as np

# fig, ax = plt.subplots(1, 4, figsize = (18, 30))
# ax[0].imshow(image_rgb/255.0) 
# ax[0].axis('off')
# ax[0].set_title('original RGB')
# for i, lab in enumerate(['R','G','B'], 1):
#     # temp = image_rgb
#     temp = np.zeros(image_rgb.shape)
#     temp[:,:,i - 1] = image_rgb[:,:,i - 1]
#     ax[i].imshow(temp/255.0) 
#     ax[i].axis("off")
#     ax[i].set_title(lab)
    
# plt.show()

