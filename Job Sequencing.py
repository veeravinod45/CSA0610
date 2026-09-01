n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    job = input("Enter job name: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append((job, deadline, profit))

jobs.sort(key=lambda x: x[2], reverse=True)

max_deadline = max(job[1] for job in jobs)

slots = [None] * (max_deadline + 1)

total_profit = 0

for job, deadline, profit in jobs:
    for j in range(deadline, 0, -1):
        if slots[j] is None:
            slots[j] = job
            total_profit += profit
            break

print("\nJob Sequence:")

for i in range(1, len(slots)):
    if slots[i] is not None:
        print("Slot", i, ":", slots[i])

print("Maximum Profit:", total_profit)
