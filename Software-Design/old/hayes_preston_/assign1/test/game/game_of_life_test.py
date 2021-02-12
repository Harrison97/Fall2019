import unittest
import sys
sys.path.insert(0, 'src/game')

from game_of_life import GameOfLife

class GameOfLifeTests(unittest.TestCase):
  tester = GameOfLife()
  
  def test_spawn_glider(self):
    self.tester.spawn_glider()
    self.assertTrue(True)
    
  def test_next_generation(self):
    self.tester.next_generation()
    self.assertTrue(True)
        
  def test_Canary(self):
    self.assertTrue(True)

if __name__ == '__main__': 
  unittest.main()
