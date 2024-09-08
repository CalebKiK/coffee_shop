from coffee import Coffee

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Customer name must be of string type.")
        if not 1<= len(name) <= 15:
            raise ValueError("Customer name characters not between 1 and 15.")
        self._name = name
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self._orders if isinstance(order.coffee, Coffee)})
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.orders().append(order)
        return order
    
    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)