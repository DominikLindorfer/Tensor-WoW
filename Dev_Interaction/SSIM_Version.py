def RotBot_main():
    #-----Main Rotation-Bot Routine-----
    first_run = True
    global config_filepath
    # config_filepath = filepath
    global WA_Position_Spells
    global WA_Position_CDs
    global WA_Position_Covenant
    global Spells_True
    global CDs_True
    global Covenant_True
    global Kick_True
    global Healer_True
    
    #-----Load CNN -----
    class_icons = "Monk/"
    filepath = './saved_model_icons/' + class_icons

    # Setup TF-Lite Interpreter 
    interpreter = tflite.Interpreter(filepath + "model.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details() 

    # model = load_model(filepath, compile = True)

    print("RotBot Main Function, Filepath: ", config_filepath)

    icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party = get_config(config_filepath)
    print(icon_dir, spells, cooldowns, covenant, hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_kick, hotkeys_party)
    
    #-----Set Directory-----
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Paladin/"
    # icon_dir = "F:/WoWAddonDev/WoWIcons/Monk/"
    
    #-----List of Icons-----
    # spells = ["bloodboil", "deathanddecay", "deathcoil", "deathstrike", "heartstrike", "marrowrend"]
    # spells = ["bladeofjustice", "judgement", "templarsverdict", "wakeofashes", "hammerofwrath", "crusaderstrike", "flashheal"]
    # spells = ["blessedhammer", "divinetoll", "judgement", "avengersshield", "hammerofwrath", "consecration"]
    # spells = ["Tigerpalm" , "Blackout", "Kegsmash", "Rushingjadewind", "Cranekick", "Breath"]
    
    icons_filenames = []
    for (dirpath, dirnames, filenames) in walk(icon_dir):
        icons_filenames.extend(filenames)
        break 
    
    icons = []
    for spell in spells:
        icon = cv2.imread(icon_dir + spell + ".jpg", 0)
        
        if icon is None:
            print("Can't read: ", spell)
            return False

        icons.append(icon)
    
    # cooldowns = ["ardentdefender", "avengingwrath", "shieldofvengeance", "acientkings", "wordofglory", "seraphim", "peacebloom"]
    # cooldowns = ["Healingelixir", "Blackox", "Purifying", "Niuzao", "Celestial", "Weaponsoforder", "Fortifyingbrew", "Legkick", "peacebloom", "Touchofdeath"]
    icons_CDs = []
    for spell in cooldowns:
        icon = cv2.imread(icon_dir + spell + ".jpg", 0)
        
        if icon is None:
            print("Can't read: ", spell)
            return False
        
        icons_CDs.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    icons_covenant = []
    for spell in covenant:
        icons_covenant.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    # print("Icons: ")

    # for icon in icons:
    #     if icon == None:
    #         print("Cant Read an Icon!!!")
    #         return 1

    # for icon in icons_CDs:
    #     if icon == None:
    #         print("Cant Read an Icon!!!")
    #         return 1
    
    print(icons, icons_CDs, icons_covenant)
    
    hotkeys = np.array(hotkeys)
    hotkeys_CDs = np.array(hotkeys_CDs)
    hotkeys_covenant = np.array(hotkeys_covenant)
    hotkeys_party = np.array(hotkeys_party)
    
    print(hotkeys, hotkeys_CDs, hotkeys_covenant, hotkeys_party)
    print(type(hotkeys))
    
    #-----List of Hotkeys-----
    # hotkeys = np.array(["3","F","1","2","G","Q"])
    # hotkeys_CDs = np.array([["LSHIFT", "3"], ["LSHIFT", "E"], ["4"], ["LSHIFT", "F"], ["E"],  ["LCONTROL", "3"], []])
    # hotkeys = np.array(["1","2","E","F","4","3"])
    # hotkeys_CDs = np.array([["LCONTROL", "Q"], ["LCONTROL", "E"], ["LALT", "2"], ["LALT", "1"], ["LALT", "3"],  ["LALT", "5"], ["LSHIFT", "4"], ["LSHIFT", "E"], [], ["G"]])
    
    #-----Set IconSize-----
    icon_dim = (56,56)

    while True:

        if stop == 1:
            break
        
        if(GetWindowText(GetForegroundWindow()) != "World of Warcraft"):
            print("WoW is not the Focus Window!!")
            time.sleep(0.5)
            continue

        #-----Read Screen and Compare to Icons-----
        
        #-----Check if Character is in Combat? -> Red (<100) = Combat, Green  (>100) = Not in Combat----
        # printscreen = screen_record(1493, 798, 5, 5)
        printscreen = screen_record(WA_Position_Combat[0], WA_Position_Combat[1], 5, 5)
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        
        if(printscreen.sum()/100 < 35 or printscreen.sum()/100 > 45):
            print("Not in Combat! (Score = ", printscreen.sum()/100, ")")
            time.sleep(random.uniform(0,0.2))
            continue

        print("(Score = ", printscreen.sum()/100, ")")



        #-----Resize Images to icon_dim-----
        # printscreen = screen_record(1480, 580, 28, 28)
        printscreen = screen_record(WA_Position_Spells[0], WA_Position_Spells[1], WA_Position_Spells[2], WA_Position_Spells[3])
        # printscreen = cv2.resize(printscreen, icon_dim, interpolation = cv2.INTER_LINEAR)
        # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
        # printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('image',printscreen)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        printscreen_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
        # printscreen_CDs = cv2.cvtColor(printscreen_CDs, cv2.COLOR_BGR2RGB)

        printscreen_np = np.asarray(printscreen)
        printscreen_np = printscreen_np / 255.0
        
        printscreen_CDs_np = np.asarray(printscreen_CDs)
        printscreen_CDs_np = printscreen_CDs_np / 255.0

        # printscreen_array = np.array([printscreen_np, printscreen_CDs_np])

        printscreen_kick = screen_record(WA_Position_Kick[0], WA_Position_Kick[1], 5, 5)
        printscreen_kick = cv2.cvtColor(printscreen_kick, cv2.COLOR_BGR2GRAY)
        # print("Shapes: ", printscreen.shape, augmented_icons_np.shape)
        # # Convert into Numpy array and Predict some Samples
        # samples_to_predict = np.array(samples_to_predict)
        # print(samples_to_predict.shape)

        # TF Model PredictionsInterpreter 
        pred_classes = []
        for sample in [printscreen_np.astype(np.float32), printscreen_CDs_np.astype(np.float32)]:
            interpreter.set_tensor(input_details[0]["index"], [sample])
            interpreter.invoke()
            predictions = interpreter.get_tensor(output_details[0]["index"])

            pred_class = np.argmax(predictions, axis = 1)
            pred_classes.append(pred_class[0])
            # score = tf.nn.softmax(predictions)
            score = tfnn.softmax(predictions)
            print(filenames[pred_class[0]], np.max(score[0])*100)

        # predictions = model.predict(printscreen_array)
        # classes = np.argmax(predictions, axis = 1)
        # score = tf.nn.softmax(predictions)
        # for i in range(len(classes)):
        #     print(icons_filenames[classes[i]], np.max(score[i])*100)

        print(spells)
        print(cooldowns) 
        keys2press, keysCD2press = None, None

        for i in range(len(spells)):
            if icons_filenames[pred_classes[0]].split('.')[0] in spells[i]:
                keys2press = hotkeys[i]
                break
        
        for i in range(len(cooldowns)):
            if icons_filenames[pred_classes[1]].split('.')[0] in cooldowns[i]:
                keysCD2press = hotkeys_CDs[i]
                break

        print(keys2press, keysCD2press)

        #-----Select Direct Input Key to press-----
        #-----Kick First if Casting-----
        if(printscreen_kick.sum()/100 == 226):
            print("KICK ACTIVATED!!!")
            for key_kick in hotkeys_kick[0]:
                PressKey(dict_hkeys["_" + key_kick])
                time.sleep(random.uniform(0,0.1))
            for key_kick in hotkeys_kick[0]:
                ReleaseKey(dict_hkeys["_" + key_kick]) 
                time.sleep(random.uniform(0,0.1))
        
        #-----Cooldowns First-----
        if(CDs_True.get()):
            if keysCD2press is not None:
                # print(sh_arr_CDs[0,0])
                for key_CDs in keysCD2press:
                    PressKey(dict_hkeys["_" + key_CDs])
                    time.sleep(random.uniform(0,0.5))
                    
                for key_CDs in keysCD2press:
                    ReleaseKey(dict_hkeys["_" + key_CDs]) 
                    time.sleep(random.uniform(0,0.5))
        
        # #-----Spells Third-----
        if(Spells_True.get()):
            if keys2press is not None:
                # print(sh_arr[0,1])
                key = dict_hkeys["_" + keys2press]
                time.sleep(random.uniform(0,0.5)) 
                PressKey(key)
                ReleaseKey(key)
        
        time.sleep(random.uniform(0,0.4))

WA_Position = WA_Position_Covenant
WA_img = screen_record(WA_Position[0], WA_Position[1], WA_Position[2], WA_Position[3])
WA_img = cv2.cvtColor(WA_img, cv2.COLOR_BGR2GRAY)

WA_img = PIL.Image.fromarray(WA_img)
WA_img = ImageTk.PhotoImage(image=WA_img) 

def Get_SSIM_values():
    #-----Main Rotation-Bot Routine-----
    global config_filepath
    global WA_Position_Spells
    global WA_Position_CDs
    
    icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs = get_config(config_filepath)
    print(icon_dir, spells, cooldowns, hotkeys, hotkeys_CDs)

    icons = []
    for spell in spells:
        icons.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    icons_CDs = []
    for spell in cooldowns:
        icons_CDs.append(cv2.imread(icon_dir + spell + ".jpg", 0))
    
    hotkeys = np.array(hotkeys)
    hotkeys_CDs = np.array(hotkeys_CDs)
    
    #-----Set IconSize-----
    icon_dim = (56,56)
        
    while True:
        if stop == 1:
            break
        
        #-----Read Screen and Compare to Icons-----
        
        #-----Resize Images to icon_dim-----
        printscreen = screen_record(WA_Position_Spells[0], WA_Position_Spells[1], WA_Position_Spells[2], WA_Position_Spells[3])
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        
        printscreen_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
        printscreen_CDs = cv2.cvtColor(printscreen_CDs, cv2.COLOR_BGR2GRAY)
            
        #-----Compare Screen to saved Icons using SSIM-----
        scores = np.array([])
        scores_CDs = np.array([])
        
        #-----stack ssim_score and hotkeys and sort descending afterwards-----
        for icon in icons:
            (score, diff) = compare_ssim(printscreen, icon, full=True)
            scores = np.append(scores, score)
            # scores = np.concatenate((scores, np.array([[score, numb]])))
            # print("SSIM: {}".format(score))
            
        for icon in icons_CDs:
            (score_CDs, diff) = compare_ssim(printscreen_CDs, icon, full=True)
            scores_CDs = np.append(scores_CDs, score_CDs)
            # scores = np.concatenate((scores, np.array([[score, numb]])))
            # print("SSIM: {}".format(score))
    
        sh_arr = np.stack((scores, hotkeys), axis=1)
        sh_arr = sh_arr[np.argsort(sh_arr[:, 0])][::-1]
        
        sh_arr_CDs = np.stack((scores_CDs, hotkeys_CDs), axis=1)
        sh_arr_CDs = sh_arr_CDs[np.argsort(sh_arr_CDs[:, 0])][::-1]
        
        print(sh_arr)
        print(sh_arr_CDs)
        time.sleep(0.5)
        

# def start_Get_SSIM_values():
#     # Assign global variable and initialize value
#     global stop
#     stop = 0
    
#     global config_filepath
#     global WA_Position_Spells
#     WA_Position_Spells = WA_Position
    
#     global WA_Position_CDs
#     WA_Position_CDs = WA_Position
    
#     # Create and launch a thread 
#     t = Thread(target = Get_SSIM_values)
#     t.start()
# from tkinter import font as tkFont
# helv36 = tkFont.Font(family='Helvetica', size=20, weight='bold')
# 
# Button_GetSSIM = Button(app,
#                       width=10,
#                       height=5,
#                       bg="#00FF00",
#                       fg="Black", 
#                       text="Start",
#                       font = helv36,
#                       command=start_Get_SSIM_values)
# Button_GetSSIM.grid(row=11, column=0)