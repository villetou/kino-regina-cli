#!/usr/bin/env python3
import sys
from datetime import datetime
from colors import bcolors
import feed_parser
import api
import helpers 
import formatting

if __name__ == '__main__':
    formatting.print_kino_regina_art()
    
    raw_feed = api.fetch_data()
    shows = feed_parser.parse(raw_feed)
    shows_by_date = helpers.group_shows_by_date(shows)
    
    formatting.print_shows(shows_by_date)
