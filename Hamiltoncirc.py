def ham(pos):
    if pos == n:
        return graph[path[-1]][path[0]] == 1

    for v in range(1, n):
        if v not in path and graph[path[-1]][v]:
            path.append(v)

            if ham(pos + 1):
                return True

            path.pop()

    return False


graph = [
    [0,1,1,0],
    [1,0,1,1],
    [1,1,0,1],
    [0,1,1,0]
]

n = len(graph)
path = [0]

if ham(1):
    print(path + [0])
else:
    print("No cycle")
