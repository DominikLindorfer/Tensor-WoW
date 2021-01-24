# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 17:44:06 2021

@author: dl
"""

from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="Your sex:").grid(row=0, sticky=W)

var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar(value=1)
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)

mainloop()



# from functools import partial  
# def Update_WAPosition(label_result, n1):  
#     num1 = (n1.get())  
#     result = int(num1)
#     label_result.config(text="Result = %d" % result)  
#     return  


# def Convert(string): 
#     li = list(string.split(" ")) 
#     print(li)
#     return li 

# number = StringVar()
# entry = Entry(app, textvariable=number).grid(row=6, column=3)   

# list_ = []
 
# def calculator(number):
#     list_ = list(number.get().split(" "))
#     print(list_)
    
# label_ = Label(app, textvariable=number).grid(row=6, column=1) 
# conv_list = partial(calculator, number)  
# # buttonCal = Button(app, text="Calculate", command=conv_list).grid(row=6, column=2) 

# def var_states():
#    print("%d %d %d" % (Spells_True.get(), CDs_True.get(), Covenant_True.get()))

# Label(app, text="Your sex:").grid(row=9, column=3)

# Spells_True = IntVar()
# CDs_True = IntVar()
# Covenant_True = IntVar()

# Checkbutton(app, text="Use Spells", variable=Spells_True).grid(row=4, column=3)
# Checkbutton(app, text="Use CDs", variable=CDs_True).grid(row=5, column=3)
# Checkbutton(app, text="Use Covenant", variable=Covenant_True).grid(row=6, column=3)

# Button(app, text='Show', command=var_states).grid(row=9, column=2)

# Button(app, text='Get What to use', command=var_states).grid(row=6, column=1, columnspan = 2)