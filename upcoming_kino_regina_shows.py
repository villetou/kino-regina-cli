#!/usr/bin/env python
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from xml.etree import ElementTree
from colors import bcolors
from formatting import *

printKinoReginaArt()

now = datetime.now().strftime('%d-%m-%Y')

post_params = urllib.parse.urlencode({'getShowtimesFrontpage': now}).encode("utf-8")
post_request = urllib.request.Request("http://kinoregina.fi/wp-content/themes/kinoregina/assets/functions/getShowtimesFrontpage.php", data=post_params)

contents = urllib.request.urlopen(post_request).read().decode('utf-8')

# Fix incomplete result with proper opening and closing tags
patched_contents = '<?xml version="1.0"?><root>' + contents.strip() + '</div></root>'

root = ElementTree.fromstring(patched_contents)

weekdays = {
    0: "Maanantai",
    1: "Tiistai",
    2: "Keskiviikko",
    3: "Torstai",
    4: "Perjantai",
    5: "Lauantai",
    6: "Sunnuntai"
}

showsByDate = {}

if root:
    show_containers = root.findall('div/div[@class="event d-flex d-md-block pr col-12"]')
    for type_tag in show_containers:
        time_str = type_tag.findall('div/span[@class="start"]')[0].text
        time_obj = datetime.strptime(time_str, '%d-%m-%Y %H:%M')
        timezone = type_tag.findall('div/span[@class="timezone"]')[0].text
        title = type_tag.findall('div/a/span[@class="title"]')[0].text
        link = type_tag.findall('div/a')[0].attrib['href']
        date_str = time_obj.strftime('%d-%m-%Y')

        if not showsByDate.get(date_str): 
            showsByDate[date_str] = []
        
        # Group by date
        showsByDate[date_str].append({
            'title': title,
            'datetime': time_obj,
            'link': link
        })

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
