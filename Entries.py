# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:26:54 2021

@author: dl
"""

import tkinter as tk

root = tk.Tk()

margin = 0.23
projectedSales = tk.IntVar()
profit = tk.IntVar()

entry = tk.Entry(root, textvariable=projectedSales)

entry.pack()

def profit_calculator():
    profit.set(margin * projectedSales.get())

labelProSales = tk.Label(root, textvariable=projectedSales)
labelProSales.pack()

labelProfit = tk.Label(root, textvariable=profit)
labelProfit.pack()

button_calc = tk.Button(root, text="Calculate", command=profit_calculator)
button_calc.pack()

root.mainloop()