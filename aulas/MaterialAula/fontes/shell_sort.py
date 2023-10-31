import numpy as np

def shell_sort(vetor):
    intervalo = len(vetor) // 2

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2

    return vetor

shell_sort(np.array([8, 5, 1, 4, 2, 3]))