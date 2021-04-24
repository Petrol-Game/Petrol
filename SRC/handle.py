posplatforms = ['DESK']

platform = posplatforms[0]

def out(*args):
    out = ""

    for arg in args:
        out += " " + arg.__str__()

    if platform == "STAN":
        print(out)

def get(*args):
    out = ""

    for arg in args:
        out += " " + arg.__str__()

    if platform == "DESK":
        return str(input(out))

def setup():
    if platform == "DESK":
        return