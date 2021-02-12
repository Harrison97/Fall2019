import unittest

from src.game.game_of_life import *

class GameOfLifeTests(unittest.TestCase):
  
  def test_Canary(self):
    self.assertTrue(True)

  def test_dead_cell_stays_dead_with_number_of_live_neighbors_0(self):
    self.assertEqual(0,
      next_state(current_state = 0, number_of_live_neighbors = 0))        

  def test_dead_cell_stays_dead_with_number_of_live_neighbors_1(self):
    self.assertEqual(0,
      next_state(current_state = 0, number_of_live_neighbors = 1))        

  def test_dead_cell_stays_dead_with_number_of_live_neighbors_2(self):
    self.assertEqual(0,
      next_state(current_state = 0, number_of_live_neighbors = 2))        

  def test_dead_cell_stays_dead_with_number_of_live_neighbors_5(self):
    self.assertEqual(0,
      next_state(current_state = 0, number_of_live_neighbors = 5))        

  def test_dead_cell_stays_dead_with_number_of_live_neighbors_8(self):
    self.assertEqual(0,
      next_state(current_state = 0, number_of_live_neighbors = 8))        

  def test_dead_cell_comes_to_live_with_number_of_live_neighbors_3(self):
   self.assertEqual(1,
      next_state(current_state = 0, number_of_live_neighbors = 3))

  def test_live_cell_dies_with_number_of_live_neighbors_1(self):
    self.assertEqual(0,
        next_state(current_state = 0, number_of_live_neighbors = 1))

  def test_live_cell_dies_with_number_of_live_neighbors_4(self):
     self.assertEqual(0,
        next_state(current_state = 0, number_of_live_neighbors = 4))
     
  def test_live_cell_dies_with_number_of_live_neighbors_8(self):
     self.assertEqual(0,
        next_state(current_state = 0, number_of_live_neighbors = 8))
     
  def test_live_cell_stays_alive_with_number_of_live_neighbors_2(self):
     self.assertEqual(1,
        next_state(current_state = 1, number_of_live_neighbors = 2))

  def test_live_cell_stays_alive_with_number_of_live_neighbors_3(self):
     self.assertEqual(1,
        next_state(current_state = 1, number_of_live_neighbors = 3))

  def test_signal_live_cell_at_position_three_three(self):
    neighbors = {(2, 2): 0,(2, 3): 0,(2, 4): 0, (3, 2): 0, (3, 3): 1, (3, 4): 0,(4, 2): 0,(4, 3): 0,(4, 4): 0}
    spawn_here = {(3, 3): 1}
    self.assertEqual(neighbors, generateSignal(spawn_here))

  def test_signal_two_live_cells_at_position_two_two_three_three(self):
    spawn_dict = {(2, 2): 1, (3, 3): 1}
    neighbors_dict = {(1, 1): 0, (1, 2): 0, (1, 3): 0, (2, 1): 0, (2, 2): 1, (2, 3): 0, (2, 4): 0,  (3, 1): 0, (3, 2): 0, (3, 3): 1, (3, 4): 0,(4, 2): 0,(4, 3): 0,(4, 4): 0}
    self.assertEqual(neighbors_dict, generateSignal(spawn_dict))

  def test_return_neighbor_count_one(self):
    dict_cells = {(0, 0): 1, (1, 1): 1, (0, 1): 0}
    self.assertEqual(1, return_neighbor_count((1, 1), dict_cells))

  def test_return_live_cell_set(self):
    live_cells = set()
    live_cells = {(0, 0), (1, 1), (1, 2)}
    all_cells = {(0, 0): 1, (1, 1): 1, (0, 1): 0, (1, 2): 1}
    self.assertEqual(live_cells, return_live_cell_set(all_cells))

  def test_store_cells(self):
    set_of_initial_live_cells = { (0, 0), (0, 1), (1, 1), (1, 0)}
    dict_starting_cells = {(0, 0): 1, (0, 1): 1, (1, 1): 1, (1, 0): 1}
    self.assertEqual(dict_starting_cells, store_cells(set_of_initial_live_cells))

  def test_simulate_game_no_survivors(self):
    set_spawn = set()
    set_spawn ={(0, 0), (1, 1)}
    self.assertEqual(set(), simulateGame(set_spawn))

  def test_simulate_game_ocillator(self):
    set_spawn = set()
    next_gen = set()
    set_spawn ={(1, 0), (1, 1), (1, 2)}
    next_gen = {(0, 1), (1, 1), (2, 1)}
    self.assertEqual(next_gen, simulateGame(set_spawn))
    
  def test_game_of_life_simulation(self):
    set_spawn = set()
    next_gen = set()
    set_spawn ={(1, 0), (1, 1), (1, 2)}
    next_gen = simulateGame(set_spawn)
    self.assertEqual(set_spawn, simulateGame(next_gen))
    
if __name__ == '__main__': 
  unittest.main()
