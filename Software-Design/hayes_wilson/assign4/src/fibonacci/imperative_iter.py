def imperative_iter(n):
  if n < 0:
    return None
  if 0 <= n <= 1:
    return 1
  n_1 = 1
  n_2 = 1
  for i in range(2, n):
    temp = n_1 + n_2
    n_2 = n_1
    n_1 = temp
  return n_1 + n_2

