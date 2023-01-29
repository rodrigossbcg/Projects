# Projeto final - Estudo da rede de metro londrina
#
# Alunos:
# Ricardo E. Santo, nº 93357
# Rodrigo Sarroeira, nº 92761

from g12_metro_fase1 import London_M
import csv
import numpy as np


# ______________________________________________________________________________________________________________________

class Metro(London_M):

    def __init__(self):
        London_M.__init__(self)
        self._a_matrix = None
# ______________________________________________________________________________________________________________________

    def read_stations(self):
        return self._read_stations()

    @staticmethod
    def _read_stations():  # ler o ficheiro do tipo csv relativo às estações
        info = []
        with open('london.stations.txt') as stations1:
            stations2 = csv.DictReader(stations1)
            for line in stations2:
                info.append((int(line["id"]), float(line["latitude"]), float(line["longitude"]), line["name"],
                             line["display_name"], float(line["zone"]), int(line["total_lines"]), int(line["rail"])))
        return info

    def create_stations(self):
        sts = self.read_stations()
        for i in sts:
            self.add_station(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])

# ______________________________________________________________________________________________________________________

    def read_connections(self):
        return self._read_connections()

    @staticmethod
    def _read_connections():                    # ler o ficheiro do tipo csv relativo às conexões
        info = []
        with open('london.connections.txt') as connections1:
            connections2 = csv.DictReader(connections1)
            for line in connections2:
                info.append((int(line["station1"]), int(line["station2"]), int(line["line"]), float(line["time"])))
        return info

    def _uniques_connections(self):
        con = self.read_connections()
        uniques = set([])
        for i in con:
            uniques.add((i[0], i[1]))
        return list(uniques)

    def create_connections(self):
        con = self._uniques_connections()
        for i in con:
            self.add_connection(i[0], i[1])
# ______________________________________________________________________________________________________________________

    def adjacency(self):                       # criar matriz de adjacencias
        stations = self._read_stations()
        self._a_matrix = np.zeros([len(stations), len(stations)])
        for i in self._uniques_connections():
            j = 0
            while i[0] != stations[j][0]:      # enquanto não encontrar o primeiro vértice
                j = j + 1
            w = 0
            while i[1] != stations[w][0]:      # esquanto não encontrar o segundo vértice
                w = w + 1
            self._a_matrix[j, w] = 1
            self._a_matrix[w, j] = 1
        return self._a_matrix

    def degree(self, adjacency):                       # matriz diagonal que guarda o grau de ligação de cada vertice
        degree = np.diag(adjacency.sum(axis=1))
        return degree

    @staticmethod
    def laplacian(degree, adjacency):                 # matriz de laplace ( L = D - A ), ligações (-1), grau (degree)
        return degree - adjacency

    @staticmethod
    def eigenvalues_eigenvectors(l):
        values, vectors = np.linalg.eig(l)
        return values, vectors

    def cuts(self, g1, g2):                         # elaborar as arestas de corte entre grafos g1 e g2
        arestas = []
        for i in g1:                                # vetor com os nós do grafo negativo
            arestas_gi = self._graph[i]             # lista com as arestas de g1[i]
            for j in g2:                            # percorrer os valores de g2 (vértices do outro cluster)
                for w in arestas_gi:                # percorrer as ligações de g1[i]
                    st1_2 = w.get_st1_st2()
                    st1 = st1_2[0]                  # estação inicial (id)
                    st2 = st1_2[1]                  # estação final (id)
                    if j == st1 or j == st2:        # ver se g2[j] pertence a alguma das ligações de g1[i]
                        arestas.append((st1, st2))  # lista com tuplo ( vertice de g1 , vertice de g2 )
        return arestas
