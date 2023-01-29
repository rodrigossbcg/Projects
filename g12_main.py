# Projeto final - Estudo da rede de metro londrina
#
# Alunos:
# Ricardo E. Santo, nº 93357
# Rodrigo Sarroeira, nº 92761
# ______________________________________________________________________________________________________________________

import numpy as np
import plotly.graph_objects as go
from g12_dijkstra import London_Metro
from g12_minimum_Cut_Graph import Metro

# Conditions ___________________________________________________________________________________________________________

# Condições para visualização de resultados e visualização gráfica

# show results part 1
results_p1 = True

# show results part 2
results_p2 = True

# graph part 1
graph_1 = True

# graph part 2
graph_2 = True

# Main 1st part  _______________________________________________________________________________________________________

if __name__ == '__main__':

    # Criar classe Metro
    m1 = Metro()

    # Adicionar primeiro estações e depois criar ligações
    m1.create_stations()
    m1.create_connections()  # já com a limpeza de connections repetidas

    # Criar matriz de adjacências para o grafo (A)
    A = m1.adjacency()

    # Criar matriz de grau (degree matrix)
    D = m1.degree(A)

    # Criar matriz de Laplace (L = D - A)
    L = m1.laplacian(D, A)

    # Devolve os valores e o vétores prórios de L
    valores, vetores = m1.eigenvalues_eigenvectors(L)

    # Encontrar o vetor de Fiedler
    index_fiedler_value = np.argsort(valores)[1]
    partition = np.array([val >= 0 for val in vetores[:, index_fiedler_value]])
    c = len(partition)
    v_sinal = []
    for i in partition:
        if i:
            v_sinal.append(1)
        else:
            v_sinal.append(-1)
    v_sinal = np.array(v_sinal)

    # devole o id das estações pertencentes a g1 e a g2 (partição 1 e partição 2)
    g1 = []
    g2 = []
    names1 = []
    names2 = []
    coord_x1 = []
    coord_y1 = []
    coord_x2 = []
    coord_y2 = []
    for i in range(0, len(v_sinal)):
        if v_sinal[i] == - 1:
            g1.append(m1.read_stations()[i][0])
            names1.append(m1.read_stations()[i][3])
            coord_x1.append(m1.read_stations()[i][2])
            coord_y1.append(m1.read_stations()[i][1])
        else:
            g2.append(m1.read_stations()[i][0])
            names2.append(m1.read_stations()[i][3])
            coord_x2.append(m1.read_stations()[i][2])
            coord_y2.append(m1.read_stations()[i][1])

    # número mínimo de cortes
    n_cuts = 0.25 * np.dot(np.dot(v_sinal.transpose(), L), v_sinal)

    # Ratio cut partition
    f = n_cuts / (len(g1) * len(g2))

    if results_p1:
        print('=====================================================')
        print('Results for the Spectral Bissection Algorithm', end="\n\n")
        print('The number of cut edges is: ' + str(n_cuts))
        print('The number of nodes in graph 1 is ' + str(len(g1)))
        print('The number of nodes in graph 2 is ' + str(len(g2)))
        print('The ratio cut partition, f = ' + str(f))


# Graph minimum cut info _______________________________________________________________________________________________

    edge_x = []
    edge_y = []
    for edge in m1.read_connections():
        st1 = edge[0]
        st2 = edge[1]
        x0, y0 = m1.rawData[st1].get_longitude(), m1.rawData[st1].get_latitude()
        x1, y1 = m1.rawData[st2].get_longitude(), m1.rawData[st2].get_latitude()
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_c_x = []
    edge_c_y = []
    for edge in m1.cuts(g1, g2):
        st1, st2 = edge
        x0, y0 = m1.rawData[st1].get_longitude(), m1.rawData[st1].get_latitude()
        x1, y1 = m1.rawData[st2].get_longitude(), m1.rawData[st2].get_latitude()
        edge_c_x.append(x0)
        edge_c_x.append(x1)
        edge_c_x.append(None)
        edge_c_y.append(y0)
        edge_c_y.append(y1)
        edge_c_y.append(None)

# Edge Generator _______________________________________________________________________________________________________

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#00ff00'),
        hoverinfo='none',
        mode='lines')

    edge_cuts = go.Scatter(
        x=edge_c_x, y=edge_c_y,
        line=dict(width=1, color='#fe2ec8'),
        hoverinfo='none',
        mode='lines')

