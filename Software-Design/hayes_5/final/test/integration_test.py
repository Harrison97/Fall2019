import unittest
import src.worldtime_api as api
import src.unixtime as ut

class Test_Integration(unittest.TestCase):

  def test_fetch_unixtime_returns_unixtime(self):
    unixtime = ut.fetch_unixtime(api.fetch_content, api.parse_content)
    prefix = 'Unix time is '
    self.assertEquals(unixtime[:13], prefix)
    self.assertGreater(int(unixtime[13:]), 1574284022)

