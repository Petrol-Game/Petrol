import petrolasset as asset

class callset:
    def __init__(self, player):
        npcs = []

        npcs.append(asset.npc("Mr Road", asset.position(0, 0), 10, 0, 1))
        npcs.append(asset.npc("Mrs Armstrong", asset.position(3, 2), 10, 0, 1))
        npcs.append(asset.npc("Mr Thyme", asset.position(6, 5), 10, 0, 5))
        npcs.append(asset.npc("Mr Almost", asset.position(10, 5), 10, 0, 10))

        self.npcs = npcs

        player.health = 10

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

    def newroom(self, coords, mapp, player):
        go = []

        for u in mapp[coords]["dirs"]:
            
            go.append(u.__str__())
        
        gof = ""
        
        for i in go:
            coo = asset.position(coords.split("/")[0],coords.split("/")[1])
            coop = coo
            
            if i == "N":
                coop.gonorth()
                
                gof += ", to the north their is " + mapp[coop.__str__()]["name"]
            if i == "E":
                coop.goeast()
                
                gof += ", to the east their is " + mapp[coop.__str__()]["name"]
            if i == "S":
                coop.gosouth()
                
                gof += ", to the south their is " + mapp[coop.__str__()]["name"]
            if i == "W":
                coop.gowest()
                
                gof += ", to the west their is " + mapp[coop.__str__()]["name"]

        room = str(mapp[coords]["name"])

        if room == "outside":
            print("you are " + room + gof)
        elif room == "concourse" or room == "refectory":
            print("you are in the " + room + gof)
        elif room == "corridor":
            print("you are in a " + room + ", " + gof)
        else:
            print("you are in the " + room + " room" + gof)

        it = []

        try:
            for item in mapp[coords]["items"]:

                it.append(item)
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
        
    def room(self, player, coords):
        damage = []
        for npc in self.npcs:
            if npc.position.__str__() == coords.__str__():
                if npc.relation == 0:
                    if npc.health >= 0:
                        damage.append(npc)
        
        print()

        dama = ""

        for dam in damage:
            player.health -= dam.damage

            dama += dam.name + ", "

        if len(dama) > 0:
            print(dama + "attacked you, your health is at " + player.health.__str__())

    def interact(self, item, player):
        if item.upper() == "SHUTDOWN BUTTON":
            print()

            if input("Are you sure you want to do this? [Y/N] ").upper() == "Y":
                player.won = True
                player.health = 0
        elif item.upper() == "APPLE":
            player.health += 3

            if player.health > 10:
                player.health = player.health - (player.health - 10)

            print("you ate an apple, your health is now at, " + player.health.__str__())
        else:
            print("sorry you cannot interact with this object")

    def speak(self, player, to):
        inroom = False

        for npc in self.npcs:
            if npc.name.upper() == to.upper():
                if npc.position.x == player.pos.x:
                    if npc.position.y == player.pos.y:
                        inroom = True

                        break

        if inroom:
            print("Sorry, " + to.upper() + " doesnt want to talk to you right now")
        else:
            print("Sorry, " + to.upper() + " isnt in this room")
