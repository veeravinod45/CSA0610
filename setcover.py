U = {1, 2, 3, 4, 5}
sets = [{1, 2, 3}, {2, 4}, {3, 4, 5}, {1, 5}]

covered = set()
answer = []

while covered != U:
    s = max(sets, key=lambda x: len(x - covered))
    answer.append(s)
    covered |= s
    sets.remove(s)

print(answer)
