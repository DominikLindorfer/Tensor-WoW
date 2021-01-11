# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:32:22 2020

@author: dl
"""

# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Q = 0x10
F2 = 0x3C

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

dict_hkeys = {
"_1"          :     0x02, 
"_2"          :     0x03,
"_3"          :     0x04,
"_4"          :     0x05,
"_5"          :     0x06,
"_6"          :     0x07,
"_7"          :     0x08,
"_8"          :     0x09,
"_9"          :     0x0A,
"_0"          :     0x0B,
"_Q"          :     0x10,
"_W"          :     0x11,
"_E"          :     0x12,
"_R"          :     0x13,
"_T"          :     0x14,
"_Y"          :     0x15,
"_U"          :     0x16,
"_I"          :     0x17,
"_O"          :     0x18,
"_P"          :     0x19,
"_LCONTROL"   :     0x1D,
"_A"          :     0x1E,
"_S"          :     0x1F,
"_D"          :     0x20,
"_F"          :     0x21,
"_G"          :     0x22,
"_H"          :     0x23,
"_J"          :     0x24,
"_K"          :     0x25,
"_L"          :     0x26,
"_LSHIFT"     :     0x2A,
"_Z"          :     0x2C,
"_X"          :     0x2D,
"_C"          :     0x2E,
"_V"          :     0x2F,
"_B"          :     0x30,
"_N"          :     0x31,
"_M"          :     0x32,
"_F1"         :     0x3B,
"_F2"         :     0x3C,
"_F3"         :     0x3D,
"_F4"         :     0x3E,
"_F5"         :     0x3F,
"_F6"         :     0x40,
"_F7"         :     0x41,
"_F8"         :     0x42,
"_F9"         :     0x43,
"_F1"         :    0x44,
"_LALT"       :    0x38,
}

if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)
