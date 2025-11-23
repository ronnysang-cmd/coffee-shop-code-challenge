import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def setup_method(self):
        Order.all = []

    def test_coffee_name(self):
        coffee = Coffee("Espresso")
        assert coffee.name == "Espresso"

    def test_bad_coffee_names(self):
        with pytest.raises(ValueError):
            Coffee("AB")  
        with pytest.raises(ValueError):
            Coffee(123)  

    def test_orders_method(self):
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        order = Order(customer, coffee, 4.50)
        
        orders = coffee.orders()
        assert len(orders) == 1
        assert orders[0] == order

    def test_customers_method(self):
        coffee = Coffee("Cappuccino")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        Order(customer1, coffee, 4.00)
        Order(customer2, coffee, 4.25)
        
        customers = coffee.customers()
        assert len(customers) == 2

    def test_num_orders_method(self):
        coffee = Coffee("Mocha")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        assert coffee.num_orders() == 0
        
        Order(customer1, coffee, 5.00)
        assert coffee.num_orders() == 1
        
        Order(customer2, coffee, 5.25)
        assert coffee.num_orders() == 2

    def test_average_price_method(self):
        coffee = Coffee("Americano")
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        
        assert coffee.average_price() == 0
        
        Order(customer1, coffee, 3.00)
        Order(customer2, coffee, 5.00)
        
        assert coffee.average_price() == 4.0