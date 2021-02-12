import unittest
from timeit import timeit

class Test_Fibonacci(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_memo_is_faster_than_recursive(self):
    recursive_test_5 = timeit('recursive(5)', setup='from fibonacci import recursive', number=3)
    recursive_test_12 = timeit('recursive(12)', setup='from fibonacci import recursive', number=3)
    recursive_test_30 = timeit('recursive(30)', setup='from fibonacci import recursive', number=3)

    memo_test_5 = timeit('memo(5)', setup='from fibonacci import memo', number=3)
    memo_test_12 = timeit('memo(12)', setup='from fibonacci import memo', number=3)
    memo_test_30 = timeit('memo(30)', setup='from fibonacci import memo', number=3)

    test_5 = recursive_test_5 > memo_test_5
    test_12 = recursive_test_12 > memo_test_12
    test_30 = recursive_test_30 > memo_test_30

    self.assertTrue(test_5)
    self.assertTrue(test_12)
    self.assertTrue(test_30)

if __name__ == '__main__':

    unittest.main()
