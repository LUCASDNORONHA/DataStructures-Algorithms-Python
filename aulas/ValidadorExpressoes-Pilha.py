import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        # Array de caracteres
        self.valores = np.empty(self.capacidade, dtype=str)

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def pilha_vazia(self):
        return self.topo == -1

    def empilhar(self, valor):
        if self.pilha_cheia():
            print('A pilha está cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print('A pilha está vazia')
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1


# Função para verificar a validade das expressões
def verifica_expressao(expressao):
    pilha = Pilha(len(expressao))

    for caractere in expressao:
        if caractere in '([{':
            pilha.empilhar(caractere)
        elif caractere in ')]}':
            if pilha.pilha_vazia():
                return False
            topo = pilha.desempilhar()
            if (caractere == ')' and topo != '(') or \
                    (caractere == ']' and topo != '[') or \
                    (caractere == '}' and topo != '{'):
                return False

    return pilha.pilha_vazia()


# Expressões de teste
expressoes = [
    "c[d]",
    "a{b[c]d}e",
    "a{b(c]d}e",
    "a[b{c}d]e}",
    "a{b(c)",
]

for expressao in expressoes:
    if verifica_expressao(expressao):
        print(f'A expressão "{expressao}" está balanceada.')
    else:
        print(f'A expressão "{expressao}" não está balanceada.')