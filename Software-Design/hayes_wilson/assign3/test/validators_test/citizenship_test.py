import unittest
from validators import Citizenship

class Test_Citizenship(unittest.TestCase):

  def test_check_citizenship_returns_true_for_valid_candidate(self):
    self.assertEquals(Citizenship().validate('555-55-5555'), True)

  def test_check_citizenship_returns_false_and_reason_for_failed_candidate(self):
    self.assertEquals(Citizenship().validate('111-11-1111'), (False, 'Not a citizen.'))
