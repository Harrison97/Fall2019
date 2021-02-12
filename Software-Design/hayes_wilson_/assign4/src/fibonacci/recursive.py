def recursive(n):
  if n < 0:
    return None
  if 0 <= n <= 1:
    return 1
  return recursive(n-1) + recursive(n-2)

