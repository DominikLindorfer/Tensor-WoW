# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Jan 10 11:56:29 2021

# @author: lindorfer
# """

#-----This does also what I want but is slower somehow-----
# from tkinter import *

# running = True  # Global flag
# idx = 0

# def scanning():
#     if running:  # Only do this if the Stop button has not been clicked
#         global idx
#         idx = idx +1
#         print(idx)

#     # After 1 second, call scanning again (create a recursive loop)
#     root.after(1, scanning)

# def start():
#     """Enable scanning by setting the global flag to True."""
#     global running
#     running = True

# def stop():
#     """Stop scanning by setting the global flag to False."""
#     global running
#     running = False

# root = Tk()
# root.title("Title")
# root.geometry("500x500")

# app = Frame(root)
# app.grid()

# start = Button(app, text="Start Scan", command=start)
# stop = Button(app, text="Stop", command=stop)

# start.grid()
# stop.grid()

# root.after(1, scanning)  # After 1 second, call scanning
# root.mainloop()



#-----This does what I want-----
from tkinter import *
from threading import Thread

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

def stop():
    # Assign global variable and set value to stop
    global stop
    stop = 1

root = Tk()
root.title("Title")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan",command=start_thread)
stop = Button(app, text="Stop",command=stop)

start.grid()
stop.grid()
app.mainloop() 
#-----Until here-----



# import tkinter as tk
# from concurrent import futures
# import time
 
# thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
# class MainFrame(tk.Frame):
 
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.label = tk.Label(self, text='not running')
#         self.label.pack()
#         self.listbox = tk.Listbox(self)
#         self.listbox.pack()
#         self.button = tk.Button(
#             self, text='blocking task', command=self.on_button)
#         self.button.pack(pady=15)
#         self.pack()
 
#     def on_button(self):
#         print('Button clicked')
#         thread_pool_executor.submit(self.blocking_code)
 
 
#     def set_label_text(self, text=''):
#         self.label['text'] = text
 
#     def listbox_insert(self, item):
#         self.listbox.insert(tk.END, item)
 
#     def blocking_code(self):
#         self.after(0, self.set_label_text, 'running')
 
#         for number in range(5):
#             self.after(0, self.listbox_insert, number)
#             print(number)
#             time.sleep(1)
 
#         self.after(0, self.set_label_text, ' not running')
 
 
# if __name__ == '__main__':
#     app = tk.Tk()
#     main_frame = MainFrame()
#     app.mainloop()