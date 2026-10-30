INF = 9999999
V = 8
# Матриця суміжності для Варіанту 2
G = [
    [0, 1, 6, 2, INF, INF, INF, INF],
    [1, 0, INF, 4, 9, 5, INF, INF],
    [6, INF, 0, INF, INF, 8, INF, 9],
    [2, 4, INF, 0, 1, INF, INF, INF],
    [INF, 9, INF, 1, 0, INF, 6, INF],
    [INF, 5, 8, INF, INF, 0, 2, INF],
    [INF, INF, INF, INF, 6, 2, 0, 4],
    [INF, INF, 9, INF, INF, INF, 4, 0]
]
selected = [False] * V
selected[0] = True
no_edge = 0

print("--- АЛГОРИТМ ПРИМА ---")
print("Edge : Weight")
while no_edge < V - 1:
    min_val = INF
    x, y = 0, 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and G[i][j]:
                    if G[i][j] < min_val:
                        min_val = G[i][j]
                        x, y = i, j
    print(f"{x+1} - {y+1} : {min_val}")
    selected[y] = True
    no_edge += 1
