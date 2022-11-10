import ast
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

def get_Settings(settings_path = "Settings.dat"):
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
    print(config_filepath)
        
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

