class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        print(self.valor)

class ListaDuplamenteEncadeada:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp

    def excluir_final(self):
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def excluir_posicao(self, valor):
        atual = self.primeiro
        while atual.valor != valor:
            atual = atual.proximo
            if atual == None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo

        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def mostrar_frente(self):
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def mostrar_tras(self):
        atual = self.ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior

lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_final(3)
lista.insere_final(4)
lista.excluir_inicio()
lista.excluir_final()
lista.excluir_posicao(3)