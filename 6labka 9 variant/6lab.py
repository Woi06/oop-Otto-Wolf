import random
A = [random.randint(1, 100) for _ in range(15)]
print("Сгенерированный массив:", A)
print()
for x in A:
    if x % 5 == 0:
        print(f"{x} делится на 5")
    else:
        print(f"{x} не делится на 5")