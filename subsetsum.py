def subset(i, total):
    if total == target:
        print(result)
        return True

    if i == len(a) or total > target:
        return False

    result.append(a[i])

    if subset(i + 1, total + a[i]):
        return True

    result.pop()

    return subset(i + 1, total)


a = [10, 7, 5, 18, 12]
target = 35
result = []

subset(0, 0)
