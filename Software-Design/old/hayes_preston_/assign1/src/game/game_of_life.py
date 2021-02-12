from enum import Enum

class CellState(Enum):
  Dead = 0
  Alive = 1

def next_state(current_state, number_of_live_neighbors):
  if number_of_live_neighbors == 3:
    return CellState.Alive
  
  return CellState.Dead