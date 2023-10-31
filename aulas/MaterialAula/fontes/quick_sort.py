import numpy as np
def particao(vetor, inicio, final):
  pivo = vetor[final]
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]
  vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
  return i + 1

def quick_sort(vetor, inicio, final):
  if inicio < final:
    posicao = particao(vetor, inicio, final)
    # Esquerda
    quick_sort(vetor, inicio, posicao - 1)
    # Direito
    quick_sort(vetor, posicao + 1, final)
  return vetor

vetor = np.array([38, 27, 43, 3, 9, 82, 10])
quick_sort(vetor, 0, len(vetor) - 1)