# Find all element tags related to shows
# Useful for dodging malformed HTML elements in the full document

from typing import List
from datetime import datetime
import re

regexStr = r"""<div class="title-container d-md-flex aic fl">(?:\s*)<a href="(.+)"><span class="title">(.+)</span></a>(?:\s*)</div>(?:\s*)<div class="calendar-icon add-to-calendar cp pa addeventatc">(?:\s*)<i class="far fa-calendar-alt"></i>(?:\s*)<span class="start">(.+)</span>(?:\s*)<span class="timezone">Europe/Helsinki</span>(?:\s*)<span class="title">(?:.+)</span>(?:\s*)</div>(?:\s*)<a href="https://kauppa.kavi.fi/fi/events/pwdg/event_buybox/show/(\w+)" target="_blank" class="add-to-cart cp pa"><i class="fas fa-shopping-cart"></i></a>(?:\s*)"""

showRegex = re.compile(regexStr)

def _find_all_movie_elements(rawXml: str):
    return re.findall(showRegex, rawXml)

def _to_movie_dict(show: tuple) -> dict:
    return {
        'link': show[0],
        'title': show[1],
        'datetime': datetime.strptime(show[2], '%d-%m-%Y %H:%M'),
        'shopId': show[3]
    }

def parse(raw_xml: str) -> List[dict]:
    return map(_to_movie_dict, _find_all_movie_elements(raw_xml))
