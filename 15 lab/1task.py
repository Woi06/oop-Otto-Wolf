import datetime

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
logger1 = Logger()
logger1.log("Otto начал тестирование ACL в Cisco Packet Tracer")
logger1.log("Otto провёл демонстрацию MongoDB: авторизация и резервное копирование")
logger1.log("Otto добавил систему примерки в проект магазина аниме-одежды")
for entry in logger1.logs:
    print(entry)
