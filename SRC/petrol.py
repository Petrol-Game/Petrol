import time
import random
import json
import os
import importlib

import petrolasset as asset

# title function shows the title and info at the begining
def title():
    asset.clear()

    #this loads in the file, defining how many variations of the ascii art their are
    logoa = asset.openfi("ASSETS/LOGO/A.txt", "r")

    logoaa = int(logoa.read())

    logoa.close()
    logoa = None
    #-----

    #this loads in one of the ascii art logos and displays it alongside other info
    logo = asset.openfi("ASSETS/LOGO/" + str(random.randint(0,logoaa)) + ".txt", "r")

    print(logo.read())

    logo.close()
    logo = None
    
    print()
    print("V: 1.0.0 B3")
    print()
    print("[PRESS ENTER TO START]")
    print("for extra options type extra")
    print()
    #-----

#this is the main loop the code runs on
while True:
    #open the settings file and set the settings acordingly
    d = asset.openfi("ASSETS/SETTINGS/config.txt", "r")
    settings = d.read()
    settings = settings.split("\n")
    de = settings[0]
    d.close()

    debug = None

    if de == "1":
        debug = True
    else:
        debug = False

    last = None
    #-----

    title()
    
    a = input()

    # this is the script for the menu
    if a.upper() == "EXTRA":
        dodo = True

        while dodo:
            asset.clear()

            print("[EXTRA]")
            print()

            print("0: Settings")
            print("1: Petrol Credits")
            print("2: Source")
            print("3: License")
            print("4: Exit")
            print()

            a = int(input("? "))

            print()

            if a == 0:
                dododo = True

                while dododo:
                    asset.clear()
                    
                    print("[settings]")
                    print()
                    print("0: Debug - " + str(debug))
                    print("1: Back")
                    print()

                    b = int(input("? "))

                    if b == 0:
                        debug = not(debug)

                        togo = None

                        if debug:
                            togo = "1"
                        else:
                            togo = "0"

                        togofi = asset.openfi("ASSETS/SETTINGS/config.txt", "w")
                        settings[0] = togo

                        togofi.write(asset.settingsset(settings))

                        togofi.close()
                    elif b == 1:
                        dododo = False
            elif a == 1:
                print("Petrol Made by AUnicornWithNoLife")

                input()
            elif a == 2:
                print("https://github.com/AUnicornWithNoLife/Petrol")

                input()
            elif a == 3:
                li = asset.openfi("ASSETS/LI/LICENSE", "r")
                print(li.read())
                li.close()

                input()
            elif a == 4:
                asset.clear()

                dodo = False
            else:
                print("Error")

                input()

            print()
        #------

        print("starting game")

    #this loads in the possible maps and asks the user wich one they want to play
    posmaps = []

    try:
        posmaps = os.listdir("./ASSETS/MAPS")
    except:
        posmaps = os.listdir("./SRC/ASSETS/MAPS")

    choice = None

    possib = True

    while possib:
        asset.clear()

        print("MAPS:")

        i = 0

        for posm in posmaps:
            print(i.__str__() + ": " + posm)

            i += 1

        print()
        choice = input("? ")

        try:
            mapfi = asset.openfi("ASSETS/MAPS/" + posmaps[int(choice)] + "/map.json", "r")
            setup = importlib.import_module("ASSETS.MAPS." + posmaps[int(choice)] + ".setup")

            possib = False
        except:
            pass

    maptxt = mapfi.read()
    mapfi.close()
    mapfi = None

    mapd = json.loads(maptxt)
    maptxt = None

    asset.clear()
    
    print("playing on map: " + posmaps[int(choice)])
    print()
    #-----
    
    #this sets up the player variable, and the place where all the custom map code is run
    p1 = asset.player(mapd)

    callback = setup.callset(p1)
    #-----

    #this loop is where the gameplay happens
    while p1.health >= 0:
        if last != p1.posi():
            print()
            callback.newroom(p1.posi(), mapd, p1)
    
        callback.room(p1, p1.posi())
    
        print()

        last = p1.posi()

        com = input(">> ")

        if com[:2].upper() == "GO":
            posib = []

            for u in mapd[p1.posi()]["dirs"]:
                posib.append(mapd[p1.posi()]["dirs"][u])

            posib = asset.settogo(posib)

            if com.upper() in posib:
                if com.upper() == "GO NORTH":
                    p1.pos.gonorth()
                elif com.upper() == "GO EAST":
                    p1.pos.goeast()
                elif com.upper() == "GO SOUTH":
                    p1.pos.gosouth()
                elif com.upper() == "GO WEST":
                    p1.pos.gowest()
            else:
                print("sorry you cant travel that way") 
        elif com[:4].upper() == "KILL":
            callback.attack(p1.fist, "fist", com[5:], p1.pos)
        elif com.upper() == "BACKPACK":
            print()
            print(p1.inventory.__str__())
        elif com[:6].upper() == "PICKUP":
            # allows you to pickup items, still need to add functoins to allow you to drop items

            for item in mapd[p1.posi()]["items"]:
                try:
                    if mapd[p1.posi()]["items"][item].upper() == com[7:].upper():
                        p1.inventory.items.append(asset.item(mapd[p1.posi()]["items"][item].upper()))
                        mapd[p1.posi()]["items"][item] = None

                        print("picked up " + com[7:].upper())
                    else:
                        print("sorry could not find " + com[7:].upper())
                except:
                    print("sorry could not find " + com[7:].upper())
        elif com[:3].upper() == "USE":
            pos = p1.inventory.items
            cando = False

            for p in pos:
                if p.__str__().upper() == com[4:].upper():
                    cando = True

                    break

            if cando:
                callback.interact(com[4:], p1)
            else:
                print("sorry you dont have that item")
        elif com.upper() == "CREDITS":
            asset.clear()

            credd = asset.openfi("ASSETS/MAPS/SCHOOL/INFO.json", "r")
        
            cred = credd.read()
            credd.close()

            asset.petrolcredits(cred)

            asset.clear()

            last = None
        else:
            # all debug commands go here, they are only execed when debug flag is set, this is disabled in release builds.

            if debug:
                if com.upper() == "TP":
                    print("[DEBUG]")
                    print("debug command - not garanteed to work")
                    print()

                    p1.pos = asset.position(input("x: "), input("y: "))
                elif com.upper() == "WIN":
                    print("[DEBUG]")
                    print("debug command - not garanteed to work")
                    print()

                    p1.won = True
                    p1.health = -1
                elif com.upper() == "LOOSE":
                    print("[DEBUG]")
                    print("debug command - not garanteed to work")
                    print()

                    p1.won = False
                    p1.health = -1
                else:
                    print("invalid command " + '"' + com.upper() + '"' + ", if you believe this is an error please report in on the issues page, on the github repository")
            else:
                print("invalid command " + '"' + com.upper() + '"' + ", if you believe this is an error please report in on the issues page, on the github repository")

    asset.clear()

    #this handles the endgame stuff
    if p1.won:
        out = asset.openfi("ASSETS/END/WIN/0.txt")

        print(out.read())

        out.close()
    else:
        out = asset.openfi("ASSETS/END/LOST/0.txt")
        
        print(out.read())

        out.close()

    print()
    input()