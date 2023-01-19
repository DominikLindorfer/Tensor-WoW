
from ttkthemes import ThemedStyle

#-----Style-----
def set_app_style(root):

    style = ThemedStyle(root)
    # print(style.theme_names())
    style.theme_use('arc')  # white style
    # style.theme_use('equilux')  # white style
    # style.theme_use('black')  # white style
    style.configure('L.TButton', background='White', foreground='Black', font = 'Cambria 20')
    style.configure('TButton', background='White', foreground='Black', font = 'Cambria 14')
    style.configure('s.TButton', background='White', foreground='Black', font = 'Cambria 12')
    style.configure('Red.TCheckbutton', background='White', foreground='Black', font = 'Cambria 12')
    style.configure('L.TLabel', background='White', foreground='Black', font = 'Cambria 12')
    style.configure('L2.TLabel', background='White', foreground='Black', font = 'Cambria 18 underline')
    style.configure('L3.TLabel', background='White', foreground='Black', font = 'Cambria 12')
    style.configure('L4.TLabel', background='White', foreground='Black', font = 'Cambria 16')