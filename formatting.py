from colors import bcolors

def print_delimiter():
    print ("────────────────────────────────────")

def print_header(*arg):
    print (bcolors.UNDERLINE)
    print (*arg, bcolors.ENDC)

def print_kino_regina_art():
    print (bcolors.HEADER, r"""
|)  o        _      ,_   _  _, o        _,  
|/) | /|/|  / \_   /  | |/ / | | /|/|  / |  
| \/|/ | |_/\_/       |/|_/\/|/|/ | |_/\/|_/
                             (|          """, bcolors.ENDC)

def print_shows(shows_by_date: dict):
    weekdays = {
        0: "Maanantai",
        1: "Tiistai",
        2: "Keskiviikko",
        3: "Torstai",
        4: "Perjantai",
        5: "Lauantai",
        6: "Sunnuntai"
    }

    for _, shows in shows_by_date.items():
        day = shows[0]['datetime']

        print_header (weekdays[day.weekday()], day.strftime('%d.%m.%Y'))
        for show in shows:
            print ("")
            print (show['datetime'].strftime('%H:%M'), show['title'], bcolors.OKBLUE)
            print (show['link'], bcolors.ENDC)
        print ("")
        print_delimiter()

