from datetime import datetime
import urllib.parse
import urllib.request

def fetch_data():
    now = datetime.now().strftime('%d-%m-%Y')
    post_params = urllib.parse.urlencode({'getShowtimesFrontpage': now}).encode("utf-8")
    post_request = urllib.request.Request("http://kinoregina.fi/wp-content/themes/kinoregina/assets/functions/getShowtimesFrontpage.php", data=post_params)
    return urllib.request.urlopen(post_request).read().decode('utf-8')

