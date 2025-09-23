import random
A = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]
for row in A:
    print(row)
product = 1
for i in range(4):
    for j in range(4):
        if i > j:
            product *= A[i][j]
print("Произведение элементов ниже главной диагонали =", product)