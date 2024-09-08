# Sharon_Gikenye's coffee_shop
## Introduction.
### Domain Modeling.
This repo models a coffee shop's domain using object oriented programming principles in python. The application consists of three main entitiesinclusing:
> Customer, Coffee and Order
with relationships established between them to  simulate te interactions in a real coffee shop.
## Project Structure
The files containing [coffee class](./coffee.py), [customer class](./customer.py) and [order class](./order.py) are in the root of this directory.
The test files for each class are in the [tests folder](./tests/)

## Installation
1. Clone the repository:
    ```bash
    git clone 
    ```
2. Set up virtual environment using pipenv:
    ```bash
    pipenv install
    pipenv shell
    ```
3. Install dependencies: This project uses pytest for testing:
    ```bash
    pipenv install pytest
    ```
## Classes and methods
1. Implement Initializers and Properties

   - Customer Class (`customer.py`):
     - Initialize a `Customer` with a `name` (string between 1 and 15 characters).
     - Implement a property `name` with the necessary validation.
   - Coffee Class (`coffee.py`):
     - Initialize a `Coffee` with a `name` (string, at least 3 characters long).
     - Implement a property `name` with the necessary validation.
   - Order Class (`order.py`):
     - Initialize an `Order` with a `Customer` instance, a `Coffee` instance, and a `price` (float between 1.0 and 10.0).
     - Implement properties `customer`, `coffee`, and `price` with the necessary validation.

 

2. Define Object Relationship Methods and Properties

   - Implement methods that establish relationships between objects:
     - Order Class (`order.py`):
       - `customer` property returns the `Customer` instance for the order.
       - `coffee` property returns the `Coffee` instance for the order.
     - Coffee Class (`coffee.py`):
       - `orders()` method returns a list of all `Order` instances for that coffee.
       - `customers()` method returns a unique list of `Customer` instances who have ordered that coffee.
     - Customer Class (`customer.py`):
       - `orders()` method returns a list of all `Order` instances for that customer.
       - `coffees()` method returns a unique list of `Coffee` instances that the customer has ordered.

 

3. Implement Aggregate and Association Methods

 - Customer Class (`customer.py`):
     - `create_order(coffee, price)` method: Receives a `Coffee` instance and a price, creates a new `Order` instance, and associates it with that customer and the coffee.
   - Coffee Class (`coffee.py`):
     - `num_orders()` method: Returns the total number of times a coffee has been ordered.
     - `average_price()` method: Returns the average price for a coffee based on its orders.

 

4. Bonus Task (Optional) 

    - Implement the `most_aficionado(coffee)` class method in the `Customer` class:
     - Receives a `coffee` object as an argument.
     - Returns the `Customer` instance that has spent the most money on the provided `coffee`.
     - Returns `None` if there are no customers for the provided `coffee`.