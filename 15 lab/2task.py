# Реализация паттерна Strategy для расчёта скидок

class DiscountStrategy:
    def apply(self, price):
        raise NotImplementedError("Метод apply должен быть реализован")

class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)

def calculate_total(price, strategy: DiscountStrategy):
    return strategy.apply(price)

# Демонстрация смены стратегий
if __name__ == "__main__":
    price = 1000

    strategies = [
        ("Без скидки", NoDiscount()),
        ("Скидка 15%", PercentageDiscount(15)),
        ("Скидка 300 тенге", FixedDiscount(300))
    ]

    for name, strategy in strategies:
        total = calculate_total(price, strategy)
        print(f"{name}: {total} тенге")
