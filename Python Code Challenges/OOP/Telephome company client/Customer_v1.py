class Customer:
    """Telephone company customer """

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance

    def __str__(self):
        return "Client \"{}\". Balance: {}$".format(self.name, self.balance)

    @property
    def balance(self):
        return self._balance

    def record_payment(self, amount_paid):
        # top up client balance
        assert amount_paid > 0, "The top-up amount must be > 0!"
        self._balance += amount_paid

    def record_call(self, call_type, minutes):
        # deduct the cost of a call from the client's balance
        if call_type == "U":  # urban call
            self._balance -= minutes * 5
        elif call_type == "M":  # mobile call
            self._balance -= minutes * 1

class CustomerFree2ndMinuteAfter10(Customer):
    """Telephone company customer (Customer inheritor)"""

    def record_call(self, call_type, minutes):
        if call_type == "U" and minutes > 10:
            bonus_minutes = (minutes - 10) // 2
        else:
            bonus_minutes = 0

        # Calling the parent calculation method
        super().record_call(call_type, minutes - bonus_minutes)


class CustomerTwiceCheaperFirst5Minutes(Customer):
    """Telephone company customer (Customer inheritor)"""

    def record_call(self, call_type, minutes):
        LIMIT_CHEAP = 5
        if minutes > LIMIT_CHEAP:
            cheap_minutes = LIMIT_CHEAP
            expensive_minutes = minutes - LIMIT_CHEAP
        else:
            cheap_minutes = minutes
            expensive_minutes = 0

        super().record_call(call_type, cheap_minutes / 2 + expensive_minutes * 2)


if __name__ == "__main__":
    ivan = Customer("Ivan Petrov", 100)
    # elena, ekaterina and sergey are instances of other classes
    elena = CustomerFree2ndMinuteAfter10("Elena Mironova", 100)
    ekaterina = CustomerFree2ndMinuteAfter10("Ekaterina Efimova", 100)
    sergey = CustomerTwiceCheaperFirst5Minutes("Sergey Vasiliev", 100)

    ivan.record_call("U", 20)
    elena.record_call("U", 20)
    ekaterina.record_call("M", 20)
    sergey.record_call("U", 20)

    print(ivan)
    print(elena)
    print(ekaterina)
    print(sergey)

