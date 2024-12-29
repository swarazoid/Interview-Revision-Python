from enum import Enum
from datetime import datetime
from typing import List

# Enums
class BikeSize(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class ScooterType(Enum):
    ELECTRIC = "Electric"
    GAS = "Gas"


# Base Product class
class Product:
    def __init__(self, product_id: str, name: str, is_rented: bool = False):
        self.product_id: str = product_id
        self.name: str = name
        self.is_rented: bool = is_rented

    def mark_as_rented(self):
        pass

    def mark_as_returned(self):
        pass


# Bike subclass
class Bike(Product):
    def __init__(self, product_id: str, name: str, size: BikeSize):
        super().__init__(product_id, name)
        self.size: BikeSize = size


# Scooter subclass
class Scooter(Product):
    def __init__(self, product_id: str, name: str, scooter_type: ScooterType):
        super().__init__(product_id, name)
        self.scooter_type: ScooterType = scooter_type


# Customer class
class Customer:
    def __init__(self, customer_id: str, name: str, contact: str):
        self.customer_id: str = customer_id
        self.name: str = name
        self.contact: str = contact
        self.balance: float = 0.0

    def add_charge(self, amount: float):
        pass

    def pay_balance(self, amount: float):
        pass


# Rental class
class Rental:
    def __init__(
        self, rental_id: str, product_id: str, customer_id: str, rental_date: datetime, due_date: datetime
    ):
        self.rental_id: str = rental_id
        self.product_id: str = product_id
        self.customer_id: str = customer_id
        self.rental_date: datetime = rental_date
        self.due_date: datetime = due_date
        self.is_returned: bool = False

    def mark_as_returned(self):
        pass


# Inventory class
class Inventory:
    def __init__(self):
        self.products: List[Product] = []
        self.rentals: List[Rental] = []

    # Product-related operations
    def add_product(self, product: Product):
        pass

    def remove_product(self, product_id: str):
        pass

    def get_available_products(self) -> List[Product]:
        pass

    def get_rented_products(self) -> List[Product]:
        pass

    # Rental-related operations
    def rent_product(self, product_id: str, customer_id: str, due_date: datetime):
        pass

    def return_product(self, rental_id: str):
        pass

    def get_customer_rented_products(self, customer_id: str) -> List[Product]:
        pass

    def get_overdue_rentals(self) -> List[Rental]:
        pass


"""
Database Schema:

Products Table:
product_id (Primary Key)
name
type (e.g., bike or scooter)
size (Nullable, for bikes)
scooter_type (Nullable, for scooters)
is_rented (Boolean)

Customers Table:
customer_id (Primary Key)
name
contact
balance

Rentals Table:
rental_id (Primary Key)
product_id (Foreign Key to Products)
customer_id (Foreign Key to Customers)
rental_date
due_date
is_returned (Boolean)
"""

# APIs
# API Schemas for Bike Rental Shop

# ## Product APIs
# - `POST /products/` 
#   - Add a product to the inventory.

# - `DELETE /products/{product_id}` 
#   - Remove a product permanently from the inventory.

# - `GET /products/available` 
#   - Get a list of all available products for rent.

# - `GET /products/rented` 
#   - Get a list of all rented products.

# ## Customer APIs
# - `POST /customers/` 
#   - Add a new customer to the system.

# - `GET /customers/{customer_id}` 
#   - Retrieve customer details by customer ID.

# - `GET /customers/{customer_id}/rented-products` 
#   - Get all products currently rented by a customer.

# ## Rental APIs
# - `POST /rentals/` 
#   - Record a product being rented to a customer.

# - `POST /rentals/{rental_id}/return` 
#   - Mark a product as returned.

# - `GET /rentals/overdue` 
#   - Get all overdue rentals.

# ## Query APIs
# - `GET /query/small-bikes` 
#   - Get the count of small bikes available for rent.

# - `GET /query/available-products` 
#   - List all available products (bikes and scooters) for rent.

# - `GET /query/customer-balance/{customer_id}` 
#   - Check if a customer has an outstanding balance.

# - `GET /query/products-rented` 
#   - List all products currently rented.

# - `GET /query/overdue-products` 
#   - Check which products are overdue for return and who rented them.
