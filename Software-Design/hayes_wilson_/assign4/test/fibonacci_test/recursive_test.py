import unittest
from fibonacci import recursive

class Test_Recursive(unittest.TestCase):

  def test_recursive(self):
    self.assertEqual(recursive(0), 1)
    self.assertEqual(recursive(-1), None)
    self.assertEqual(recursive(7), 21)

