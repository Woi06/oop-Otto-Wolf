try:
    with open("tanks.txt", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("Ошибка: Файл не найден!")
else:
    print("Файл успешно прочитан.")
    for line in data:
        print(line.strip())
finally:
    print("Программа завершена.")
