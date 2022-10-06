# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:08:03 2021

@author: dl
"""

from win32gui import GetWindowText, GetForegroundWindow
import time
while True:
    print(GetWindowText(GetForegroundWindow()))
