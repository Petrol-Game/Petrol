import random

class npc:
    def __init__(self, name, position, health, relation):
        self.name = name
        self.position = position
        self.health = health
        self.relation = relation

    def __str__(self):
        out = "[" + self.name + "] - " + self.position.__str__() + " - [H" + str(self.health) + "] - [R" + str(self.relation) + "]"
        
        return out

class position:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def gonorth(self):
        self.y -= 1

    def goeast(self):
        self.x += 1

    def gosouth(self):
        self.y += 1

    def gowest(self):
        self.x -= 1

    def __str__(self):
        out = str(self.x) + "/" + str(self.y)

        return out

class item:
    def __init__(self, code):
        self.code = int(code)

    def __str__(self):
        out = self.code.__str__()

        return out

def settogo(stuff):
    out = []

    for i in stuff:
        do = i.replace("N", "GO NORTH")

        if do == "GO NORTH":
            out.append(do)
        
        do = i.replace("E", "GO EAST")

        if do == "GO EAST":
            out.append(do)

        do = i.replace("S", "GO SOUTH")

        if do == "GO SOUTH":
            out.append(do)

        do = i.replace("W", "GO WEST")

        if do == "GO WEST":
            out.append(do)

    return out


def checkmap(mapu):
    done = []

    current = mapu["SPAWN"]["coord"]

    todo = []

    while True:
        tch = mapu[current]["dirs"]

        for u in tch:
            i = tch[u]

            c = "0"
            nc = "pp"

            if i == "N":
                c = "S"
                nc = current[0] + "/" + str(int(current[2]) - 1)
            elif i == "E":
                c = "W"
                nc = str(int(current[0]) - 1) + "/" + current[2]
            elif i == "S":
                c = "N"
                nc = current[0] + "/" + str(int(current[2]) + 1)
            elif i == "W":
                c = "E"
                nc = str(int(current[0]) + 1) - "/" + current[2]
            else:
                return False
            
            if not(nc in done):
                todo.append(nc)
            try:
                todo.remove(current)
            except:
                pass
                
            done.append(current)

            notin = True

            for p in mapu[nc]["dirs"]:
                pp = mapu[nc]["dirs"][p]

                if pp == c:
                    notin = False

                    pass

            if notin:
                print(nc)

                return False

            if len(todo) == 0:
                return True
            else:
                current = todo[0]