import unittest
from validators import Criminal

class Test_Criminal(unittest.TestCase):

  def test_check_criminal_returns_true_for_valid_candidate(self):
    self.assertEquals(Criminal().validate('555-55-5555'), True)

  def test_check_criminal_returns_false_and_reason_for_failed_candidate(self):
    self.assertEquals(Criminal().validate('111-11-1111'), (False, 'Break in.'))
