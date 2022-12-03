# printscreen_CDs = screen_record(1480, 682, 28, 28)
        printscreen_CDs = screen_record(WA_Position_CDs[0], WA_Position_CDs[1], WA_Position_CDs[2], WA_Position_CDs[3])
        printscreen_CDs = cv2.cvtColor(printscreen_CDs, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('image',printscreen_CDs)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        printscreen_covenant = screen_record(WA_Position_Covenant[0], WA_Position_Covenant[1], WA_Position_Covenant[2], WA_Position_Covenant[3])
        printscreen_covenant = cv2.cvtColor(printscreen_covenant, cv2.COLOR_BGR2GRAY)
        
        printscreen_kick = screen_record(WA_Position_Kick[0], WA_Position_Kick[1], 5, 5)
        printscreen_kick = cv2.cvtColor(printscreen_kick, cv2.COLOR_BGR2GRAY)
        
        if(first_run):
            # printscreen_old = printscreen
            time.sleep(3)
            first_run = False

        #-----Healbot: Read Party Health-----        
        if(Healer_True.get()):
            #-----Check if Character is in Casting -> Red (<100) = Casting, Green  (>100) = Not in Casting----
            printscreen = screen_record(WA_Position_Casting[0], WA_Position_Casting[1], WA_Position_Casting[2], WA_Position_Casting[3])
            printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
            
            if(printscreen.sum()/100 > 45):
                print("I'm Casting already! (Score = ", printscreen.sum()/100, ")")
                time.sleep(random.uniform(0,0.2))
                continue

            frame_width = 40 
            printscreen_party = ImageGrab.grab(bbox=(WA_Position_Party[0], WA_Position_Party[1], WA_Position_Party[0] + frame_width*5, WA_Position_Party[1] + 1))
            party_health = []

            for i in range(5):
                p = printscreen_party.getpixel((i*frame_width, 0)) 

                health = convert_rbg_to_int(p)
                party_health.append([i, health])

            party_health.sort(key=lambda x: x[1])
            print(party_health)

            #-----Target Party Members-----
            for health in party_health:
                if health[1] == 0:
                    continue
                party_key = health[0]
                break

            # Skip if the lowest partymember is nearly max health
            if health[1] / 1000 > 97:
                print("Skipping: Party is Max Health!")
                continue

            print(hotkeys_party[party_key])
            
            PressKey(dict_hkeys["_" + hotkeys_party[party_key]])
            time.sleep(random.uniform(0,0.3))
            ReleaseKey(dict_hkeys["_" + hotkeys_party[party_key]]) 
            time.sleep(random.uniform(0,0.3))
        
        #-----Compare Screen to saved Icons using SSIM-----
        scores = np.array([])
        scores_CDs = np.array([])
        scores_Covenant = np.array([])
        
        #-----stack ssim_score and hotkeys and sort descending afterwards-----
        for icon in icons:
            (score, diff) = compare_ssim(printscreen, icon, full=True)
            scores = np.append(scores, score)
            # scores = np.concatenate((scores, np.array([[score]])))
            # print("SSIM: {}".format(score))
         
        for icon in icons_CDs:
            (score_CDs, diff) = compare_ssim(printscreen_CDs, icon, full=True)
            scores_CDs = np.append(scores_CDs, score_CDs)
            # scores = np.concatenate((scores, np.array([[score]])))
            print("SSIM: {}".format(score_CDs))
            
        for icon in icons_covenant:
            (score_Covenant, diff) = compare_ssim(printscreen_covenant, icon, full=True)
            scores_Covenant = np.append(scores_Covenant, score_Covenant)
        
        sh_arr = np.stack((scores, hotkeys), axis=1)
        sh_arr = sh_arr[np.argsort(sh_arr[:, 0])][::-1]

        sh_arr_CDs = np.stack((scores_CDs, hotkeys_CDs), axis=1)
        sh_arr_CDs = sh_arr_CDs[np.argsort(sh_arr_CDs[:, 0])][::-1]
        
        sh_arr_Covenant = np.stack((scores_Covenant, hotkeys_covenant), axis=1)
        sh_arr_Covenant = sh_arr_Covenant[np.argsort(sh_arr_Covenant[:, 0])][::-1]
        
        print(sh_arr[0,1])
        print(sh_arr_CDs[0,1])

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
        if(sh_arr_CDs[0,0] > 0.1 and CDs_True.get()):
            # print(sh_arr_CDs[0,0])
            for key_CDs in sh_arr_CDs[0,1]:
                PressKey(dict_hkeys["_" + key_CDs])
                time.sleep(random.uniform(0,0.5))
                
            for key_CDs in sh_arr_CDs[0,1]:
                ReleaseKey(dict_hkeys["_" + key_CDs]) 
                time.sleep(random.uniform(0,0.5))
        
        #-----Covenant Utility Second
        if(sh_arr_Covenant[0,0] > 0.1 and Covenant_True.get()):
            # print(sh_arr_Covenant[0,1])
            for key_Covenant in sh_arr_Covenant[0,1]:
                PressKey(dict_hkeys["_" + key_Covenant])
                time.sleep(random.uniform(0,0.5))
                
            for key_Covenant in sh_arr_Covenant[0,1]:
                ReleaseKey(dict_hkeys["_" + key_Covenant]) 
                time.sleep(random.uniform(0,0.5))
        
        # #-----Spells Third-----
        if(Spells_True.get()):
            # print(sh_arr[0,1])
            key = dict_hkeys["_" + sh_arr[0,1]]
            time.sleep(random.uniform(0,0.5)) 
            PressKey(key)
            ReleaseKey(key)