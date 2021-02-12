import unittest
from validators import Credit

class Test_Credit(unittest.TestCase):

  def test_check_credit_returns_true_for_valid_candidate(self):
    self.assertEquals(Credit().validate('555-55-5555'), True)

  def test_check_credit_returns_false_and_reason_for_failed_candidate(self):
    self.assertEquals(Credit().validate('111-11-1111'), (False, 'Poor Credit.'))
