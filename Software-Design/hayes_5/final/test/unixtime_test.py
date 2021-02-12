import unittest
import src.unixtime as ut

class Test_Unixtime(unittest.TestCase):

  def test_fetch_unixtime_passes_content_to_parse_content(self):
    content = ''
    def parse_content(c):
      nonlocal content
      content = c
      return c

    fetch_content = lambda: '1111'

    ut.fetch_unixtime(fetch_content, parse_content)
    self.assertEquals(content, '1111')

  def test_fetch_unixtime_raises_exeption(self):

    def fetch_content():
      raise Exception
    parse_content = lambda content: 1

    self.assertRaises(Exception, ut.fetch_unixtime(fetch_content, parse_content))

