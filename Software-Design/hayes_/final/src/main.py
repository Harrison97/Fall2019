import sys

from worldtime_api import fetch_city_data, parse_data_for_raw_offset
from hours_offset import get_hours_offset
from read_file import get_cities_from_file

GMT_RAW_OFFSET = 3600

if len(sys.argv) != 2:
  print('Error: Requires 2 Arguments\nExample: main.py <file>')
else:
  cities_file = sys.argv[1]

  cities = get_cities_from_file(cities_file)

  for city in cities:
    print(get_hours_offset(fetch_city_data, parse_data_for_raw_offset, city, GMT_RAW_OFFSET))
