import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (станцій)
stations = {
    0: "Зарічна",
    1: "Майдан праці",
    2: "Сонячна",
    3: "Міська лікарня",
    4: "Бульвар Вечерній",
    5: "Мудрьона",
    6: "Будинок рад",
    7: "Проспект Металлургів",
    8: "Кільцева"
}
G.add_nodes_from(stations.keys())

# Додавання ребер з вагами (маршрутів між станціями)
routes = [
    (0, 2, 4), (1, 2, 2), (2, 3, 3), (3, 4, 2),
    (4, 5, 4), (5, 6, 3), (6, 7, 2), (7, 8, 5)
]
G.add_weighted_edges_from(routes)

# Візуалізація графа
pos = nx.spring_layout(G)  # визначення позицій для вузлів
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, labels=stations, node_color='skyblue', node_size=1500, edge_color='gray', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Transport Network with Weights")
plt.show()

# Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів між всіма вершинами
def dijkstra_all_pairs_shortest_paths(graph):
    paths = dict(nx.all_pairs_dijkstra_path(graph))
    lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    return paths, lengths

# Використання алгоритму Дейкстри
paths, lengths = dijkstra_all_pairs_shortest_paths(G)

# Виведення результатів
print("Shortest paths between all pairs of stations:")
for start_node, path_dict in paths.items():
    for end_node, path in path_dict.items():
        print(f"{stations[start_node]} -> {stations[end_node]}: {' -> '.join(stations[node] for node in path)} (Distance: {lengths[start_node][end_node]})")
