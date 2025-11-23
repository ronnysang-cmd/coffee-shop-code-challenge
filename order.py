class Order:
    all = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer class")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee class")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        if price < 1.0 or price > 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price