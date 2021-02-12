def get_cities_from_file(filename):
  cities = []
  with open(filename, 'r') as f:
    for word in f:
      cities.append(word.replace('\n', ''))
  return cities

