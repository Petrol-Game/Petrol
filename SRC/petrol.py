import time
import random
import json

import petrolasset as asset

import MAPS.SCHOOL.setup as setup

while True:
    debug = True

    mapfi = asset.openf("MAPS/SCHOOL/map.json", "r")

    maptxt = mapfi.read()
    mapfi.close()
    mapfi = None

    mapd = json.loads(maptxt)
    maptxt = None

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
    
    print("playing on map: SCHOOL")
    print()
       
    p1 = asset.player(mapd)

    callback = setup.callset()

    while p1.health > 0:
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
            credd = asset.openfi("MAPS/SCHOOL/INFO.json", "r")
        
            cred = credd.read()
            credd.close()

            asset.petrolcredits(cred)
        else:
            # all debug commands go here, they are only execed when debug flag is set, this is disabled in release builds.

            if debug:
                if com.upper() == "TP":
                    print("[DEBUG]")
                    print("debug command - not garanteed to work")
                    print()
                    p1.pos = asset.position(input("x: "), input("y: "))
            else:
                print("invalid command " + '"' + com.upper() + '"' + ", if you believe this is an error please report in on the issues page, on the github repository")

    asset.clear()

    if p1.won:
        callback.win()
    else:
        callback.loose()

    print()
    input()