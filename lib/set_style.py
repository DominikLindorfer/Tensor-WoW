from ttkthemes import ThemedStyle
from tkinter.ttk import Style

# -----Style-----
def set_app_style(root):

    # style = ThemedStyle(root)
    # sv_ttk.use_dark_theme()
    # sv_ttk.set_theme("dark")

    root.tk.call("source", "./themes/azure.tcl")
    root.tk.call("set_theme", "dark")

    style = Style(root)
    style.configure("L.TButton", font="Serif 16")
    style.configure("TButton", font="Serif 12")
    style.configure("s.TButton", font="Serif 12")
    style.configure("Red.TCheckbutton", font="Serif 11")
    style.configure("L.TLabel", font="Serif 16")
    style.configure("L2.TLabel", font="Serif 16")
    style.configure("L3.TLabel", font="Serif 12")
    style.configure("L4.TLabel", font="Serif 12")
    style.configure("L5.TLabel", font="Serif 12")

    # root.tk.call('source', './themes/sprites_dark.tcl')  # Put here the path of your theme file
    # print(style.theme_names())
    # style.theme_use('sprites_dark')  # white style
    # style.theme_use('equilux')
    # style.theme_use('black')
    # style.theme_use('arc')  # white style
    # style.configure('L.TButton', background='White', foreground='Black', font = 'Cambria 20')
    # style.configure('TButton', background='White', foreground='Black', font = 'Cambria 14')
    # style.configure('s.TButton', background='White', foreground='Black', font = 'Cambria 12')
    # style.configure('Red.TCheckbutton', background='White', foreground='Black', font = 'Cambria 12')
    # style.configure('L.TLabel', background='White', foreground='Black', font = 'Cambria 12')
    # style.configure('L2.TLabel', background='White', foreground='Black', font = 'Cambria 18 underline')
    # style.configure('L3.TLabel', background='White', foreground='Black', font = 'Cambria 12')
    # style.configure('L4.TLabel', background='White', foreground='Black', font = 'Cambria 16')
    # style.configure('L5.TLabel', background='White', foreground='Black', font = 'Cambria 14')
