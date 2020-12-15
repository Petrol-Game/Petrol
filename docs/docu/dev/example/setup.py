import petrolasset as asset

class callset:
    def attack(damage, wepon, target, coord, npcs):
        for npc in npcs:
            if npc.name.upper() == target.upper():
                if npc.position.__str__() == coord.__str__():
                    npc.health -= float(damage)

                    if npc.health <= 0:
                        print("You killed " + target.upper() + ", with a " + wepon.upper())
                    else:
                        print("You attacked " + target.upper() + ", with a " + wepon.upper())
                    
                    return
        
        print("You could not attack " + target.upper())

    def newroom(coords, mapp, player, npcs):
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

        for npc in npcs:
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

    def room(player, coords, npcs):
        damage = []
        for npc in npcs:
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