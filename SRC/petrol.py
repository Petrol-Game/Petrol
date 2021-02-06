import random
import json
import os
import importlib
import platform
import sys

import petrolasset as asset
import petrolextra as extra

# log only works on UNIX based systems, do not enable on release, beta or alpha versions of this software.

dolog = False

logdata = ""

if dolog:
    import log

    # create log, and create event for load

    logdata = log.log()
    logdata.add("Loaded Petrol")

def addlog(msg, ltype = "INFO"):
    if dolog:
        logdata.add(msg, ltype)

# title function shows the title and info at the begining
def title(version):
    if platform.system() == "Windows":
        asset.clear()

        print("Petrol")
    else:
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
    print("V: " + version)
    print()
    print("[PRESS ENTER TO START]")
    print("for extra options type extra")
    print()
    #-----

#this is the main loop the code runs on
while True:
    #open the settings file and set the settings acordingly

    try:
        d = asset.openfi("ASSETS/SETTINGS/config.txt", "r")
        settings = d.read()
        settingspl = settings.split("\n")
        de = settingspl[0]
        d.close()

        debug = bool(de)

        addlog("Settings loaded in")
    except Exception as Ex:
        addlog("Failed loading settings - " + Ex.__str__(), "FATAL")

        break

    #-----

    #open STATS file

    try:
        d = asset.openfi("ASSETS/STATS/data.txt", "r")
        stats = d.read()
        stats = asset.stats(stats.split(";")[0], stats.split(";")[1])
        d.close()

        addlog("Loaded stats")
    except Exception as Ex:
        addlog("Failed loading stats - " + Ex.__str__(), "FATAL")

        break

    #---

    info = asset.info()

    a = "++more cheese++"

    while a != "":
        last = None
        
        title(info.version)
        
        a = input()

        if a.upper() == "EXTRA":
            extra.menu(info, stats)

            #reopen the settings file because settings may have been changed by the menu

            try:
                d = asset.openfi("ASSETS/SETTINGS/config.txt", "r")
                settings = d.read()
                settings = settings.split("\n")
                de = settings[0]
                d.close()

                debug = bool(de)

                addlog("Settings loaded in")
            except:
                addlog("Failed loading settings", "FATAL")

                break

            #-----

    print("starting game")

    #this loads in the possible maps and asks the user wich one they want to play

    choice = None

    try:
        posmaps = []

        try:
            posmaps = os.listdir("./ASSETS/MAPS")
        except:
            posmaps = os.listdir("./SRC/ASSETS/MAPS")

        posmaps.remove(".DS_Store")

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
            except Exception as e:
                print(e)

                input()

                pass

        maptxt = mapfi.read()
        mapfi.close()
        mapfi = None

        mapd = json.loads(maptxt)
        maptxt = None

        asset.clear()
        
        print("playing on map: " + posmaps[int(choice)])
        print()

        addlog("Chossen map: " + choice)
    except:
        addlog("Failed loading map")

        break
    #-----
    
    #this sets up the player variable, and the place where all the custom map code is run

    try:
        p1 = asset.player(mapd)

        callback = setup.callset(p1)

        addlog("Player setup")
    except:
        addlog("Failed setting up Player", "FATAL")

        break

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

        addlog("Player command: " + com)

        if com[:2].upper() == "GO":
            posib = []

            for u in mapd[p1.posi()]["dirs"]:
                posib.append(u)

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
                    if item.upper() == com[7:].upper():
                        p1.inventory.items.append(item.upper())
                        mapd[p1.posi()]["items"] = None

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
        elif com[:5].upper() == "SPEAK":
            callback.speak(p1,com[6:])
        elif com[:4].upper() == "DROP":
            did = False

            for item in p1.inventory.items:
                if item.__str__().upper() == com[5:].upper():
                    did = True

                    p1.inventory.items.remove(item.__str__())
                    mapd[p1.pos.__str__()]["items"].append(item.__str__())

                    print("Dropped")

                if not(did):
                    print("Cound not drop " + com[5:].upper())
        elif com.upper() == "END":
            print("Exiting")
            print()
            
            sys.exit()
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
    print()
    
    if p1.won:
        stats.addwin()
        
        if platform.system() == "Windows":
            print("You Won!")
        else:
            out = asset.openfi("ASSETS/END/WIN/0.txt")

            print(out.read())

            out.close()
    else:
        stats.addloose()
        
        if platform.system() == "Windows":
            print("You Lost!")
        else:
            out = asset.openfi("ASSETS/END/LOST/0.txt")

            print(out.read())

            out.close()

    d = asset.openfi("ASSETS/STATS/data.txt", "w")
    stat = str(stats.win) + ";" + str(stats.loose)
    d.write(stat)
    d.close()

    print()
    input()
