# Projeto final - Estudo da rede de metro londrina
#
# Alunos:
# Ricardo E. Santo, nº 93357
# Rodrigo Sarroeira, nº 92761
#_______________________________________________________________________________________________________________________
from g12_structures import Station
from g12_structures import Connections


# Class Metro __________________________________________________________________________________________________________


class Metro:

    def __init__(self):
        self.graph = {}             # criar dicionário
        self._station = 0           # contador de estações
        self._connections = 0       # contador de conecções
        self.rawData = {}           # guarda informações sobre as stations
        self.graph1 = {}            # necessário para calcular o tempo ótimo

    def add_station(self, id_s, latitude, longitude, name, display_name, zone, total_lines, rail):
        if id_s not in self.graph.keys():
            station = Station(id_s, latitude, longitude, name, display_name, zone, total_lines, rail)
            self.graph[station.get_id()] = set([])

            self.rawData[station.get_id()] = station
                                            # adicionar a estação ao dicionário
            self._station = self._station + 1

        if id_s not in self.graph1.keys():
            station = Station(id_s, latitude, longitude, name, display_name, zone, total_lines, rail)
            self.graph1[station.get_id()] = set([])

    def add_connection(self, st1, st2, line=None, time=None):

        con = Connections(st1, st2, line, time)     # criar objeto do tipo Connections
        self.graph[st1].add(con)                    # adicionar à lista da estação 1
        self.graph1[st1].add(con)
        con = Connections(st2, st1, line, time)
        self.graph[st2].add(con)                    # adicionar à lista da estação 2
        self.graph1[st2].add(con)
        self._connections = self._connections + 1

# ______________________________________________________________________________________________________________________
