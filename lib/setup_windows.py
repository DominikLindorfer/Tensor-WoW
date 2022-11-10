from PIL.ImageTk import PhotoImage
from tkinter import ttk

def setup_root(root):
    root.title("WoW Rot Bot")
    root.geometry("505x580")
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='LogoV3_icon.png'))

def setup_app(app):
    app.configure(bg='White')
    app.grid()

    col_count = 10
    row_count = 12

    for col in range(col_count):
        app.grid_columnconfigure(col, weight=1, minsize=200)

    for row in range(row_count):
        app.grid_rowconfigure(row, weight=1, minsize=25)


#-----Buttons-----    
def setup_buttons(app, start, stop, config, variables, showWA, thread_findmouse): 
    # Button_Start = Button(app, bg="#00FF00", fg="Black", text="Start", font = helv36, command=start_RotBot)
    # Button_Stop = Button(app, bg="Red", fg="Black", text="Stop", font = helv36, command=stop)

    # open_configfile, config_filepath, Label_Filepath_Config  = config[0], config[1], config[2]
    open_configfile, Label_Filepath_Config  = config[0], config[2]
    global config_filepath
    Spells_True, CDs_True, Kick_True, Covenant_True, Healer_True = variables[0], variables[1], variables[2], variables[3], variables[4]

    Button_Start = ttk.Button(app, text="Start", command=start, style="L.TButton")
    Button_Stop = ttk.Button(app, text="Stop", command=stop, style="L.TButton")
    Button_Start.grid(row=1, column=0,sticky="nsew", padx=2, pady=2)
    Button_Stop.grid(row=1, column=1,sticky="nsew", padx=2, pady=2)

    # Button_OpenConfigFile = ttk.Button(app, text="Open Config File", command=open_configfile, style="L2.TButton")
    Button_OpenConfigFile = ttk.Button(app, text="Open Config File", command=lambda:open_configfile(config_filepath, Label_Filepath_Config), style="L2.TButton")
    Button_OpenConfigFile.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

    cb_row = 3
    ttk.Checkbutton(app, text="Enable Spells", variable=Spells_True,style='Red.TCheckbutton').grid(row=cb_row, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(app, text="Enable CDs", variable=CDs_True, style='Red.TCheckbutton').grid(row=cb_row+1, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(app, text="Enable Covenant", variable=Kick_True, style='Red.TCheckbutton').grid(row=cb_row+2, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(app, text="Enable Kick", variable=Covenant_True, style='Red.TCheckbutton').grid(row=cb_row+3, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(app, text="I'm Healing?", variable=Healer_True, style='Red.TCheckbutton').grid(row=cb_row+4, column=0, sticky="w", padx=(15, 0))

    Button_showWA_Pic = ttk.Button(master=app, text="Get WA Pictures", command=showWA, style = "s.TButton")
    Button_showWA_Pic.grid(row=8, column=0, sticky="nsew", padx=2, pady=2)

    Button_WAPosition = ttk.Button(master=app, text="Get WA Position", command=thread_findmouse, style = "s.TButton")
    Button_WAPosition.grid(row=9, column=0, sticky="nsew", padx=2, pady=2)