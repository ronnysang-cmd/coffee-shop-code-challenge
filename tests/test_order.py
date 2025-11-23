import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def setup_method(self):
        Order.all = []

    def test_order_creation(self):
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 3.50)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 3.50
        assert order in Order.all

    def test_bad_customer(self):
        coffee = Coffee("Latte")
        with pytest.raises(ValueError):
            Order("not_a_customer", coffee, 4.00)

    def test_bad_coffee(self):
        customer = Customer("Bob")
        with pytest.raises(ValueError):
            Order(customer, "not_a_coffee", 4.00)

    def test_bad_prices(self):
        customer = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.50)  
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.00)  
        with pytest.raises(ValueError):
            Order(customer, coffee, "not_a_number")  

    def test_int_price_works(self):
        customer = Customer("Dave")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 5)  
        
        assert order.price == 5.0