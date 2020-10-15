from customer import Customer
from call_plan import CallPlanFree2ndMinuteAfter10, CallPlanTwiceCheaperFirst5Minutes

if __name__ == "__main__":

    ivan = Customer("Иван Петров", 100)

    # 1. Используется тариф по умолчанию
    ivan.record_call("Г", 20)
    print(ivan)  # Клиент "Иван Петров". Баланс: 0 руб. Тариф: "Повременный"

    ivan.record_payment(100 - ivan.balance)  # Пополнили телефон до 100 руб.

    # 2. Меняем тариф на CallPlanFree2ndMinuteAfter10
    ivan.call_plan = CallPlanFree2ndMinuteAfter10()
    ivan.record_call("Г", 20)
    print(ivan)  # Клиент "Иван Петров". Баланс: 25 руб. Тариф: "После10В2РазаДешевле"

    ivan.record_payment(100 - ivan.balance)  # Пополнили телефон до 100 руб.

    # 3. Меняем тариф на CallPlanTwiceCheaperFirst5Minutes
    ivan.call_plan = CallPlanTwiceCheaperFirst5Minutes()
    ivan.record_call("Г", 20)
    print(ivan)  # Клиент "Иван Петров". Баланс: -62.5 руб. Тариф: "ПлатиМеньшеДо5Минут"