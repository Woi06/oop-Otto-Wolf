# Реализация паттерна Factory для уведомлений

class Notification:
    def send(self, message):
        raise NotImplementedError("Метод send должен быть реализован")

class EmailNotification(Notification):
    def send(self, message):
        print(f"[Email] Отправлено сообщение: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Отправлено сообщение: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"[Push] Отправлено сообщение: {message}")

class NotificationFactory:
    _registry = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }

    @classmethod
    def get(cls, type_name):
        type_name = type_name.lower()
        if type_name in cls._registry:
            return cls._registry[type_name]()
        else:
            raise ValueError(f"Тип уведомления '{type_name}' не поддерживается")

# Демонстрация
if __name__ == "__main__":
    factory = NotificationFactory()

    notif1 = factory.get("email")
    notif2 = factory.get("sms")
    notif3 = factory.get("push")

    notif1.send("Otto завершил демонстрацию MongoDB")
    notif2.send("Otto получил 100% за ACL в Packet Tracer")
    notif3.send("Otto добавил скидки в магазин аниме-одежды")
