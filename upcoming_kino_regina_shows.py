#!/usr/bin/env python3
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from colors import bcolors
from formatting import *

from feed_parser import parseFeed

weekdays = {
    0: "Maanantai",
    1: "Tiistai",
    2: "Keskiviikko",
    3: "Torstai",
    4: "Perjantai",
    5: "Lauantai",
    6: "Sunnuntai"
}

printKinoReginaArt()

now = datetime.now().strftime('%d-%m-%Y')

post_params = urllib.parse.urlencode({'getShowtimesFrontpage': now}).encode("utf-8")
post_request = urllib.request.Request("https://kinoregina.fi/wp-content/themes/kinoregina/assets/functions/getShowtimesFrontpage.php", data=post_params)

contents = urllib.request.urlopen(post_request).read().decode('utf-8')

showsByDate = {}

shows = parseFeed(contents)

if shows:
    # Group by date
    for show in shows:
        date_str = show['datetime'].strftime('%d-%m-%Y')
        
        if not showsByDate.get(date_str): 
            showsByDate[date_str] = []
        
        showsByDate[date_str].append(show)

    # Print shows
    for _, shows in showsByDate.items():
        day = shows[0]['datetime']

        printHeader (weekdays[day.weekday()], day.strftime('%d.%m.%Y'))
        for show in shows:
            print ("")
            print (show['datetime'].strftime('%H:%M'), show['title'], bcolors.OKBLUE)
            print (show['link'], bcolors.ENDC)
        print ("")
        printDelimiter()
else:
    sys.exit("No shows found")