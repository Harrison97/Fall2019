import unittest
from fibonacci import memo

class Test_Memo(unittest.TestCase):

  def test_memo(self):
    self.assertEqual(memo(0), 1)
    self.assertEqual(memo(-1), None)
    self.assertEqual(memo(7), 21)
    self.assertEqual(memo(7), 21)

