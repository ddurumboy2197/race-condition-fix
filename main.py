import threading
import time

class PollingLogic:
    def __init__(self):
        self.lock = threading.Lock()
        self.polling_condition = threading.Condition(self.lock)
        self.polling_status = False

    def start_polling(self):
        with self.polling_condition:
            self.polling_status = True
            self.polling_condition.notify_all()

    def stop_polling(self):
        with self.polling_condition:
            self.polling_status = False

    def is_polling(self):
        with self.polling_condition:
            return self.polling_status

    def polling_thread(self):
        while True:
            with self.polling_condition:
                if not self.polling_status:
                    break
                self.polling_condition.wait()

            # Polling logic here
            print("Polling...")
            time.sleep(1)

def main():
    polling_logic = PollingLogic()
    polling_thread = threading.Thread(target=polling_logic.polling_thread)
    polling_thread.start()

    while True:
        if polling_logic.is_polling():
            print("Polling is active")
        else:
            print("Polling is stopped")
            break

        time.sleep(1)

    polling_logic.stop_polling()

if __name__ == "__main__":
    main()
```

Bu kodda, `PollingLogic` klassi yaratilib, unda polling logigasi uchun zarur bo'lgan muhim qismlar mavjud. `start_polling` metodi pollingni boshlash uchun foydalaniladi, `stop_polling` metodi pollingni to'xtatish uchun foydalaniladi, `is_polling` metodi polling holatini tekshirish uchun foydalaniladi.

`polling_thread` funksiyasi polling logigasi uchun javob beradi. U polling holatini tekshirib, polling boshlanganda polling logigasi boshlanadi, polling to'xtaganda polling logigasi to'xtaydi.

`main` funksiyasi polling logigasi uchun asosiy funksiya bo'lib, unda polling logigasi boshlanadi va polling holati tekshiriladi.
