import unittest
from validators import Employment

class Test_Employment(unittest.TestCase):

  def test_check_employment_returns_true_for_valid_candidate(self):
    self.assertEquals(Employment().validate('555-55-5555'), True)

  def test_check_employment_returns_false_and_reason_for_failed_candidate(self):
    self.assertEquals(Employment().validate('111-11-1111'), (False, 'No Experience.'))
