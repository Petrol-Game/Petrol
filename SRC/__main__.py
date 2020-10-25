print()
print("Loading Petrol")
print()

try:
    from petrol import *
except Exception as e:
    print("ERROR")
    print()
    print(e.__str__())