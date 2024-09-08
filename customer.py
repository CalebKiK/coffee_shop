"""Class customer"""
class Customer:
    def __init__(self, name):
        """Initialize an instance of customer class with a name"""
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        """Initialize customer with a name string between 1 and 15 characters"""
        if not isinstance(name, str):
            raise TypeError("Customer name must be of string type.")
        if not 1<= len(name) <= 15:
            raise ValueError("Customer name characters not between 1 and 15.")
        self._name = name
 
    def orders(self):
        """Return a list of all order instances for that order"""
        from order import Order
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        """Return a unique list of coffee instances that the customer has ordered"""
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        """create a new order instance"""
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee should be an instance of Coffee.")
        order = Order(self, coffee, price)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        """Return customer who spent the most amount of money on the coffee."""
        from order import Order
        customer_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)