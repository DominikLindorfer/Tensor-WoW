from PIL.ImageTk import PhotoImage
import PIL
from PIL import ImageTk
from tkinter import ttk, Frame, Label
# import lib.config
from lib.screen_functions import showWA_Pic


def setup_root(root):
    root.title("WoW Rot Bot")
    root.geometry("505x580")
    root.tk.call(
        "wm", "iconphoto", root._w, PhotoImage(file="./Logo/LogoV4_icon.png", master=root)
    )


def setup_app(app):
    # app.configure(bg='White')
    app.grid()

    col_count = 10
    row_count = 16

    for col in range(col_count):
        app.grid_columnconfigure(col, weight=1, minsize=200)

    for row in range(row_count):
        app.grid_rowconfigure(row, weight=1, minsize=25)


def setup_buttons_labels(
    app,
    start,
    stop,
    config,
    variables,
    thread_findmouse,
    WA_Position_Spells,
    WA_Position_CDs,
    WA_Position_Covenant,
):
    # -----Labels-----
    # Label_Utilities = ttk.Label(master=app, text="  Utilities  ", style = "L2.TLabel")
    # Label_Utilities.grid(row=2, column=0, sticky="n")
    Label_WAPosition = ttk.Label(
        master=app, text="WeakAura Position on Screen", style="L3.TLabel"
    )
    Label_WAPosition.grid(row=10, column=0, sticky="n")

    Label_Filepath_Config = ttk.Label(
        master=app, text="Config File Path", style="L3.TLabel", wraplength=200
    )
    Label_Filepath_Config.grid(row=3, column=1, sticky="n", rowspan=2)

    Label_Output_Header = ttk.Label(master=app, text="  Output  ", style="L2.TLabel")
    Label_Output_Header.grid(row=12, column=0, sticky="n", columnspan=2)

    # -----Buttons-----
    showWA = lambda: showWA_Pic(
        label_showWA_Spells,
        label_showWA_CDs,
        label_showWA_Covenant,
        WA_Position_Spells,
        WA_Position_CDs,
        WA_Position_Covenant,
    )

    open_configfile, config_filepath = config[0], config[1]
    Spells_True, CDs_True, Kick_True, Covenant_True, Healer_True = (
        variables[0],
        variables[1],
        variables[2],
        variables[3],
        variables[4],
    )

    Button_Start = ttk.Button(app, text="Start", command=start, style="L.TButton")
    Button_Stop = ttk.Button(app, text="Stop", command=stop, style="L.TButton")
    Button_Start.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
    Button_Stop.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

    # Button_OpenConfigFile = ttk.Button(app, text="Open Config File", command=open_configfile, style="L2.TButton")
    Button_OpenConfigFile = ttk.Button(
        app,
        text="Open Config File",
        command=lambda: open_configfile(config_filepath, Label_Filepath_Config),
        style="L2.TButton",
    )
    Button_OpenConfigFile.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

    cb_row = 3
    ttk.Checkbutton(
        app, text="Enable Spells", variable=Spells_True, style="Red.TCheckbutton"
    ).grid(row=cb_row, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(
        app, text="Enable CDs", variable=CDs_True, style="Red.TCheckbutton"
    ).grid(row=cb_row + 1, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(
        app, text="Enable Kick", variable=Kick_True, style="Red.TCheckbutton"
    ).grid(row=cb_row + 2, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(
        app, text="Enable Covenant", variable=Covenant_True, style="Red.TCheckbutton"
    ).grid(row=cb_row + 3, column=0, sticky="w", padx=(15, 0))
    ttk.Checkbutton(
        app, text="I'm Healing?", variable=Healer_True, style="Red.TCheckbutton"
    ).grid(row=cb_row + 4, column=0, sticky="w", padx=(15, 0))

    Button_showWA_Pic = ttk.Button(
        master=app, text="Get WA Pictures", command=showWA, style="s.TButton"
    )
    Button_showWA_Pic.grid(row=8, column=0, sticky="nsew", padx=2, pady=2)

    Button_WAPosition = ttk.Button(
        master=app, text="Get WA Position", command=thread_findmouse, style="s.TButton"
    )
    Button_WAPosition.grid(row=9, column=0, sticky="nsew", padx=2, pady=2)

    # -----Frame for WeakAura Pictures-----
    WA_img = None
    WA_img = PIL.Image.new("RGB", (56, 56))
    WA_img = ImageTk.PhotoImage(image=WA_img)

    frame_WAs = Frame(app)
    # frame_WAs.configure(bg='White')
    frame_WAs.grid(row=5, column=1, rowspan=6)

    Label_Spells = ttk.Label(master=frame_WAs, text="Spells:      ", style="L4.TLabel")
    Label_Spells.grid(row=0, column=0, sticky="w", rowspan=2)

    Label_CDs = ttk.Label(master=frame_WAs, text="Cooldowns:      ", style="L4.TLabel")
    Label_CDs.grid(row=2, column=0, sticky="w", rowspan=2)

    Label_Covenant = ttk.Label(
        master=frame_WAs, text="Covenant:      ", style="L4.TLabel"
    )
    Label_Covenant.grid(row=4, column=0, sticky="w", rowspan=2)

    label_showWA_Spells = Label(frame_WAs)
    label_showWA_Spells.grid(row=0, column=1, rowspan=2, sticky="e")
    label_showWA_Spells.configure(image=WA_img)
    label_showWA_Spells.image = WA_img

    label_showWA_CDs = Label(frame_WAs)
    label_showWA_CDs.grid(row=2, column=1, rowspan=2, sticky="nsew")
    label_showWA_CDs.configure(image=WA_img)
    label_showWA_CDs.image = WA_img

    label_showWA_Covenant = Label(frame_WAs)
    label_showWA_Covenant.grid(row=4, column=1, rowspan=2, sticky="nsew")
    label_showWA_Covenant.configure(image=WA_img)
    label_showWA_Covenant.image = WA_img

    # label_showWA_Spells = Label(frame_WAs, image = WA_img, bg = "White")
    # label_showWA_Spells.grid(row=0, column=1, rowspan = 2, sticky="e")

    # label_showWA_CDs = Label(frame_WAs, image = WA_img, bg = "White")
    # label_showWA_CDs.grid(row=2, column=1, rowspan = 2, sticky="nsew")

    # label_showWA_Covenant = Label(frame_WAs, image = WA_img, bg = "White")
    # label_showWA_Covenant.grid(row=4, column=1, rowspan = 2, sticky="nsew")

    # labelname_Spells.configure(image=WA_img_Spells)
    # labelname_Spells.image = WA_img_Spells
    # labelname_CDs.configure(image=WA_img_CDs)
    # labelname_CDs.image = WA_img_CDs
    # labelname_Covenants.configure(image=WA_img_Covenant)
    # labelname_Covenants.image = WA_img_Covenant


def update_output_label(output_label, text):
    output_label["text"] = text


# Button(app, text='Get What to use', command=var_states).grid(row=6, column=1, columnspan = 2)
# Button_WAPosition = Button(master=app, text="Get WA Position", command=thread_findmouse)
# Button_WAPosition.grid(row=1, column=0, sticky="nsew")
# Button_move_WASpellsleft = Button(master=app, text="left", command=move_WAleft)
# Button_move_WASpellsleft.grid(row=4, column=1, sticky="nsew")
# Button_move_WASpellsright = Button(master=app, text="right", command=move_WAright)
# Button_move_WASpellsright.grid(row=5, column=1, sticky="nsew")
# Button_move_WASpellsup = Button(master=app, text="up", command=move_WAup)
# Button_move_WASpellsup.grid(row=4, column=2, sticky="nsew")
# Button_move_WASpellsdown = Button(master=app, text="down", command=move_WAdown)
# Button_move_WASpellsdown.grid(row=5, column=2, sticky="nsew")
