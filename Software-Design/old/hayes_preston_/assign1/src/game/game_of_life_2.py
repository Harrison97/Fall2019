class Cell:
  __neighbors = 0

  def __repr__(self):
    return str(self.__neighbors)

  def reset_neighbors(self):
    self.__neighbors = 0

  def get_neighbor_count(self) -> int:
    return self.__neighbors

  def inc_neighbor(self):
    self.__neighbors += 1

  def decr_neighbor(self):
    self.__neighbors -= 1



class Universe:

  def __init__(self):
    self.console_view = 10
    self.reset() # initializes a clear universe

  def reset(self):
    self.__current_state = {
        'live_cells': {},
        'dead_neighbor_cells': {}
        }
    self.__next_state = {
        'live_cells': {},
        'dead_neighbor_cells': {}
        }

  def prepare_state(self):
    self.__next_state['live_cells'] = self.__current_state['live_cells'].copy()
    self.__next_state['dead_neighbor_cells'] = self.__current_state['dead_neighbor_cells'].copy()

  def print(self):
    for row in range(self.console_view):
      for col in range(self.console_view):
        if (row, col) in self.__current_state['live_cells']:
          print('*', end = ' ')
        else:
          print("'", end = ' ')
      print('')
    print(self.__current_state)

  def __create_cell_at(self, row, col):
    if (row, col) in self.__current_state['live_cells']:
      return
    neighbor_set = set({(row-1, col-1), (row, col-1), (row+1, col-1),
                        (row-1, col), (row+1, col),
                        (row-1, col+1), (row, col+1), (row+1, col+1)})
    if (row, col) in self.__current_state['dead_neighbor_cells']:
      self.__next_state['dead_neighbor_cells'].pop((row, col))
    if (row, col) not in self.__current_state['live_cells']:
      self.__next_state['live_cells'][row, col] = Cell()
      for neighbor in neighbor_set:
        n_row, n_col = neighbor
        if (n_row, n_col) not in self.__current_state['live_cells'] and \
           (n_row, n_col) not in self.__current_state['dead_neighbor_cells']:
          self.__next_state['dead_neighbor_cells'][n_row, n_col] = Cell()
        if neighbor in self.__current_state['dead_neighbor_cells']:
          self.__next_state['dead_neighbor_cells'][neighbor].inc_neighbor()
        elif neighbor in self.__current_state['live_cells']:
          self.__next_state['live_cells'][neighbor].inc_neighbor()

  def __delete_cell_at(self, row, col):
    if (row, col) not in self.__current_state['live_cells']:
      return
    neighbor_set = set({(row-1, col-1), (row, col-1), (row+1, col-1),
                        (row-1, col), (row+1, col),
                        (row-1, col+1), (row, col+1), (row+1, col+1)})
    if (row, col) in self.__current_state['live_cells']:
      pass
      self.__next_state['live_cells'].pop((row, col))
      for neighbor in neighbor_set:
        n_row, n_col = neighbor
        if neighbor in self.__next_state['live_cells']:
          pass
          self.__next_state['live_cells'][neighbor].decr_neighbor()
        elif neighbor in self.__next_state['dead_neighbor_cells']:
          pass
          self.__next_state['dead_neighbor_cells'][neighbor].decr_neighbor()

  def spawn_glider(self):
    self.reset()
    self.prepare_state()
    gilder = [[0,0], [1,1], [1,2], [2,0], [2, 1]]
    for location in gilder:
      row, col = location
      self.__create_cell_at(row, col)
    self.__current_state = self.__next_state.copy()
    self.__next_state = {
        'live_cells': {},
        'dead_neighbor_cells': {}
        }

  def next_generation(self):
    self.prepare_state()
    for location, cell in self.__current_state['live_cells'].items():
      row, col = location
      if not 2 <= cell.get_neighbor_count() <= 3:
        pass
        #kill cell, which will decr neighbors' neighbors
        self.__delete_cell_at(row, col)
    for location, cell in self.__current_state['dead_neighbor_cells'].items():
      if cell.get_neighbor_count() == 3:
        pass
        #rev dead cell, which will inc neighbors' neighbors
        #self.__create_cell_at(row, col)
    self.__current_state = self.__next_state
    self.__next_state = {
        'live_cells': {},
        'dead_neighbor_cells': {}
        }

