import unittest
import src.hours_offset as ho
import src.worldtime_api as api

class Test_Integration(unittest.TestCase):

  def test_get_hours_offset_returns_city_and_hours_offset(self):
    base_offset = 3600
    city = 'London'

    offset = ho.get_hours_offset(api.fetch_city_data, api.parse_data_for_raw_offset, city, base_offset)
    self.assertEquals(offset, 'London      0.0')

