"""Order class"""
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        """Initialize an instance of order class"""
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    """price property"""
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

    """customer property"""
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        from customer import Customer 
        if not isinstance(customer, Customer):
            raise TypeError("Customer should be an instance of Customer class.")
        self._customer = customer

    """coffee property"""
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee should be an instance of Coffee class.")
        self._coffee = coffee