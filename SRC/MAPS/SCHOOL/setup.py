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