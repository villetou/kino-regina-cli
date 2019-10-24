from colors import bcolors

def printDelimiter():
    print ("────────────────────────────────────")

def printHeader(*arg):
    print (bcolors.UNDERLINE)
    print (*arg, bcolors.ENDC)

def printKinoReginaArt():
    print (bcolors.HEADER, r"""
|)  o        _      ,_   _  _, o        _,  
|/) | /|/|  / \_   /  | |/ / | | /|/|  / |  
| \/|/ | |_/\_/       |/|_/\/|/|/ | |_/\/|_/
                             (|          """, bcolors.ENDC)