# Node Generator _______________________________________________________________________________________________________

    node_x = []
    node_y = []
    for id_station in m1.read_stations():
        node_x.append(id_station[2])
        node_y.append(id_station[1])

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='Bluered',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_adjacencies = []
    node_text = []
    i = 0
    for key in m1.rawData.keys():
        node_adjacencies.append(D[i, i])
        node_text.append('# of connections: ' + str(D[i, i]) + '  ' + m1.rawData[key].get_name())
        i = i + 1

    node_trace.marker.color = v_sinal
    node_trace.text = node_text

# Plot options _________________________________________________________________________________________________________

    fig = go.Figure(data=[edge_trace, node_trace, edge_cuts],
                    layout=go.Layout(
                        title='<br> London Subway Network',
                        titlefont_size=25,
                        showlegend=False,
                        plot_bgcolor='#000000',
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Python code: <a Trabalho EDA /</a>",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    if graph_1:
        fig.show()

# Main 2nd part ________________________________________________________________________________________________________

    # Criar classe Metro
    m2 = London_Metro()

    # Adicionar estações e depois criar ligações
    m2.create_stations()
    m2.create_connections()  # já com a limpeza de algumas connections repetidas

    # Definição dos parametros (seeds) para o algoritmo de Dijkstra (número das estações)

    start = 232
    # 114
    # 232
    end = 6
    # 90
    # 6
    n = 2
    # 2

    # Veriável que guarda o caminho ótimo
    optimal_path = m2.dijkstra(start, end, n)

    # Cálculo dos tempo de deslocação (metro) , tempo de mudança de linha, tempo total da viagem
    travel_time = m2.get_travel_time(optimal_path, n)
    change_time = m2.get_change_time(optimal_path)
    total_time = travel_time + change_time

    if results_p2:
        print('=====================================================')
        print('Results for the shortest path (Dijkstra Algorithm)', end="\n\n")
        print('The optimal path is ' + str(optimal_path))
        print('Total time = ' + str(total_time))
        print('Change time = ' + str(change_time))


# Graph Dijkstra Info __________________________________________________________________________________________________

    edge_x = []
    edge_y = []
    for edge in m2.read_connections():
        st1 = edge[1]
        st2 = edge[2]
        x0, y0 = m2.rawData[st1].get_longitude(), m2.rawData[st1].get_latitude()
        x1, y1 = m2.rawData[st2].get_longitude(), m2.rawData[st2].get_latitude()
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_c_x = []
    edge_c_y = []
    for edge in m2.get_list(optimal_path):
        st1, st2 = edge
        x0, y0 = m2.rawData[st1].get_longitude(), m2.rawData[st1].get_latitude()
        x1, y1 = m2.rawData[st2].get_longitude(), m2.rawData[st2].get_latitude()
        edge_c_x.append(x0)
        edge_c_x.append(x1)
        edge_c_x.append(None)
        edge_c_y.append(y0)
        edge_c_y.append(y1)
        edge_c_y.append(None)

# Edge Generator _______________________________________________________________________________________________________

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#00ff00'),
        hoverinfo='none',
        mode='lines')

    edge_cuts = go.Scatter(
        x=edge_c_x, y=edge_c_y,
        line=dict(width=3, color='#fe2ec8'),
        hoverinfo='none',
        mode='lines')

# Node Generator _______________________________________________________________________________________________________

    node_x = []
    node_y = []
    for id_station in m2.read_stations():
        node_x.append(id_station[2])
        node_y.append(id_station[1])

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            # colorscale options
            # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='ice',
            reversescale=True,
            color=[],
            size=7,
            colorbar=dict(
                thickness=45,
                title='Number of lines',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    node_text = []
    for key in m2.rawData.keys():
        node_text.append('Station: ' + m2.rawData[key].get_name())

    node_trace.text = node_text
    node_trace.marker.color = np.zeros(302)

# Plot options _________________________________________________________________________________________________________

    fig = go.Figure(data=[edge_trace, node_trace, edge_cuts],
                    layout=go.Layout(
                        title='<br> Optimal path',
                        titlefont_size=25,
                        showlegend=False,
                        plot_bgcolor='#000000',
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Python code: <a Trabalho EDA /</a>",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    if graph_2:
        fig.show()

# ______________________________________________________________________________________________________________________
