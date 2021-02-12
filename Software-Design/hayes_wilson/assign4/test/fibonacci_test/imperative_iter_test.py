import unittest
from fibonacci import imperative_iter

class Test_Imperative_Iter(unittest.TestCase):

  def test_imperative_iter(self):
    self.assertEqual(imperative_iter(0), 1)
    self.assertEqual(imperative_iter(-1), None)
    self.assertEqual(imperative_iter(7), 21)

