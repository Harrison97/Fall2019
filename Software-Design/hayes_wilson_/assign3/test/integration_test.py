import unittest
from agency import evaluate
from validators import *

class Test_Integration(unittest.TestCase):


  def test_agency_evaluate_with_criteria_returns_true_for_valid_candidate(self):
    exspected_response = {
        'valid': True
    }
    response = evaluate(Credit, Employment, Criminal, Citizenship, ss_num='555-55-5555')
    self.assertEquals(response, exspected_response)

  def test_agency_evaluate_with_criteria_returns_false_and_1_reason_for_invalid_candidate(self):
    exspected_response = {
        'valid': False,
        'reasons': ['Poor Credit.']
    }
    response = evaluate(Credit, Employment, Criminal, Citizenship, ss_num='155-55-5555')
    self.assertEquals(response, exspected_response)

  def test_agency_evaluate_with_criteria_returns_false_and_2_reason_for_invalid_candidate(self):
    exspected_response = {
        'valid': False,
        'reasons': ['Poor Credit.', 'Break in.' ]
    }
    response = evaluate(Credit, Employment, Criminal, Citizenship, ss_num='115-55-5555')
    self.assertEquals(response, exspected_response)

  def test_agency_evaluate_with_criteria_returns_false_and_3_reason_for_invalid_candidate(self):
    exspected_response = {
        'valid': False,
        'reasons': ['Poor Credit.', 'No Experience.', 'Break in.']
    }
    response = evaluate(Credit, Employment, Criminal, Citizenship, ss_num='111-55-5555')
    self.assertEquals(response, exspected_response)

  def test_agency_evaluate_with_criteria_returns_false_and_4_reason_for_invalid_candidate(self):
    exspected_response = {
        'valid': False,
        'reasons': ['Poor Credit.', 'No Experience.', 'Break in.', 'Not a citizen.']
    }
    response = evaluate(Credit, Employment, Criminal, Citizenship, ss_num='111-15-5555')
    self.assertEquals(response, exspected_response)

