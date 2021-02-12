import requests

URL_ENDPOINT = 'http://worldtimeapi.org/api/timezone/Europe/%s.txt'

def fetch_city_data(city):
  r = requests.get(URL_ENDPOINT % city)

  if r.status_code == 404:
    raise Exception('Error 404')

  return r.__dict__['_content'].decode('utf-8')

def parse_data_for_raw_offset(content):

  line_array = content.split('\n')

  for line in line_array:
    split = line.split(':')
    key = split[0]
    if key == 'raw_offset':
      return int(split[1][1:]) if split[1][1:] else None

