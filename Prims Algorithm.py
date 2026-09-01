INF = 999999
graph = [
    [0, 4, 0, 0, 0, 2],
    [4, 0, 5, 0, 0, 0],
    [0, 5, 0, 3, 0, 0],
    [0, 0, 3, 0, 6, 0],
    [0, 0, 0, 6, 0, 7],
    [2, 0, 0, 0, 7, 0]
]
n = len(graph)
selected = [False] * n
selected[0] = True
total = 0
print("Prim's MST:")
for _ in range(n - 1):
    minimum = INF
    x = y = 0
    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(chr(65 + x), "-", chr(65 + y), "=", minimum)
    total += minimum
    selected[y] = True
print("Total Cost =", total)
