def soma2(n):
  if n == 0:
    return 0

  return n + soma2(n - 1)

soma2(5)