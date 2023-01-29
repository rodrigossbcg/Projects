# Projeto final - Estudo da rede de metro londrina
#
# Alunos:
# Ricardo E. Santo, nº 93357
# Rodrigo Sarroeira, nº 92761
# ______________________________________________________________________________________________________________________
from g12_structures import Station
from g12_structures import Connections


class London_M:

    def __init__(self):
        self._graph = {}                # criar dicionário
        self._station = 0               # contador de estações
        self._connections = 0           # contador de conecções
        self.rawData = {}               # guarda informações sobre as stations

    def add_station(self, id_s, latitude, longitude, name, display_name, zone, total_lines, rail):
        if id_s not in self._graph.keys():
            station = Station(id_s, latitude, longitude, name, display_name, zone, total_lines, rail)

            self._graph[station.get_id()] = set([])
            self.rawData[station.get_id()] = station
            # adicionar a estação ao dicionário
            self._station = self._station + 1

    def add_connection(self, st1, st2, line=None, time=None):

        con = Connections(st1, st2, line, time)  # criar objeto do tipo Connections
        self._graph[st1].add(con)                # adicionar à lista da estação 1
        self._graph[st2].add(con)                # adicionar à lista da estação 2
        self._connections = self._connections + 1






