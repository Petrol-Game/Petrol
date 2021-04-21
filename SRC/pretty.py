import os

class bcolors:
    ENDC = '\033[0m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

def setup():
    os.system('')

def pprint(*args):
    repla = [['<ENDC>', bcolors.ENDC],['<BOLD>', bcolors.BOLD],['<UNDER>', bcolors.UNDERLINE],['<BLACK>', bcolors.BLACK],['<RED>', bcolors.RED],['<GREEN>', bcolors.GREEN],['<YELLOW>', bcolors.YELLOW],['<BLUE>', bcolors.BLUE],['<MAGENTA>', bcolors.MAGENTA],['<CYAN>', bcolors.CYAN],['<WHITE>', bcolors.WHITE]]

    out = ""
    
    for i in args:
        out += " " + i.__str__()
        
    for r in repla:
        out = out.replace(r[0], r[1])
    
    print(out)

def iinput(*args):
    repla = [['<ENDC>', bcolors.ENDC],['<BOLD>', bcolors.BOLD],['<UNDER>', bcolors.UNDERLINE],['<BLACK>', bcolors.BLACK],['<RED>', bcolors.RED],['<GREEN>', bcolors.GREEN],['<YELLOW>', bcolors.YELLOW],['<BLUE>', bcolors.BLUE],['<MAGENTA>', bcolors.MAGENTA],['<CYAN>', bcolors.CYAN],['<WHITE>', bcolors.WHITE]]

    out = ""
    
    for i in args:
        out += " " + i.__str__()
        
    for r in repla:
        out = out.replace(r[0], r[1])
    
    return input(out)

def calc(*args):
    repla = [['<ENDC>', bcolors.ENDC],['<BOLD>', bcolors.BOLD],['<UNDER>', bcolors.UNDERLINE],['<BLACK>', bcolors.BLACK],['<RED>', bcolors.RED],['<GREEN>', bcolors.GREEN],['<YELLOW>', bcolors.YELLOW],['<BLUE>', bcolors.BLUE],['<MAGENTA>', bcolors.MAGENTA],['<CYAN>', bcolors.CYAN],['<WHITE>', bcolors.WHITE]]

    out = ""

    for i in args:
        out += " " + i.__str__()
        
    for r in repla:
        out = out.replace(r[0], r[1])
    
    return out
