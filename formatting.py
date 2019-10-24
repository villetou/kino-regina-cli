from colors import bcolors

def printDelimiter():
    print ("────────────────────────────────────")

def printHeader(*arg):
    print (bcolors.UNDERLINE)
    print (*arg, bcolors.ENDC)

def printKinoReginaArt():
    print (bcolors.HEADER, r"""
    __ __ _                ____             _            
   / //_/(_)___  ____     / __ \___  ____ _(_)___  ____ _
  / ,<  / / __ \/ __ \   / /_/ / _ \/ __ `/ / __ \/ __ `/
 / /| |/ / / / / /_/ /  / _, _/  __/ /_/ / / / / / /_/ / 
/_/ |_/_/_/ /_/\____/  /_/ |_|\___/\__, /_/_/ /_/\__,_/  
                                  /____/                 
    """, bcolors.ENDC)
