import unittest
from fibonacci import functional_iter

class Test_Functional_Iter(unittest.TestCase):

  def test_functional_iter(self):
    self.assertEqual(functional_iter(0), 1)
    self.assertEqual(functional_iter(-1), None)
    self.assertEqual(functional_iter(7), 21)

