import numpy as np

class Pilha:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.topo = -1
    # Array de chars (b'(')
    self.valores = np.chararray(self.capacidade, unicode=True)

  def __pilha_cheia(self):
    if self.topo == self.capacidade - 1:
      return True
    else:
      return False

  # Método público
  def pilha_vazia(self):
    if self.topo == -1:
      return True
    else:
      return False

  def empilhar(self, valor):
    if self.__pilha_cheia():
      print('A pilha está cheia')
    else:
      self.topo += 1
      self.valores[self.topo] = valor

  # Retorna o elemento desempilhado
  def desempilhar(self):
    if self.pilha_vazia():
      print('A pilha está vazia')
      return -1
    else:
      valor = self.valores[self.topo]
      self.topo -= 1
      return valor

  def ver_topo(self):
    if self.topo != -1:
      return self.valores[self.topo]
    else:
      return -1

# c[d]
# a{b[c]d}e
# a{b(c]d}e
# a[b{c}d]e}
# a{b(c)

expressao = str(input('Digite uma expressão: '))
pilha = Pilha(len(expressao))

for i in range(len(expressao)):
  ch = expressao[i]
  if ch == '{' or ch == '[' or ch == '(':
    pilha.empilhar(ch)
  elif ch == '}' or ch == ']' or ch == ')':
    if not pilha.pilha_vazia():
      chx = str(pilha.desempilhar())
      if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
        print('Erro: ', ch, ' na posição ', i)
        break
    else:
        print('Erro: ', ch, ' na posição ', i)
if not pilha.pilha_vazia():
    print('Erro!')