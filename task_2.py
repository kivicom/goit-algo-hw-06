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

# Додавання ребер (маршрутів між станціями)
routes = [
    (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)
]
G.add_edges_from(routes)

# Візуалізація графа
pos = nx.spring_layout(G)  # визначення позицій для вузлів
nx.draw(G, pos, with_labels=True, labels=stations, node_color='skyblue', node_size=1500, edge_color='gray', font_size=12, font_weight='bold')
plt.title("Transport Network")
plt.show()

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Використання алгоритму DFS та BFS для обох ліній
start_stations = [0, 1]
goal_station = 8

for start in start_stations:
    dfs_result = list(dfs_paths(G, start, goal_station))
    bfs_result = list(bfs_paths(G, start, goal_station))

    print(f"DFS paths from '{stations[start]}' to '{stations[goal_station]}':")
    for path in dfs_result:
        print(" -> ".join(stations[node] for node in path))

    print(f"\nBFS paths from '{stations[start]}' to '{stations[goal_station]}':")
    for path in bfs_result:
        print(" -> ".join(stations[node] for node in path))

    print("\nComparison of DFS and BFS results:")

    dfs_path = next(dfs_paths(G, start, goal_station))
    bfs_path = next(bfs_paths(G, start, goal_station))

    print(f"\nDFS path: {' -> '.join(stations[node] for node in dfs_path)}")
    print(f"BFS path: {' -> '.join(stations[node] for node in bfs_path)}")

    print("\nПояснення:")
    print("DFS досліджує якомога далі кожну гілку перед зворотним відстеженням. Спочатку може знайти довший шлях.")
    print("BFS досліджує всіх сусідів на поточній глибині, перш ніж перейти до вузлів на наступному рівні глибини. Він завжди знаходить найкоротший шлях з точки зору кількості ребер.")
    print("\n" + "="*50 + "\n")
