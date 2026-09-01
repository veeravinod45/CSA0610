n = int(input("Enter number of items: "))

items = []

for i in range(n):
    profit = int(input("Enter profit: "))
    weight = int(input("Enter weight: "))
    ratio = profit / weight
    items.append((profit, weight, ratio))

capacity = int(input("Enter knapsack capacity: "))

items.sort(key=lambda x: x[2], reverse=True)

total_profit = 0

for profit, weight, ratio in items:
    if capacity >= weight:
        capacity -= weight
        total_profit += profit
        print("Taken:", profit, weight)
    else:
        fraction = capacity / weight
        total_profit += profit * fraction
        print("Taken:", round(fraction, 2), "of item")
        break

print("Maximum Profit:", round(total_profit, 2))
