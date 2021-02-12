import requests

API_ENDPOINT = 'http://api.open-notify.org/iss-pass.json?&n=1'

def get_data_from_url(parameters):
  response = requests.get(API_ENDPOINT, params=parameters)

  if response.status_code == 404:
    raise Exception('404 Error')

  return response.json()

def parse_json_data(data):
  if data['message'] == 'success':
    return data['response'][0]['risetime']
  else:
    return data['reason']

def fetch_iss_flyover_data(lat, lon, get_data_from_url, parse_json_data):
  parameters = {
    'lat': lat,
    'lon': lon
  }

  try:
    data = get_data_from_url(parameters)
  except Exception as e:
    return e
  return parse_json_data(data)

