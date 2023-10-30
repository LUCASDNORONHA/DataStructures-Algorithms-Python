class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = [None] * self.capacidade

    def esta_cheia(self):
        return self.topo == self.capacidade - 1

    def esta_vazia(self):
        return self.topo == -1

    def empilhar(self, valor):
        if self.esta_cheia():
            print('A pilha está cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.esta_vazia():
            print('A pilha está vazia')
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def ver_topo(self):
        return self.valores[self.topo] if not self.esta_vazia() else -1

def verifica_expressao(expressao):
    pilha = Pilha(len(expressao))
    pares = {'(': ')', '[': ']', '{': '}'}

    for caractere in expressao:
        if caractere in pares.keys():
            pilha.empilhar(caractere)
        elif caractere in pares.values():
            if pilha.esta_vazia() or pares[pilha.ver_topo()] != caractere:
                return False
            pilha.desempilhar()

    return pilha.esta_vazia()

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