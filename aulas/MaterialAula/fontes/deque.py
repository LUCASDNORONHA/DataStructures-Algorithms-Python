import numpy as np

class Deque:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Início estiver na primeira posição
        elif self.inicio == 0:
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print('O deque está cheio')
            return

        # Se estiver vazio
        if self.inicio == -1:
            self.inicio = 0
            self.final = 0
        # Final estiver na última posição
        elif self.final == self.capacidade - 1:
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        # Possui somente um elemento
        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        else:
            # Volta para a posição inicial
            if self.inicio == self.capacidade - 1:
                self.inicio = 0
            else:
                # Incrementar início para remover o início atual
                self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        if self.inicio == self.final:
            self.inicio = -1
            self.final = -1
        elif self.inicio == 0:
            self.final = self.capacidade - 1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print('O deque já está vazio')
            return

        return self.valores[self.inicio]

    def get_final(self):
        if self.__deque_vazio() or self.final < 0:
            print('O deque já está vazio')
            return

        return self.valores[self.final]

deque = Deque(5)
deque.insere_final(5)
deque.insere_final(10)
deque.insere_inicio(3)
deque.insere_inicio(2)
deque.insere_final(11)

deque.insere_inicio(43)

deque.excluir_inicio()
deque.excluir_final()
