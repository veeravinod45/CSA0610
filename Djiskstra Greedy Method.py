n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex: "))

INF = 999999

distance = [INF] * n
visited = [False] * n

distance[source] = 0

for _ in range(n):

    min_distance = INF
    u = -1

    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance

print("\nShortest distances from vertex", source)

for i in range(n):
    print(source, "->", i, "=", distance[i])

