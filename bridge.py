from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, payment_method):
        self.payment_method = payment_method

    @abstractmethod
    def purchase(self):
        pass


class Tea(Beverage):
    def __init__(self, payment_method, price):
        super().__init__(payment_method)
        self.price = price

    def purchase(self):
        print("Purchasing tea...")
        self.payment_method.pay(self.price)


class Coffee(Beverage):
    def __init__(self, payment_method, price):
        super().__init__(payment_method)
        self.price = price

    def purchase(self):
        print("Purchasing coffee...")
        self.payment_method.pay(self.price)


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


credit_card = CreditCard()
cash = Cash()
paypal = PayPal()

tea_with_credit = Tea(credit_card, 3.5)
black_tea_with_cash = Tea(cash, 2.5)

coffee_with_cash = Coffee(cash, 4.0)
coffe_with_paypal = Coffee(paypal, 3.8)

tea_with_credit.purchase()
coffee_with_cash.purchase()
coffe_with_paypal.purchase()

