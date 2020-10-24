import time
import random
import json

import petrolasset as asset

import MAPS.SCHOOL.setup as setup

mapfi = None

try:
    mapfi = open("./SRC/MAPS/SCHOOL/map.json", "r")
except:
    mapfi = open("./MAPS/SCHOOL/map.json", "r")

maptxt = mapfi.read()
mapfi.close()

mapd = json.loads(maptxt)
       
p1 = asset.player(mapd)

callback = setup.callset

last = None

while True:
    if last != p1.posi():
        print()
        print(callback.newroom(p1.posi(), mapd))
    
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
        print("i will kill them")
    else:
        print("invalid command " + '"' + com.upper() + '"' + ", if you believe this is an error please report in on the issues page, on the github repository")