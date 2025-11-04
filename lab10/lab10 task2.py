name = input("введите модель танка: ")
cost = input("введите стоимость: ")

with open("tanks.txt", "a") as file:
    file.write(f"\n{name}, {cost}")
print("запись прошла успешна!")
