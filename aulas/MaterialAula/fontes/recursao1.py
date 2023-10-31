def recursao(i):
  print('Recursão')
  i += 1
  if i == 5:
    return
  else:
    recursao(i)

recursao(0)