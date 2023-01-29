# Projeto final - Estudo da rede de metro londrina
#
# Curso de Licenciatura em Ciência dos Dados
#
# Estruturas de Dados e Algoritmos
#
# Docente:
# Ana Maria Almeida
#
# Alunos:
# Ricardo E. Santo, nº 93357
# Rodrigo Sarroeira, nº 92761
#
# Class Station ________________________________________________________________________________________________________


class Station:

    def __init__(self, id_s, latitude, longitude, name, display_name, zone, total_lines, rail):
        self._id = id_s
        self._latitude = latitude
        self._longitude = longitude
        self._name = name
        self._display_name = display_name
        self._zone = zone
        self._total_lines = total_lines
        self._rail = rail

    def get_id(self):
        return self._id

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def get_name(self):
        return self._name

    def get_display_name(self):
        return self._display_name

    def get_zone(self):
        return self._zone

    def get_total_lines(self):
        return self._total_lines

    def get_rail(self):
        return self._rail


# Class Connections ____________________________________________________________________________________________________


class Connections:

    def __init__(self, st1, st2, line=None, time=None):
        self._st1 = st1
        self._st2 = st2
        self._line = {line}
        self._time = [time]

    def get_time(self):
        return self._time

    def get_line(self):
        return self._line

    def get_st1_st2(self):
        return [self._st1, self._st2]

    def get_start(self):
        return self._st1

    def get_end(self):
        return self._st2

    def opposite(self, st):
        if st == self._st1:
            return self._st2
        if st == self._st2:
            return self._st1
        else:
            raise Exception('The station you are looking for does not exist')

    def get_time_average(self):
        t_sum1, t_sum2, t_sum3 = 0, 0 , 0
        for time_tuple in self._time:
            t_sum1, t_sum2, t_sum3 = t_sum1 + time_tuple[0], t_sum2 + time_tuple[1], t_sum3 + time_tuple[0]
        n = len(self._time)
        self._time = [(t_sum1/n, t_sum2/n, t_sum3/n)]
# ______________________________________________________________________________________________________________________
