from datetime import datetime
import os
import errno

loczip = "/tmp/Petrol/LOG/runtime.log"

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
        if not os.path.exists(os.path.dirname(loczip)):
            try:
                os.makedirs(os.path.dirname(loczip))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                
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
    fi = open(loczip, "w")

    fi.write(data.__str__())

    fi.close