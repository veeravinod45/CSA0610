edges = [
    (4, 'A', 'B'),
    (5, 'B', 'C'),
    (3, 'C', 'D'),
    (6, 'D', 'E'),
    (7, 'E', 'F'),
    (2, 'A', 'F')
]
parent = {}
for edge in edges:
    parent[edge[1]] = edge[1]
    parent[edge[2]] = edge[2]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    parent[find(x)] = find(y)
edges.sort()
total = 0
count = 0
print("Kruskal's MST:")
for weight, u, v in edges:
    if find(u) != find(v):
        print(u, "-", v, "=", weight)
        total += weight
        union(u, v)
        count += 1
    if count == len(parent) - 1:
        break
print("Total Cost =", total)
