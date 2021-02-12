from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import requests
import json
import logging

tf = TimezoneFinder()
logging.basicConfig(format='%(levelname)s : %(message)s')

def timestamp_to_UTC(time):
  return datetime.utcfromtimestamp(time)

def coord_to_timezone(lat, lon):
  return tf.timezone_at(lng=lon, lat=lat)

def timestamp_to_time_at_latlon(time, lat, lon):
  zone = str(coord_to_timezone(lat, lon))
  time_obj = timestamp_to_UTC(time)
  utc = time_obj.replace(tzinfo=pytz.timezone('UTC'))
  adjusted_time = utc.astimezone(pytz.timezone(zone))
  return adjusted_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

def compute_flyover_time(lat, lon, iss_flyover_data):
  try:
    data = iss_flyover_data(lat, lon)
    return data['response'][0]['risetime']
  except Exception as e:
    logging.error(e)

