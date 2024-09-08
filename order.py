from customer import Customer 
from coffee import Coffee

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer should be an instance of Customer class.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee should be an instance of Coffee class.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        coffee._orders.append(self)
        customer._orders.append(self)
        Order.all.append(self)
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be of float type.")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0.")
        if hasattr(self, '_price'):
            raise AttributeError("Cannot change after the order is instantiated.")
        self._price = value
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee