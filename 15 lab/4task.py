# Реализация паттерна Observer

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

# Базовый интерфейс наблюдателя
class Observer:
    def update(self, state):
        raise NotImplementedError("Метод update должен быть реализован")

# Первый наблюдатель — логгер
class LoggerObserver(Observer):
    def update(self, state):
        print(f"[Logger] Состояние изменилось на: {state}")

# Второй наблюдатель — уведомление
class NotificationObserver(Observer):
    def update(self, state):
        print(f"[Notification] Новое событие: {state}")

# Демонстрация
if __name__ == "__main__":
    subject = Subject()

    logger = LoggerObserver()
    notifier = NotificationObserver()

    subject.attach(logger)
    subject.attach(notifier)

    subject.set_state("Otto завершил демонстрацию MongoDB")
    subject.set_state("Otto получил 100% за ACL в Packet Tracer")
