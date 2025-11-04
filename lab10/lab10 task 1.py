with open("tanks.txt", "r") as file:
    costs = []
    for line in file:
        tank, cost = line.strip().split(", ")
        cost = cost.replace('$', '')
        costs.append(int(cost))
        print(f"{tank} — {cost}")
    print("Средняя стоимость:", sum(costs) / len(costs))
