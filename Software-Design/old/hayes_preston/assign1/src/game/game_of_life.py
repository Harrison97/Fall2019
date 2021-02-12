from enum import Enum

class CellState(Enum):
  Dead = 0
  Alive = 1

def next_state(current_state, number_of_live_neighbors):    #determines next state and returns 1 if alive or 0 if dead
  return 1 if (number_of_live_neighbors == 3
    or (current_state == 1 and number_of_live_neighbors == 2)) else (0)

def generateSignal(position_dict)->dict:  #takes a dictionary of live cells as a parameter and returns a dictionary of the neighbors and the live cells
  signals_dict = {}
  update_dict = {}
  signals_dict = position_dict.copy()
  for key in position_dict:
    x, y = key
    for i in range(x - 1, x + 2):
      for j in range (y - 1, y + 2):
        if(i != x or j != y)and (i, j) not in position_dict:
          signals_dict.update({(i, j): 0})
  return signals_dict

def return_neighbor_count(coord, signal_set): #takes a coordinate and signal dictionary parameter, returns the number of neighbors each key has
  count = 0
  x, y = coord
  for i in range(x - 1, x + 2):
    for j in range (y - 1, y + 2):
      if(i != x or j != y):
        if((i, j) in signal_set and signal_set[(i, j)] == 1):
          count += 1
  return count
            
def return_live_cell_set(dict_of_both_cells) ->set: #takes a dictionary of both live and dead cells as parameter, returns a set of only live cells
  remaining_live_cells = set()
  for key in dict_of_both_cells:
    if(dict_of_both_cells[key] == 1):
      remaining_live_cells.add(key)
  return set(remaining_live_cells)

def store_cells(set_of_cells)->dict:  #takes a set of intial live cells as a parameter, returns a dictionary with the coord as the key, and it state as value
  dict_of_cells = {}
  for coord in set_of_cells:
    dict_of_cells[coord] = 1
  return dict_of_cells

def simulateGame(set_of_live_cells) ->set:
  update_set = {}
  live_cell_dict = store_cells(set_of_live_cells)
  live_and_neighboring_cell_dict = generateSignal(live_cell_dict)
  update_set = dict(live_and_neighboring_cell_dict)
  for key in live_and_neighboring_cell_dict:
    update_set[key] = next_state(live_and_neighboring_cell_dict[key], return_neighbor_count(key, live_and_neighboring_cell_dict))
  live_and_neighboring_cell_dict = update_set
  update_set = return_live_cell_set(live_and_neighboring_cell_dict)
  return update_set

def GameOfLife(starting_cells):
  #implement gui
  pass
