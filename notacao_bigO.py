# Notação Big-O

# Objetivo:
# Calcular a soma dos primeiros n números inteiros positivos, onde n é um número inteiro positivo.
# A partir de 1 até um valor específico, representado por n.

import timeit

# Função soma de n números consecutivos utilizando o laço for.

# Executa 11 passos ao passar o valor 10 e 1001 passos se eu passar o valor 1000.
# Podemos considerar o bigO desta função como O(n).
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

# Imprimindo o valor da função soma1.
print("Resultado da primeira função de soma:", soma1(10))

# Medindo o tempo de execução da função soma1.
timeit_result_funcao1 = timeit.timeit("soma1(10)", globals=globals(), number=100000)
print(f"Tempo médio de execução da função soma1: {timeit_result_funcao1:.6f} segundos")

# Função soma de n números consecutivos utilizando a fórmula de Gauss.

# Executa 3 passos independente do valor de n.
# Podemos considerar o bigO desta função O(3)
def soma2(n):
    return (n * (n + 1)) / 2

# Imprimindo o valor da função soma2.
print("Resultado da segunda função de soma:", soma2(10))

# Medindo o tempo de execução da função soma2.
timeit_result_funcao2 = timeit.timeit('soma2(10)', globals=globals(), number=100000)
print(f"Tempo médio de execução da função soma2: {timeit_result_funcao2:.6f} segundos")