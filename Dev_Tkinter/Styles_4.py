# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:05:31 2021

@author: dl
"""

import tkinter as tk
from tkinter import ttk
root=tk.Tk();
s = ttk.Style(); 
s.theme_use('default');
s.configure('zc.TButton',borderwidth='20')
s.configure('zc.TButton',highlightthickness='10')
s.configure('zc.TButton',highlightcolor='pink')
s.map('zc.TButton',background=[('active', 'pressed', 'yellow'),('!active','green'), ('active','!pressed', 'cyan')])
s.map('zc.TButton',relief=[('pressed','sunken'),('!pressed','raised')]);
calc_button=ttk.Button(root, text="classic", style='zc.TButton');
calc_button.grid(column=0,row=0,sticky='nsew');
root.mainloop() 