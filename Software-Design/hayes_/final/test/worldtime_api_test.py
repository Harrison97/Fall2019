import unittest
import src.worldtime_api as api
from mock import patch

class Test_Worldtime_API(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_parse_data_returns_raw_offset_on_success(self):
    data = 'a: 1\nt: 3\nraw_offset: 12345\nzzzz: test'
    raw_offset = api.parse_data_for_raw_offset(data)
    self.assertEquals(raw_offset, 12345)

  def test_parse_data_returns_none_on_bad_content(self):
    content = 'a: 1\nt: 3\n'
    raw_offset = api.parse_data_for_raw_offset(content)
    self.assertEquals(raw_offset, None)

  @patch('requests.get')
  def test_fetch_city_data_raises_exception(self, m_get):

    m_get.return_value.status_code = 404
    self.assertRaises(Exception, api.fetch_city_data, 'London')

