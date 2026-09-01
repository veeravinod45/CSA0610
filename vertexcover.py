def cover(edges, k, result=[]):
    if len(result) == k:
        if all(u in result or v in result for u, v in edges):
            print(result)
            return True
        return False

    for v in range(1, n + 1):
        if v not in result:
            result.append(v)
            if cover(edges, k, result):
                return True
            result.pop()

    return False


edges = [(1,2), (1,3), (2,3), (3,4)]
n = 4
cover(edges, 2)
