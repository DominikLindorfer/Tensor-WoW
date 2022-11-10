import numpy as np
from PIL import ImageGrab, Image, ImageTk
import cv2
import time

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
        
        printscreen =  np.array(ImageGrab.grab(bbox=(xoff - wx, yoff - wy, xoff + wx, yoff + wy)))
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

def screen_record_all(xoff = 260, yoff = 984, wxl = 50, wyt = 50, wxr = 50, wyb = 50): 
    last_time = time.time()
    printscreen =  np.array(ImageGrab.grab(bbox=(xoff - wxl, yoff - wyt, xoff + wxr, yoff + wyb)))
    return printscreen

def convert_rbg_to_int(rgb_tuple):
    return rgb_tuple[0] * 256*256 + rgb_tuple[1]*256 + rgb_tuple[0]

def showWA_Pic(labelname_Spells, labelname_CDs, labelname_Covenants, WA_Position_Spells, WA_Position_CDs, WA_Position_Covenant):
    WA_img_Spells = screen_record(WA_Position_Spells[0], WA_Position_Spells[1], WA_Position_Spells[2], WA_Position_Spells[3])
    WA_img_Spells = cv2.cvtColor(WA_img_Spells, cv2.COLOR_BGR2GRAY)
    WA_img_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
    WA_img_CDs = cv2.cvtColor(WA_img_CDs, cv2.COLOR_BGR2GRAY)
    WA_img_Covenant = screen_record(WA_Position_Covenant[0], WA_Position_Covenant[1], WA_Position_Covenant[2], WA_Position_Covenant[3])
    WA_img_Covenant = cv2.cvtColor(WA_img_Covenant, cv2.COLOR_BGR2GRAY)
    
    
    WA_img_Spells = Image.fromarray(WA_img_Spells)
    WA_img_Spells = ImageTk.PhotoImage(image=WA_img_Spells) 
    WA_img_CDs = Image.fromarray(WA_img_CDs)
    WA_img_CDs = ImageTk.PhotoImage(image=WA_img_CDs)
    WA_img_Covenant = Image.fromarray(WA_img_Covenant)
    WA_img_Covenant = ImageTk.PhotoImage(image=WA_img_Covenant) 
    
    labelname_Spells.configure(image=WA_img_Spells)
    labelname_Spells.image = WA_img_Spells
    labelname_CDs.configure(image=WA_img_CDs)
    labelname_CDs.image = WA_img_CDs
    labelname_Covenants.configure(image=WA_img_Covenant)
    labelname_Covenants.image = WA_img_Covenant

# def move_WAleft():
#     WA_Position[0] = WA_Position[0] + 1
#     Button_showWA_Pic.invoke()
#     Label_WA_curPosition["text"] = 'Position: {0}'.format(WA_Position)

# def move_WAright():
#     WA_Position[0] = WA_Position[0] - 1
#     Button_showWA_Pic.invoke()
#     Label_WA_curPosition["text"] = 'Position: {0}'.format(WA_Position)
    
# def move_WAup():
#     WA_Position[1] = WA_Position[1] + 1
#     Button_showWA_Pic.invoke()
#     Label_WA_curPosition["text"] = 'Position: {0}'.format(WA_Position)
    
# def move_WAdown():
#     WA_Position[1] = WA_Position[1] - 1
#     Button_showWA_Pic.invoke()
#     Label_WA_curPosition["text"] = 'Position: {0}'.format(WA_Position)
    