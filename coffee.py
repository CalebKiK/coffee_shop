"""Coffee class"""
class Coffee:
    def __init__(self, name):
        """Initialize an instance coffee class with a name"""
        self.name = name
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

    def orders(self):
        """List of all order instances for that coffee"""
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        """unique list of customers who have ordered that coffee"""
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        """Return total number of times the coffee has been ordered."""
        return len(self.orders())
    
    def average_price(self):
        """Return average price of coffee based on the orders"""
        total_price = sum(order.price for order in self.orders())
        return total_price / len(self.orders())