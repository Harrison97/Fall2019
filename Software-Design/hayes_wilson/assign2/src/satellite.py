from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder
import json

tf = TimezoneFinder()

def timestamp_to_UTC(time):
  return datetime.utcfromtimestamp(time)

def coord_to_timezone(lat, lon):
  return tf.timezone_at(lng=lon, lat=lat)

def timestamp_to_time_at_latlon(time, lat, lon):
  if type(time) != int:
    raise Exception(time)
  zone = str(coord_to_timezone(lat, lon))
  time_obj = timestamp_to_UTC(time)
  utc = time_obj.replace(tzinfo=pytz.timezone('UTC'))
  adjusted_time = utc.astimezone(pytz.timezone(zone))
  return adjusted_time.strftime('%l:%M%p')

def compute_time_of_flyover(lat, lon, iss_flyover_time, get_data, parse_data):
  try:
    return timestamp_to_time_at_latlon(iss_flyover_time(lat, lon, get_data, parse_data), lat, lon)
  except Exception as e:
    return e if str(e) != "'None'" else None

