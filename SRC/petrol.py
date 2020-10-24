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

class player:
    def __init__(self):
        print("[SETUP]")
        print()
        print("name: ")
        self.name = input()
        print()

        self.health = 10
        self.inventory = ['torch']

        self.pos = asset.position(int(mapd["SPAWN"]["coord"][0]),int(mapd["SPAWN"]["coord"][2]))

    def __str__(self):
        out = "[" + self.name + "] - [H" + str(self.health) + "] - " + self.pos.__str__() + " - " + self.inventory.__str__()

        return out

    def addinv(self, item):
        self.inventory.append(item)

    def reminv(self, item):
        self.inventory.remove(item)

    def posi(self):
        out = self.pos.__str__()

        return out
       
p1 = player()

callback = setup.callset

while True:
    print()
    print(callback.newroom(p1.posi(), mapd))
    print()

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