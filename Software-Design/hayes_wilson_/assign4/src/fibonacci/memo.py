from .recursive import *
m = {}

def memo(n):
  if n in m:
    return m[n]
  else:
    m[n] = recursive(n)
    return m[n]

