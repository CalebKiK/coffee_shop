class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the coffee name once it has been set.")
        if not isinstance(value, str):
            raise TypeError("Coffee name must be of type str.")
        if len(value) < 3:
            raise ValueError("Customer name should be at least 3 characters long.")
        self._name = value
    # def orders(self):
    #     return self._orders
    
    # def customers(self):
    #     return list({order.customer for order in self._orders if isinstance(order.customer, Customer)})
    
    # def num_orders(self):
    #     return len(self._orders)
    
    # def average_price(self):
    #     total_price = sum(order.price for order in self._orders)
    #     return total_price / len(self._orders)