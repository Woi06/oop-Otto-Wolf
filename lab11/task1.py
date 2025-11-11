class астральный_маг:
    def __init__(self, name, level, player_id, rating, abilities, hero_class):
        self.name = name
        self.level = level
        self.player_id = player_id
        self.уровень_навыков = rating
        self.abilities = abilities
        self.hero_class = hero_class

    def display_info(self):
        print("🎮 Игра: Soul Knight Prequel")
        print("=== Главный герой ===")
        print(f"👤 Имя: {self.name}")
        print(f"🎯 Уровень: {self.level}")
        print(f"🆔 ID: {self.player_id}")
        print(f"📚 Класс: {self.hero_class}")
        print(f"⭐ Уровень навыков: {self.уровень_навыков}/10")
        print(f"✨ Способности: {', '.join(self.abilities)}")

player1 = астральный_маг(
    "Woi",
    67,
    "N6767",
    8,
    ["Звёздный взрыв", "Астральная броня", "Снятие чар: стеллахрома"],
    "астральный маг"
)
player1.display_info()
