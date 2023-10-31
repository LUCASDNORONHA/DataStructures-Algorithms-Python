import numpy as np

vertices2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
vertices2_inv = {0: 'A', 1: 'B', 2:'C', 3:'D', 4:'E', 5: 'F'}

arestas2 = np.zeros([len(vertices2), len(vertices2)], dtype=int)
arestas2[vertices2['A'],[vertices2['B']]] = 2
arestas2[vertices2['A'],[vertices2['C']]] = 1
arestas2[vertices2['B'],[vertices2['D']]] = 1
arestas2[vertices2['C'],[vertices2['D']]] = 3
arestas2[vertices2['C'],[vertices2['E']]] = 4
arestas2[vertices2['D'],[vertices2['F']]] = 2
arestas2[vertices2['E'],[vertices2['F']]] = 2

import sys
class Dijkstra:
  def __init__(self, vertices, arestas, inicio):
    self.tamanho = len(vertices)
    self.vertices = vertices
    self.grafo = arestas
    self.inicio = inicio

  def mostra_solucao(self, distancias):
    print('Menores distâncias de {} até todos os outros'.format(self.vertices[self.inicio]))
    for vertice in range(self.tamanho):
      print(self.vertices[vertice], distancias[vertice])

  def distancia_minima(self, distancia, visitados):
    minimo = sys.maxsize
    for vertice in range(self.tamanho):
      if distancia[vertice] < minimo and visitados[vertice] == False:
        minimo = distancia[vertice]
        indice_minimo = vertice
    return indice_minimo

  def dijkstra(self):
    distancia = [sys.maxsize] * self.tamanho
    distancia[self.inicio] = 0
    visitados = [False] * self.tamanho

    for _ in range(self.tamanho):
      indice_minimo = self.distancia_minima(distancia, visitados)
      visitados[indice_minimo] = True
      for vertice in range(self.tamanho):
        if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False \
            and distancia[vertice] > distancia[indice_minimo] + self.grafo[indice_minimo][vertice]:
          distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]

    self.mostra_solucao(distancia)

dijkstra = Dijkstra(vertices2_inv, arestas2, vertices2['A'])
dijkstra.dijkstra()