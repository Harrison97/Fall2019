import requests

url = 'http://worldtimeapi.org/api/ip.txt'

def fetch_content():
  r = requests.get(url)

  if r.status_code == 404:
    raise Exception('Error 404')

  return r.__dict__['_content'].decode('utf-8')

def parse_content(content):

  line_array = content.split('\n')

  for line in line_array:
    split = line.split(':')
    key = split[0]
    if key == 'unixtime':
      return split[1][1:]

  return 'not found'

