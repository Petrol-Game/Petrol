import time
import random
import json
import os
import importlib

import petrolasset as asset

while True:
    debug = True

    last = None

    logoa = asset.openfi("ASSETS/LOGO/A.txt", "r")

    logoaa = int(logoa.read())

    logoa.close()
    logoa = None

    logo = asset.openfi("ASSETS/LOGO/" + str(random.randint(0,logoaa)) + ".txt", "r")

    print(logo.read())

    logo.close()
    logo = None
    
    print()
    print("[PRESS ENTER TO START]")
    print()
    
    input()

    asset.clear()

    print("MAPS:")

    posmaps = []

    try:
        posmaps = os.listdir("./ASSETS/MAPS")
    except:
        posmaps = os.listdir("./SRC/ASSETS/MAPS")

    i = 0

    for posm in posmaps:
        print(i.__str__() + ": " + posm)

    print()
    choice = input("? ")

    mapfi = asset.openfi("ASSETS/MAPS/" + posmaps[int(choice)] + "/map.json", "r")
    setup = importlib.import_module("ASSETS.MAPS." + posmaps[int(choice)] + ".setup")

    maptxt = mapfi.read()
    mapfi.close()
    mapfi = None

    mapd = json.loads(maptxt)
    maptxt = None

    asset.clear()
    
    print("playing on map: " + posmaps[int(choice)])
    print()
       
    p1 = asset.player(mapd)

    callback = setup.callset()

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

                    input()
                elif com.upper() == "WIN":
                    print("[DEBUG]")
                    print("debug command - not garanteed to work")
                    print()

                    p1.won = True
                    p1.health = -1

                    input()
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