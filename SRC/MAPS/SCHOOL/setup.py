import petrolasset

class callset:
    def newroom(coords, mapp):
        go = []

        for u in mapp[coords]["dirs"]:
            i = mapp[coords]["dirs"][u]

            if len(go) >= 1:
                go.append(", " + i.__str__())
            else:
                go.append(i.__str__())
        
        gofa = petrolasset.settoin(go)

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