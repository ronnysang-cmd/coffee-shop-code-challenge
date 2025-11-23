class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        coffee_orders = []
        for order in Order.all:
            if order.coffee == self:
                coffee_orders.append(order)
        return coffee_orders

    def customers(self):
        customer_list = []
        for order in self.orders():
            if order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list

    def num_orders(self):
        count = 0
        for order in self.orders():
            count += 1
        return count

    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0
        total = 0
        for order in orders:
            total += order.price
        return total / len(orders)