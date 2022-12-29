import ast
import json
from tkinter.filedialog import askopenfilename, asksaveasfilename
#-----Find Path of the Config File-----

def get_config(config_filepath):

    print("Getting Config from Path: ", config_filepath)

    f = open(config_filepath, "r")
    f.readline()
    icon_dir = f.readline().rstrip() 
    
    f.readline()
    spells = list(f.readline().rstrip().split(" "))
    f.readline()
    cooldowns = list(f.readline().rstrip().split(" "))
    f.readline()
    covenant = list(f.readline().rstrip().split(" "))
    
    f.readline()
    hotkeys = ast.literal_eval(f.readline().rstrip()) 
    f.readline()
    hotkeys_CDs = ast.literal_eval(f.readline().rstrip()) 
    f.readline()
    hotkeys_covenant = ast.literal_eval(f.readline().rstrip())
    
    f.readline()
    hotkeys_kick = ast.literal_eval(f.readline().rstrip())
   
    if f.readline() == '':
        hotkeys_party = None
    else:
        hotkeys_party = ast.literal_eval(f.readline().rstrip())
   
    return icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party

def get_config_json(config_filepath):
    
    with open(config_filepath) as json_file:
        settings = json.load(json_file)

    class_CNN = settings.get("Class", None)
    icon_dir = settings.get("Icon Directory", None)
    spells = settings.get("Spells", None)
    cooldowns = settings.get("Cooldowns", None)
    hotkeys = settings.get("Hotkeys Spells", None)
    hotkeys_CDs = settings.get("Hotkeys CDs", None)
    hotkeys_kick = settings.get("Hotkeys Kick", None)
    hotkeys_party = settings.get("Hotkeys Party", None)
   
    return icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs, hotkeys_kick, hotkeys_party, class_CNN

def get_settings(settings_path = "Settings.dat"):
   f = open(settings_path, "r")
   f.readline()
   WA_Position_Spells = ast.literal_eval(f.readline().rstrip()) 
   
   f.readline()
   WA_Position_CDs = ast.literal_eval(f.readline().rstrip()) 
   
   f.readline()
   WA_Position_Covenant = ast.literal_eval(f.readline().rstrip()) 
   
   f.readline()
   WA_Position_Combat = ast.literal_eval(f.readline().rstrip()) 
   
   f.readline()
   WA_Position_Kick = ast.literal_eval(f.readline().rstrip()) 
   
   f.readline()
   WA_Position_Casting = ast.literal_eval(f.readline().rstrip()) 
   
   f.readline()
   WA_Position_Party = ast.literal_eval(f.readline().rstrip()) 
   
   return WA_Position_Spells, WA_Position_CDs, WA_Position_Covenant, WA_Position_Combat, WA_Position_Kick, WA_Position_Casting, WA_Position_Party

def get_settings_json(settings_path = "settings.json"):

    with open(settings_path) as json_file:
        settings = json.load(json_file)

    config_filepath = settings["config_filepath"]
    WA_Position_Spells    = settings["WA_Position_Spells"]
    WA_Position_CDs       = settings["WA_Position_CDs"]
    WA_Position_Covenant  = settings["WA_Position_Covenant"]
    WA_Position_Combat    = settings["WA_Position_Combat"]
    WA_Position_Kick      = settings["WA_Position_Kick"]
    WA_Healer_Casting = settings["WA_Healer_Casting"]
    WA_Healer_Party_Positions = settings["WA_Healer_Party_Positions"]
    
    return config_filepath, WA_Position_Spells, WA_Position_CDs, WA_Position_Covenant, WA_Position_Combat, WA_Position_Kick, WA_Healer_Casting, WA_Healer_Party_Positions

def open_configfile(config_filepath, Label_Filepath_Config):

    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )

    if not filepath:
        return
    
    Label_Filepath_Config["text"] = filepath
    # global config_filepath
    config_filepath = filepath
    # print(config_filepath)
    
    with open("settings.json") as json_file:
        settings = json.load(json_file)

    settings["config_filepath"] = config_filepath 

    json_object = json.dumps(settings, indent=4)
    
    with open("settings.json", "w") as outfile:
        outfile.write(json_object)

    return filepath

def save_file():

    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

