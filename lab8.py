import collections
import random

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = collections.defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def bfs(self, s, t, parent):
        visited = {node: False for node in self.nodes}
        queue = collections.deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v, cap in self.graph[u].items():
                if not visited[v] and cap > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = {}
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v].setdefault(u, 0)
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

# Инициализация узлов
nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'T']
g = Graph(nodes)

# Генерация случайных весов для ребер из схемы
edges = [
    ('S','A'), ('S','C'), ('S','D'), ('S','B'), ('A','C'), ('B','D'),
    ('C','E'), ('C','F'), ('D','E'), ('D','F'), ('E','G'), ('E','H'),
    ('F','G'), ('F','H'), ('G','H'), ('G','T'), ('H','T')
]

print("Сгенерированные веса:")
for u, v in edges:
    cap = int(input(f'{u} -> {v}'))
    # cap = random.randint(100, 1000)
    g.add_edge(u, v, cap)
    print(f"{u} -> {v}: {cap}")

print(f"\nМаксимальный поток: {g.ford_fulkerson('S', 'T')}")
