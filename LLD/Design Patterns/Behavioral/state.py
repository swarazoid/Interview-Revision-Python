"""
Use case: We use this pattern when the object can go from 1 state to another and we want to avoid too many if else to decide the next state it should go.For eg: Vending machine

The vending machine has multiple states, such as:

Idle: Waiting for the user to insert money.
Collecting Money: Accepting money from the user.
Product Selection: Allowing the user to select a product.
Dispensing Product: Delivering the selected product.
Refunding Change: Returning excess money if any.
Out of Stock/Error: Handling errors or when the machine is out of stock.


In this every state class will follow the same interface and implement the states which can be the next state from the current state.
It can be said it kind of breaks the Interface segregation and Liskov's substitution principle. But we are not actually throwing not implemented error. We need to handle it gracefully to show the error to Customer.
""" 

from abc import ABC, abstractmethod


# Context
class VendingMachine:
    """Vending machine context that maintains the current state."""
    def __init__(self):
        self.state = IdleState()
        self.balance = 0

    def set_state(self, state):
        """Set the current state."""
        self.state = state

    def insert_money(self, amount):
        """Delegate money insertion to the current state."""
        self.state.insert_money(self, amount)

    def select_product(self, product):
        """Delegate product selection to the current state."""
        self.state.select_product(self, product)

    def dispense_product(self):
        """Delegate product dispensing to the current state."""
        self.state.dispense_product(self)

    def refund(self):
        """Delegate refunding to the current state."""
        self.state.refund(self)


# State Interface
class State(ABC):
    """Abstract base class for all states."""
    @abstractmethod
    def insert_money(self, machine, amount):
        pass

    @abstractmethod
    def select_product(self, machine, product):
        pass

    @abstractmethod
    def dispense_product(self, machine):
        pass

    @abstractmethod
    def refund(self, machine):
        pass


# Concrete States
class IdleState(State):
    def insert_money(self, machine, amount):
        print(f"Money inserted: ${amount}")
        machine.balance += amount
        machine.set_state(CollectingMoneyState())

    def select_product(self, machine, product):
        print("Please insert money first.")

    def dispense_product(self, machine):
        print("Please insert money and select a product first.")

    def refund(self, machine):
        print("No money to refund.")


class CollectingMoneyState(State):
    def insert_money(self, machine, amount):
        print(f"Additional money inserted: ${amount}")
        machine.balance += amount

    def select_product(self, machine, product):
        print(f"Product '{product}' selected.")
        machine.set_state(ProductSelectionState(product))

    def dispense_product(self, machine):
        print("Please select a product first.")

    def refund(self, machine):
        print(f"Refunding ${machine.balance}")
        machine.balance = 0
        machine.set_state(IdleState())


class ProductSelectionState(State):
    def __init__(self, product):
        self.product = product

    def insert_money(self, machine, amount):
        print("Cannot insert money after product selection.")

    def select_product(self, machine, product):
        print("Product already selected.")

    def dispense_product(self, machine):
        if machine.balance >= 2:  # Assume all products cost $2
            print(f"Dispensing product: {self.product}")
            machine.balance -= 2
            machine.set_state(RefundingChangeState())
        else:
            print("Insufficient balance. Please insert more money.")
            machine.set_state(CollectingMoneyState())

    def refund(self, machine):
        print(f"Refunding ${machine.balance}")
        machine.balance = 0
        machine.set_state(IdleState())


class RefundingChangeState(State):
    def insert_money(self, machine, amount):
        print("Cannot insert money while refunding change.")

    def select_product(self, machine, product):
        print("Cannot select product while refunding change.")

    def dispense_product(self, machine):
        print("Product already dispensed.")

    def refund(self, machine):
        if machine.balance > 0:
            print(f"Refunding change: ${machine.balance}")
        else:
            print("No change to refund.")
        machine.balance = 0
        machine.set_state(IdleState())


# Client Code
if __name__ == "__main__":
    vending_machine = VendingMachine()

    # Test scenario
    vending_machine.insert_money(1)  # Insert $1
    vending_machine.select_product("Soda")  # Select a product
    vending_machine.insert_money(2)  # Insert additional $2
    vending_machine.dispense_product()  # Dispense the product
    vending_machine.refund()  # Refund change if any
