V = 5
edges = [(1, 2, 4), (1, 3, 2), (2, 3, 1), (2, 4, 5), (3, 4, 8), (3, 5, 10), (4, 5, 2)]
INF = 999999
G = [[INF] * V for _ in range(V)]
for i in range(V): G[i][i] = 0
for u, v, w in edges:
    G[u-1][v-1] = w
    G[v-1][u-1] = w

def dijkstra(start):
    dist, pred = [INF] * V, [-1] * V
    dist[start] = 0
    visited = [False] * V
    for _ in range(V):
        min_d, u = INF, -1
        for i in range(V):
            if not visited[i] and dist[i] < min_d:
                min_d, u = dist[i], i
        if u == -1: break
        visited[u] = True
        for v in range(V):
            if G[u][v] != INF and not visited[v] and dist[u] + G[u][v] < dist[v]:
                dist[v], pred[v] = dist[u] + G[u][v], u + 1
    return dist, pred

def floyd():
    D = [row[:] for row in G]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][k] + D[k][j] < D[i][j]: D[i][j] = D[i][k] + D[k][j]
    return D

print("--- АЛГОРИТМ ДЕЙКСТРИ (Старт з вершини 1) ---")
dist, pred = dijkstra(0)
for i in range(1, V): print(f"До вершини {i+1}: відстань = {dist[i]}, попередник = {pred[i]}")

print("\n--- АЛГОРИТМ ФЛОЙДА ---")
D = floyd()
for row in D: print([val if val != INF else 'INF' for val in row])
