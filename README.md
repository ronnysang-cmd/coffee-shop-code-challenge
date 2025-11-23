# Coffee Shop Domain Model

This is my Python project for modeling a coffee shop using object-oriented programming.

## What it does

I created three classes:
- Customer - people who buy coffee
- Coffee - different types of coffee
- Order - when a customer buys a coffee

## How to run it

1. Go to the coffee_shop folder
2. Run `pipenv install` to install pytest
3. Run `pipenv shell` to activate the virtual environment
4. Run `python debug.py` to test everything

## My Classes

### Customer
- Has a name (1-15 characters)
- Can see all their orders
- Can see what coffees they've ordered
- Can create new orders
- Has a class method to find who spent the most on a coffee

### Coffee  
- Has a name (at least 3 characters)
- Can see all orders for this coffee
- Can see all customers who ordered it
- Can count how many times it was ordered
- Can calculate average price

### Order
- Links a customer and coffee together
- Has a price between $1.00 and $10.00
- All orders are stored in Order.all list

## Testing

I wrote tests for all my classes. Run `pytest` to test everything.

## Files

- customer.py - Customer class
- coffee.py - Coffee class  
- order.py - Order class
- debug.py - Testing script
- tests/ - All my test files

## Author 
- ronny sang# coffee-shop-code-challenge
