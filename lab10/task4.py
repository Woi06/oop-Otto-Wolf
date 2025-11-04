try:
    tank_name = input("введите имя танка: ")
    cost = int(input("введите стоимость танка: "))
    if cost < 300000:
        raise ValueError("цена низкая! стоимость нереалистичная.")
    print("информация о танке принята.")
except ValueError as e:
    print("ошибка:", e)
