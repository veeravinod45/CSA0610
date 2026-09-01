items = [4, 8, 1, 4, 2, 1]
capacity = 10

bins = []

for item in items:
    for b in bins:
        if sum(b) + item <= capacity:
            b.append(item)
            break
    else:
        bins.append([item])

print("Bins:", bins)
print("Number of bins:", len(bins))
