from call_plan import CallPlanSimple

class Customer:
    """Клиент телефонной компании."""

    def __init__(self, name, balance=0, call_plan=None):
        self.name = name
        self._balance = balance
        self.call_plan = call_plan
        # Если тарифный план не был указан, используем CallPlanSimple()
        if self.call_plan is None:
            self.call_plan = CallPlanSimple()

    def __str__(self):
        return "Клиент \"{}\". Баланс: {} руб. Тариф: \"{}\"". \
            format(self.name, self.balance, self.call_plan.name)

    @property
    def balance(self):
        """Вернуть баланс клиента.

        Свойство 'balance' доступно только для чтения:
        давать доступ на изменение его напрямую было бы неправильно."""
        return self._balance

    def record_payment(self, amount_paid):
        """Пополнить баланс клиента на 'amount_paid' руб."""
        assert amount_paid > 0, "Сумма пополнения должна быть > 0!"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        """Списать стоимость звонка с баланса клиента.

        Параметры:
            - call_type (str): тип звонка:
                "Г": городской;
                "М": мобильный;

            - minutes (int): количество минут разговора.
        """
        # Делегируем определение стоимости звонка классу call_plan
        costs = self.call_plan.record_call(call_type, minutes)
        self._balance -= costs
