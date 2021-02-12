from worldtime_api import fetch_content, parse_content
from unixtime import fetch_unixtime

print(str(fetch_unixtime(fetch_content, parse_content)))

