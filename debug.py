# Testing my coffee shop classes
from customer import Customer
from coffee import Coffee
from order import Order

# Test creating customers
print("Creating customers...")
customer1 = Customer("Alice")
customer2 = Customer("Bob")
print(f"Created: {customer1.name}, {customer2.name}")

# Test creating coffees
print("\nCreating coffees...")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")
print(f"Created: {coffee1.name}, {coffee2.name}")

# Test creating orders
print("\nCreating orders...")
order1 = Order(customer1, coffee1, 3.50)
order2 = Order(customer2, coffee1, 4.00)
order3 = Order(customer1, coffee2, 5.25)
print("Orders created successfully")

# Test methods
print("\nTesting methods:")
print(f"Alice has {len(customer1.orders())} orders")
print(f"Alice ordered: {[c.name for c in customer1.coffees()]}")
print(f"Espresso has {coffee1.num_orders()} orders")
print(f"Espresso average price: ${coffee1.average_price():.2f}")

# Test create_order
print("\nTesting create_order:")
new_order = customer2.create_order(coffee2, 4.75)
print(f"Bob ordered {new_order.coffee.name} for ${new_order.price}")

# Test most_aficionado
print("\nTesting most_aficionado:")
biggest_fan = Customer.most_aficionado(coffee1)
if biggest_fan:
    print(f"Biggest Espresso fan: {biggest_fan.name}")
else:
    print("No customers found")