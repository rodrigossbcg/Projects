# Projeto final - Estudo da rede de metro londrina
#
# Alunos:
# Ricardo E. Santo, nº 93357
# Rodrigo Sarroeira, nº 92761
#_______________________________________________________________________________________________________________________
import csv
from g12_metro_fase2 import Metro


# Class London Metro ___________________________________________________________________________________________________


class London_Metro(Metro):

    def __init__(self):
        Metro.__init__(self)

# Create Stations ______________________________________________________________________________________________________

    def read_stations(self):
        return self._read_stations()

    @staticmethod
    def _read_stations():
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

# Create Connections ___________________________________________________________________________________________________

    def read_connections(self):
        return self._read_connections()

    @staticmethod
    def _read_connections():
        info = []
        with open('Interstation v3.csv') as connections1:
            connections2 = csv.reader(connections1)
            i = 0
            for line in connections2:
                if i != 0:
                    info.append((int(line[0]), int(line[1]), int(line[2]), float(line[3]), float(line[4]),
                                 float(line[5]), float(line[6])))
                i = i + 1
        return info

    def create_connections(self):
        st1_st2 = []
        uniques = set([])
        con = self.read_connections()
        for i in con:
            st1_st2.append((i[1], i[2]))
        for i in con:
            if (i[1], i[2]) not in uniques:
                self.add_connection(i[1], i[2], i[0], (i[4], i[5], i[6]))
            else:
                edge_modified = self.find_edge(i[1], i[2])
                edge_modified._line.add(i[0])
                edge_modified._time.append((i[4], i[5], i[6]))

            uniques.add((i[1], i[2]))
            uniques.add((i[2], i[1]))
        for i in con:
            edge_modified = self.find_edge(i[1], i[2])
            edge_modified.get_time_average()

# Dijkstra Algorithm ___________________________________________________________________________________________________

    def dijkstra(self, start, end, n):

        if start == end:
            raise  ValueError("A estação de destino igual a estação de partida!")

        shortest_dist = {}           # guardar todas as distancias minimas desde start até ao nó
        track_prodecessor = {}       # guarda o caminho até ao nó atual
        unvisited = self.graph       # guarda os não visitados
        infinity = float("inf")      # número muito grande
        path = []                    # caminho ótimo
        prev_con = None

        # dizer que a distancia de start até qualquer outro nó é infinito, porque não foram visitados
        for node in unvisited:
            shortest_dist[node] = infinity
        shortest_dist[start] = 0

        while unvisited:

            current = None

            for node in unvisited:
                if current is None:
                    current = node
                elif shortest_dist[node] < shortest_dist[current]:
                    current = node

            con_options = self.graph[current]  # Guardar todas as conexões do nó atual

            for con in con_options:

                change_line = False

                if prev_con is not None and prev_con.get_line() != con.get_line():
                    change_line = True

                if con.get_time()[0][n] + shortest_dist[current] + change_line * 10 < shortest_dist[con.opposite(current)]:
                    shortest_dist[con.opposite(current)] = con.get_time()[0][n] + shortest_dist[current]
                    track_prodecessor[con.opposite(current)] = current
                    prev_con = con

            unvisited.pop(current)

        current = end

        while current != start:
            try:
                path.insert(0, current)
                current = track_prodecessor[current]
            except KeyError:
                print("The path is not reachable")
                break
        path.insert(0, start)

        if shortest_dist[end] < infinity:
            return path

# Optimal time _________________________________________________________________________________________________________

    def find_edge(self, start, end):
        return self._find_edge(start, end)

    def _find_edge(self, start, end):
        connections = self.graph1[start]
        for con in connections:
            if end == con.get_start() or end == con.get_end():
                return con

    def get_list(self, l):
        return self._get_list(l)

    @staticmethod
    def _get_list(l):
        route = l
        tuples = []
        i = 0
        while i != len(route) - 1:
            tuples.append((route[i], route[i + 1]))
            i = i + 1
        return tuples

    def get_travel_time(self, optimal_path, n):

        travel_time = 0
        optimal_path = self._get_list(optimal_path)
        for i in optimal_path:
            con = self.find_edge(i[0], i[1])
            travel_time = travel_time + con.get_time()[0][n]
        return travel_time

    def get_change_time(self, l):

        change_time = 0
        path = self._get_list(l)
        prev_path = self.find_edge(path[0][0], path[0][1])
        for i in path:
            path = self.find_edge(i[0], i[1])
            if path.get_line() != prev_path.get_line():
                change_time = change_time + 10
            prev_path = path
        return change_time

# ______________________________________________________________________________________________________________________
