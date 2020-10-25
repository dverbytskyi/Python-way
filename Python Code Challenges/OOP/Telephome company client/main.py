from customer import Customer
from call_plan import CallPlanSimple, \
                      CallPlanFree2ndMinuteAfter10, \
                      CallPlanTwiceCheaperFirst5Minutes

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
    print(ivan, "\n")  # Клиент "Иван Петров". Баланс: -62.5 руб. Тариф: "ПлатиМеньшеДо5Минут"

    call_plans = (CallPlanSimple(),
                  CallPlanFree2ndMinuteAfter10(),
                  CallPlanTwiceCheaperFirst5Minutes())

    minutes = tuple(range(0, 26, 5))  # 0, 5, 10, 15, 20, 25 мин.

    # Сравним стоимости звонков для тарифов
    for call_type in ("Г", "М"):
        print("{:20}".format(call_type), end="")
        # Заголовок - минуты
        for minute in minutes:
            print("{:>8d} мин.".format(minute), end="")
        print()

        # Подсчет стоимости
        for call_plan in call_plans:
            print("{:20}".format(call_plan.name), end="")
            for minute in minutes:
                print("{:>8.2f} руб.".format(call_plan.record_call(call_type, minute)), end="")
            print()

        print()