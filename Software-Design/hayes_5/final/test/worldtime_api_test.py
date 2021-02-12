import unittest
import src.worldtime_api as api
from mock import patch
import requests

class Test_Worldtime_API(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_parse_content_returns_unixtime_on_success(self):
    content = 'a: 1\nt: 3\nunixtime: 12345\nzzzz: test'
    unixtime = api.parse_content(content)
    self.assertEquals(unixtime, '12345')

  def test_parse_content_returns_unixtime_not_found_when_not_on_page(self):
    content = 'a: 1\nt: 3\n'
    unixtime = api.parse_content(content)
    self.assertEquals(unixtime, 'not found')



  @patch('requests.get')
  def test_fetch_unixtime_handles_exceptions(self, m_get):
    parse_content = lambda content: 2
    m_get.return_value.status_code = 404

    def fetch_unixtime(fetch_content, parse_content):
      try:
        fetch_content()
      except Exception as err:
        return err

    self.assertEquals(str(fetch_unixtime(api.fetch_content, parse_content)), 'Error 404')

