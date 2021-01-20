from datetime import datetime

import petrolasset as asset

loc = "ASSETS/LOG/runtime.log"

class entry:
    def __init__(self, info, level = "INFO"):
        self.level = level
        self.info = info
        
        self.time = datetime.now().__str__()

    def __str__(self):
        ret = self.time + " - " + self.level + ": " + self.info

        return ret

class log:
    def __init__(self):
        self.data = []

    def add(self, info, level = "INFO"):
        data = entry(info, level)

        self.data.append(data)

        save(self)

    def __str__(self):
        ret = ""

        for dat in self.data:
            ret += dat.__str__() + "\n"

        return ret
    
def save(data):
    fi = asset.openfi(loc, "w")

    fi.write(data.__str__())

    fi.close