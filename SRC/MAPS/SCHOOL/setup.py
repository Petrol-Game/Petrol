import petrolasset as asset

class callset:
    def __init__(self):
        npcs = []
        
        add = asset.npc("Mr Road", asset.position(0, 0), 10, 0)
        npcs.append(add)

        self.npcs = npcs

    def attack(self, damage, wepon, target, coord):
        for npc in self.npcs:
            if npc.name.upper() == target.upper():
                if npc.position.__str__() == coord.__str__():
                    npc.health -= float(damage)

                    if npc.health <= 0:
                        print("You killed " + target.upper() + ", with a " + wepon.upper())
                    else:
                        print("You attacked " + target.upper() + ", with a " + wepon.upper())
                    
                    return
        
        print("You could not attack " + target.upper())

    def newroom(self, coords, mapp):
        go = []

        for u in mapp[coords]["dirs"]:
            i = mapp[coords]["dirs"][u]

            if len(go) >= 1:
                go.append(", " + i.__str__())
            else:
                go.append(i.__str__())
        
        gofa = asset.settoin(go)

        gof = ""

        for i in gofa:
            gof += i.__str__()

        room = str(mapp[coords]["name"])

        if room == "outside":
            print("you are " + room + ", you can go " + gof.__str__())
        elif room == "concourse":
            print("you are in the " + room + ", you can go " + gof.__str__())
        elif room == "corridor":
            print("you are in a " + room + ", you can go " + gof.__str__())
        else:
            print("you are in the " + room + " room, you can go " + gof.__str__())

        it = []

        try:
            for item in mapp[coords]["items"]:
                ite = mapp[coords]["items"][item]

                it.append(ite)
        except:
            pass
        
        floor = ""
        dofloor = False

        if len(it) > 0:
            dofloor = True

            out = ""

            for i in it:
                out += "a " + i + ", "

            out = out[:-2]

            floor = "on the floor there is, " + out
        
        tosay = []

        for npc in self.npcs:
            if npc.position.__str__() == coords.__str__():
                tosay.append(npc.name)

        people = ""
        dopeople = False

        if len(tosay) > 0:
            dopeople = True

            out = ""

            for i in tosay:
                out += i + ", "
            
            out = out[:-2]

            people = "you are joined by, " + out

        if dopeople and dofloor:
            print(people + " and " + floor)
        elif dopeople:
            print(people)
        elif dofloor:
            print(floor)