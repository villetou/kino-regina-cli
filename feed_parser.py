# Find all element tags related to shows
# Useful for dodging malformed HTML elements in the full document

from typing import List
from datetime import datetime
import re

regexStr = r"""<div class="title-container d-md-flex aic fl">(?:\s*)<a href="(.+)"><span class="title">(.+)</span></a>(?:\s*)</div>(?:\s*)<div class="calendar-icon add-to-calendar cp pa addeventatc">(?:\s*)<i class="far fa-calendar-alt"></i>(?:\s*)<span class="start">(.+)</span>(?:\s*)<span class="timezone">Europe/Helsinki</span>(?:\s*)<span class="title">(?:.+)</span>(?:\s*)</div>(?:\s*)<a href="https://kauppa.kavi.fi/fi/events/pwdg/event_buybox/show/(\w+)" target="_blank" class="add-to-cart cp pa"><i class="fas fa-shopping-cart"></i></a>(?:\s*)"""

showRegex = re.compile(regexStr)

def _findAllMovieElements(rawXml: str):
    return re.findall(showRegex, rawXml)

def _toMovieDict(show: tuple) -> dict:
    return {
        'link': show[0],
        'title': show[1],
        'datetime': datetime.strptime(show[2], '%d-%m-%Y %H:%M'),
        'shopId': show[3]
    }

def parseFeed(rawXml: str) -> List[dict]:
    return map(_toMovieDict, _findAllMovieElements(rawXml))
