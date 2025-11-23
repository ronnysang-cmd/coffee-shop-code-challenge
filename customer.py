class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        customer_orders = []
        for order in Order.all:
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders

    def coffees(self):
        coffee_list = []
        for order in self.orders():
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        customer_totals = {}
        
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer in customer_totals:
                    customer_totals[order.customer] += order.price
                else:
                    customer_totals[order.customer] = order.price
        
        if len(customer_totals) == 0:
            return None
        
        highest_spender = None
        highest_amount = 0
        for customer, total in customer_totals.items():
            if total > highest_amount:
                highest_amount = total
                highest_spender = customer
        
        return highest_spender