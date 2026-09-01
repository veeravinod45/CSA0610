edges = [
    (4, 'A', 'B'),
    (5, 'B', 'C'),
    (3, 'C', 'D'),
    (6, 'D', 'E'),
    (7, 'E', 'F'),
    (2, 'A', 'F')
]
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
parent = {}
for v in vertices:
    parent[v] = v
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False
total = 0
mst = []
while len(mst) < len(vertices) - 1:
    cheapest = {}
    for weight, u, v in edges:
        set_u = find(u)
        set_v = find(v)
        if set_u != set_v:
            if set_u not in cheapest or weight < cheapest[set_u][0]:
                cheapest[set_u] = (weight, u, v)
            if set_v not in cheapest or weight < cheapest[set_v][0]:
                cheapest[set_v] = (weight, u, v)
    for weight, u, v in cheapest.values():
        if union(u, v):
            mst.append((u, v, weight))
            total += weight
            print(u, "-", v, "=", weight)
print("Total Cost =", total)
