def color(v):
    if v == n:
        print(coloring)
        return True

    for c in range(1, m + 1):
        if all(graph[v][i] == 0 or coloring[i] != c
               for i in range(n)):
            coloring[v] = c
            if color(v + 1):
                return True
            coloring[v] = 0
    return False


graph = [[0,1,1,0],
         [1,0,1,1],
         [1,1,0,1],
         [0,1,1,0]]

n, m = 4, 3
coloring = [0] * n
color(0)
