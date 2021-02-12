import unittest
import src.hours_offset as ho

class Test_Hours_Offset(unittest.TestCase):

  def test_get_hours_offset_passes_city_to_parse_function(self):
    city = ''
    base_offset = 3600

    def fetch_data(c):
      nonlocal city
      city = c
      return 5

    parse_data = lambda data: 3

    ho.get_hours_offset(fetch_data, parse_data, 'London', base_offset)
    self.assertEquals(city, 'London')


  def test_get_hours_offset_returns_city_and_hours_offset_on_valid_data(self):
    city = 'London'
    base_offset = 3600

    def fetch_data(c):
      return 5

    parse_data = lambda data: 7200

    line = ho.get_hours_offset(fetch_data, parse_data, city, base_offset)
    self.assertEquals(line, 'London      2.0')

  def test_get_hours_offset_returns_city_and_err_on_bad_request(self):
    city = 'London'
    base_offset = 3600

    def fetch_data(c):
      raise Exception

    parse_data = lambda data: 7200

    line = ho.get_hours_offset(fetch_data, parse_data, city, base_offset)
    self.assertEquals(line, 'London      ERR')

  def test_get_hours_offset_returns_city_and_dashes_on_bad_content(self):
    city = 'London'
    base_offset = 3600

    def fetch_data(c):
      return 7

    parse_data = lambda data: None

    line = ho.get_hours_offset(fetch_data, parse_data, city, base_offset)
    self.assertEquals(line, 'London      ---')

  def test_get_hours_offset_handles_exeption(self):
    city = ''
    base_offset = 3600

    def fetch_data():
      raise Exception
    parse_data = lambda content: 1

    self.assertRaises(Exception, ho.get_hours_offset(fetch_data, parse_data, city, base_offset))

