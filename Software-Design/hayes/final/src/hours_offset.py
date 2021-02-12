def get_hours_offset(fetch_data, parse_data, city, base_raw_offset):

  try:
    data = fetch_data(city)
  except Exception as err:
    return '{0:12}{1}'.format(city, 'ERR')

  raw_offset = parse_data(data)

  hours_offset = raw_offset/base_raw_offset if raw_offset != None else '---'

  return '{0:12}{1}'.format(city, hours_offset)

