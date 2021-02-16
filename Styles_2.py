from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedStyle


#--------root style
root = tk.Tk()
#--------root backgroud
root.configure(bg="white")
#--------root title
root.title("Reminder")
#--------root size
root.geometry("225x300")

# white theme
style = ThemedStyle(root)
style.theme_use('arc')  # white style

#--------create empty list
tasks = []


#--------function
def darkmd():
    style.theme_use("equilux")  # only changes the theme of the ttk widgets
    # change style of tk widgets manually:
    bg = style.lookup('TLabel', 'background')
    fg = style.lookup('TLabel', 'foreground')
    root.configure(bg=style.lookup('TLabel', 'background'))
    lb_tasks.configure(bg=bg, fg=fg)


#--------command
lbl_title = ttk.Label(root, text="ToDoList")
lbl_title.grid(row=0, column=0)

lbl_display = ttk.Label(root, text="")
lbl_display.grid(row=0, column=1)

txt_input = ttk.Entry(root, width=20)
txt_input.grid(row=1, column=1)

bt_add_task = ttk.Button(root, text="Add Task")
bt_add_task.grid(row=1, column=0)

bt_del_all = ttk.Button(root, text="Del all")
bt_del_all.grid(row=2, column=0)

bt_del_one = ttk.Button(root, text="Del")
bt_del_one.grid(row=3, column=0)

bt_sort_asc = ttk.Button(root, text="Sort (ASC)")
bt_sort_asc.grid(row=4, column=0)

bt_sort_desc = ttk.Button(root, text="Sort (DESC)")
bt_sort_desc.grid(row=5, column=0)

bt_total_task = ttk.Button(root, text="Num Of Task")
bt_total_task.grid(row=6, column=0)

bt_darkmd = ttk.Button(root, text="Darkmode", command=darkmd)
bt_darkmd.grid(row=7, column=0)

lb_tasks = tk.Listbox(root, fg="black")
lb_tasks.grid(row=2, column=1, rowspan=9)

#--------main
root.mainloop()