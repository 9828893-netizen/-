class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([w, u, v])
    def find(self, parent, i):
        if parent[i] == i: return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]: parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]: parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[0])
        parent, rank = [], []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            w, u, v = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("--- АЛГОРИТМ КРУСКАЛА ---")
        print("Edge : Weight")
        total = 0
        for u, v, weight in result:
            print(f"{u+1} - {v+1} : {weight}")
            total += weight
        print(f"Загальна вага: {total}")

g = Graph(8)
edges = [
    (0, 1, 1), (0, 2, 6), (0, 3, 2), 
    (2, 3, 4), (1, 4, 9), (1, 5, 5), 
    (2, 5, 8), (2, 7, 9), 
    (3, 4, 1), 
    (4, 6, 6), 
    (5, 6, 2), 
    (6, 7, 4)
]
for u, v, w in edges: g.add_edge(u, v, w)
g.kruskal_mst()
