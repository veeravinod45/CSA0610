def floydWarshall(a):
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = min(a[i][j],
                               a[i][k] + a[k][j])
    print("Shortest Path Matrix:")
    for row in a:
        print(row)
INF = 999
a = [
    [0, 2, 9, INF],
    [2, 0, 3, 4],
    [9, 3, 0, 1],
    [INF, 4, 1, 0]
]
floydWarshall(a)
