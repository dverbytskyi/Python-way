class CallPlan:
    """Абстрактный класс для всех тарифных планов."""

    def __init__(self):
        self.name = "Абстрактный тариф"

    def record_call(self, call_type, minutes):
        """Списать стоимость звонка с баланса клиента.

        Параметры:
            - call_type (str): тип звонка:
                "Г": городской;
                "М": мобильный;

            - minutes (float): количество минут разговора.
        """
        # Делегируем расчет стоимости отдельному методу
        # Так, наследнику достаточно будет переопределить каждый из них,
        # не меняя общую логику ниже
        if call_type == "Г":
            return self.record_call_g(minutes)
        elif call_type == "М":
            return self.record_call_m(minutes)
        else:
            return 0

    def record_call_g(self, minutes):
        """Вернуть стоимость звонка на городской номер для 'minutes' минут."""
        raise NotImplementedError  # Должны реализовать дочерние классы

    def record_call_m(self, minutes):
        """Вернуть стоимость звонка на мобильный номер для 'minutes' минут."""
        raise NotImplementedError  # Должны реализовать дочерние классы


class CallPlanSimple(CallPlan):

    def __init__(self):
        self.name = "Повременный"

    def record_call_g(self, minutes):
        return minutes * 5

    def record_call_m(self, minutes):
        return minutes * 1


class CallPlanFree2ndMinuteAfter10(CallPlanSimple):

    def __init__(self):
        self.name = "После10В2РазаДешевле"

    def record_call_g(self, minutes):
        if minutes > 10:
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        # Вызываем родительский метод расчета
        return super().record_call_g(minutes - bonus_minutes)


class CallPlanTwiceCheaperFirst5Minutes(CallPlanSimple):

    def __init__(self):
        self.name = "ПлатиМеньшеДо5Минут"

    def record_call(self, call_type, minutes):
        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0

        # Вызываем родительский метод расчета
        return super().record_call(call_type, cheap_minutes / 2 +
                                   expensive_minutes * 2)