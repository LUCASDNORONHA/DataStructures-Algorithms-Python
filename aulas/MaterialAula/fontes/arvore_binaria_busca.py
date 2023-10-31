class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

  def mostra_no(self):
    print(self.valor)


class ArvoreBinariaBusca:
  def __init__(self):
    self.raiz = None
    self.ligacoes = []

  def inserir(self, valor):
    novo = No(valor)
    # Se a árvore estiver vazia
    if self.raiz == None:
      self.raiz = novo
    else:
      atual = self.raiz
      while True:
        pai = atual
        # Esquerda
        if valor < atual.valor:
          atual = atual.esquerda
          if atual == None:
            pai.esquerda = novo
            return
        # Direita
        else:
          atual = atual.direita
          if atual == None:
            pai.direita = novo
            return

  def pesquisar(self, valor):
    atual = self.raiz
    while atual.valor != valor:
      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita
      if atual == None:
        return None
    return atual

  # Raiz, esquerda, direita
  def pre_ordem(self, no):
    if no != None:
      print(no.valor)
      self.pre_ordem(no.esquerda)
      self.pre_ordem(no.direita)

  # Esquerda, raiz, direita
  def em_ordem(self, no):
    if no != None:
      self.em_ordem(no.esquerda)
      print(no.valor)
      self.em_ordem(no.direita)

  # Esquerda, direita, raiz
  def pos_ordem(self, no):
    if no != None:
      self.pos_ordem(no.esquerda)
      self.pos_ordem(no.direita)
      print(no.valor)

  def excluir(self, valor):
    if self.raiz == None:
      print('A árvore está vazia')
      return

    # Encontrar o nó
    atual = self.raiz
    pai = self.raiz
    e_esquerda = True
    while atual.valor != valor:
      pai = atual
      # Esquerda
      if valor < atual.valor:
        e_esquerda = True
        atual = atual.esquerda
      # Direita
      else:
        e_esquerda = False
        atual = atual.direita
      if atual == None:
        return False

    # O nó a ser apagado é uma folha
    if atual.esquerda == None and atual.direita == None:
      if atual == self.raiz:
        self.raiz = None
      elif e_esquerda == True:
        pai.esquerda = None
      else:
        pai.direita = None

    # O nó a ser apagado não possui filho na direita
    elif atual.direita == None:
      if atual == self.raiz:
        self.raiz = atual.esquerda
      elif e_esquerda == True:
        pai.esquerda = atual.esquerda
      else:
        pai.direita = atual.esquerda
    # O nó a ser apagado não possui filho na esquerda
    elif atual.esquerda == None:
      if atual == self.raiz:
        self.raiz = atual.direita
      elif e_esquerda == True:
        pai.esquerda = atual.direita
      else:
        pai.direita = atual.direita
    # O nó possui dois filhos
    else:
      sucessor = self.get_sucessor(atual)
      if atual == self.raiz:
        self.raiz = sucessor
      elif e_esquerda == True:
        pai.esquerda = sucessor
      else:
        pai.direita = sucessor
      sucessor.esquerda = atual.esquerda

    return True

  def get_sucessor(self, no):
    pai_sucessor = no
    sucessor = no
    atual = no.direita
    while atual != None:
      pai_sucessor = sucessor
      sucessor = atual
      atual = atual.esquerda
    if sucessor != no.direita:
      pai_sucessor.esquerda = sucessor.direita
      sucessor.direita = no.direita
    return sucessor

arvore = ArvoreBinariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

arvore.pesquisar(39)
arvore.pesquisar(84)
arvore.pesquisar(100)

arvore.excluir(9)
arvore.excluir(14)
arvore.excluir(72)