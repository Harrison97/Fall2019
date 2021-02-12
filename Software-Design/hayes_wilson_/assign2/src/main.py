import sys
import satellite as sat
import satellite_api as api

if len(sys.argv) != 3:
  print('Error: Requires 2 Arguments\nExample: main.py <lat> <lon>')
else:
  lat = sys.argv[1]
  lon = sys.argv[2]
  print(sat.compute_time_of_flyover(float(lat), float(lon),\
    api.fetch_iss_flyover_data, api.get_data_from_url, api.parse_json_data))
