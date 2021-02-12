import unittest
import src.read_file as rf

class Test_Read_File(unittest.TestCase):

  def test_get_cities_from_file(self):
    cities = rf.get_cities_from_file('src/cities.txt')
    self.assertEquals(cities,['London', 'Riga', 'Amsterda',
      'Minsk', 'Brussels', 'Kiev.txt', 'Warsaw', 'Krakow'])

