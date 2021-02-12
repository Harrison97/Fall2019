import unittest
from agency import evaluate

class Test_Agency(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_agency_evaluate_gets_passed_1_criteria_and_fails(self):
    class Test_criteria_1:
      def validate(self, ss_num):
        return (False, 'This is a Test.')
    exspected_response = {
        'valid': False,
        'reasons': ['This is a Test.']
    }
    response = evaluate(Test_criteria_1, ss_num='Fake Social')
    self.assertEquals(response, exspected_response)

  def test_agency_evaluate_gets_passed_multiple_criteria_and_fails(self):
    class Test_criteria_1:
      def validate(self, ss_num):
        return (False, 'This is a Test 1.')
    class Test_criteria_2:
      def validate(self, ss_num):
        return (False, 'This is a Test 2.')
    exspected_response = {
        'valid': False,
        'reasons': ['This is a Test 1.', 'This is a Test 2.']
    }
    response = evaluate(Test_criteria_1, Test_criteria_2, ss_num='Fake Social')
    self.assertEquals(response, exspected_response)

  def test_agency_evaluate_gets_passed_multiple_criteria_and_passes(self):
    class Test_criteria_1:
      def validate(self, ss_num):
        return True
    class Test_criteria_2:
      def validate(self, ss_num):
        return True
    exspected_response = {
        'valid': True
    }
    response = evaluate(Test_criteria_1, Test_criteria_2, ss_num='Fake Social')
    self.assertEquals(response, exspected_response)

