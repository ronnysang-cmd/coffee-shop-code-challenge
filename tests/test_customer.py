import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def setup_method(self):
        Order.all = []

    def test_customer_name(self):
        customer = Customer("John")
        assert customer.name == "John"

    def test_bad_names(self):
        with pytest.raises(ValueError):
            Customer("")  
        with pytest.raises(ValueError):
            Customer("ThisNameIsTooLong")  
        with pytest.raises(ValueError):
            Customer(123)  

    def test_customer_orders_method(self):
        customer = Customer("Alice")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 3.50)
        
        orders = customer.orders()
        assert len(orders) == 1
        assert orders[0] == order

    def test_customer_coffees_method(self):
        customer = Customer("Bob")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        Order(customer, coffee1, 3.50)
        Order(customer, coffee2, 4.00)
        
        coffees = customer.coffees()
        assert len(coffees) == 2

    def test_create_order_method(self):
        customer = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        order = customer.create_order(coffee, 4.25)
        
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.25

    def test_most_aficionado_method(self):
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        coffee = Coffee("Espresso")
        
        Order(customer1, coffee, 3.50)
        Order(customer2, coffee, 4.00)
        Order(customer1, coffee, 2.75)
        
        result = Customer.most_aficionado(coffee)
        assert result == customer1

    def test_most_aficionado_none(self):
        coffee = Coffee("Mocha")
        result = Customer.most_aficionado(coffee)
        assert result is None