import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (станцій)
stations = {
    1: "Площадь Труда",
    2: "Солнечная",
    3: "Городская больница",
    4: "Бульвар Вечерний",
    5: "Мудрёная",
    6: "Дом Советов",
    7: "Проспект Металлургов",
    8: "Кольцевая"
}
G.add_nodes_from(stations.keys())

# Додавання ребер (маршрутів між станціями)
routes = [
    (1, 2), (2, 3), (3, 4),(4, 5), (5, 6), (6, 7),(7, 8)
]
G.add_edges_from(routes)

# Візуалізація графа
pos = nx.spring_layout(G)  # визначення позицій для вузлів
nx.draw(G, pos, with_labels=True, labels=stations, node_color='skyblue', node_size=1500, edge_color='gray', font_size=12, font_weight='bold')
plt.title("Transport Network")
plt.show()

# Кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

# Список вершин та ребер
nodes = G.nodes()
edges = G.edges()
print(f"Nodes: {nodes}")
print(f"Edges: {edges}")

# Ступінь кожної вершини
degrees = dict(G.degree())
print(f"Degree of each node: {degrees}")

# Середній ступінь вершин
avg_degree = sum(degrees.values()) / num_nodes
print(f"Average degree: {avg_degree:.2f}")
