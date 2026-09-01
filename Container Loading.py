n = int(input("Enter number of containers: "))

weights = []

for i in range(n):
    weight = int(input("Enter weight: "))
    weights.append(weight)

capacity = int(input("Enter ship capacity: "))

weights.sort()

total_weight = 0
count = 0
selected = []

for weight in weights:
    if total_weight + weight <= capacity:
        total_weight += weight
        selected.append(weight)
        count += 1
    else:
        break

print("\nSelected containers:", selected)
print("Number of containers loaded:", count)
print("Total weight:", total_weight)
