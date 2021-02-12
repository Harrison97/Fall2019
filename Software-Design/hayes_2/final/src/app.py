from random import random, shuffle
import requests

ENDPOINT_URL = 'http://agile.cs.uh.edu/spell?'

def pick_word_from_file(filename):
  num_lines = sum(1 for line in open(filename))
  r = int(random()*num_lines)
  line = 0
  with open(filename, 'r') as f:
    for word in f:
      if line == r:
        return word.replace('\n', '')
      line += 1

def scramble_word(word):
  word_list = list(word)
  shuffle(word_list)
  return ''.join(word_list)

def check_word(word):
  pass
