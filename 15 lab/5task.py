# Singleton: конфигурация магазина
class StoreConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StoreConfig, cls).__new__(cls)
            cls._instance.currency = "KZT"
            cls._instance.tax_rate = 0.12  # 12% налог
            cls._instance.discount_percent = 10
        return cls._instance

    def show(self):
        print(f"Валюта: {self.currency}, Налог: {self.tax_rate * 100}%, Скидка: {self.discount_percent}%")

# Strategy: базовый интерфейс оплаты
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Метод pay должен быть реализован")

# Стратегии оплаты
class KaspiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"[Kaspi] Оплата {amount} тенге прошла успешно")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"[Card] Списано {amount} тенге с банковской карты")

class QiwiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"[QIWI] Перевод {amount} тенге завершён")

# Factory: создаёт нужный объект оплаты
class PaymentFactory:
    _providers = {
        "kaspi": KaspiPayment,
        "card": CardPayment,
        "qiwi": QiwiPayment
    }

    @classmethod
    def get(cls, name):
        name = name.lower()
        if name in cls._providers:
            return cls._providers[name]()
        else:
            raise ValueError(f"Платёжный провайдер '{name}' не поддерживается")

# Основная функция оплаты
def process_payment(base_price, provider_name):
    config = StoreConfig()
    discount = base_price * (config.discount_percent / 100)
    tax = base_price * config.tax_rate
    final_price = base_price - discount + tax

    print(f"\n💳 Выбран провайдер: {provider_name}")
    print(f"Базовая цена: {base_price} тенге")
    print(f"Скидка: -{discount:.2f} тенге")
    print(f"Налог: +{tax:.2f} тенге")
    print(f"Итоговая сумма: {final_price:.2f} тенге")

    strategy = PaymentFactory.get(provider_name)
    strategy.pay(round(final_price))

# Демонстрация
if __name__ == "__main__":
    config = StoreConfig()
    config.show()

    process_payment(5000, "Kaspi")
    process_payment(7500, "Card")
    process_payment(3000, "Qiwi")
