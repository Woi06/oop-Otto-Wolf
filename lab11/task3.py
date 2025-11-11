import math

class Spell:
    def area_of_effect(self):
        pass

class Fireball(Spell):
    def __init__(self, radius):
        self.radius = radius

    def area_of_effect(self):
        return math.pi * self.radius ** 2

class IceWall(Spell):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of_effect(self):
        return self.width * self.height

# Список заклинаний
spells = [Fireball(3), IceWall(5, 2)]

# Вывод площади действия каждого заклинания
for spell in spells:
    area = round(spell.area_of_effect(), 2)
    print(f"📏 Площадь действия заклинания: {area} м²")
