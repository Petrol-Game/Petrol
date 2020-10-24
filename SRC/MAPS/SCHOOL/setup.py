import petrolasset

class callset:
    def newroom(coords, mapp):
        go = ""

        for u in mapp[coords]["dirs"]:
            i = mapp[coords]["dirs"][u]

            if len(go) >= 1:
                go += ", " + i
            else:
                go = i
        
        print("you are in the " + str(mapp[coords]["name"]) + " room, you can go " + str(go))