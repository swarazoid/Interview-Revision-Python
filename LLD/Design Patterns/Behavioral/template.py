"""
Use case: When we want all classes to follow a specific steps to perform a task, but also allow the steps implementation to be different
Example: There is a send_money method in some UPI class.
I can send money to friend or merchant. The app has decided 4 steps to transfer
check balance -> debit money -> debit convenience fees -> credit money.
So every class who is implementing the send_money must have these 4 functions called in order
"""

from abc import ABC, abstractmethod

class UPISendMoneyTemplate(ABC):
    """Abstract base class that defines the template method for sending money."""
    
    def send_money(self, amount):
        """Template method defining the steps to transfer money."""
        print("Initiating money transfer...")
        self.check_balance(amount)
        self.debit_money(amount)
        self.debit_convenience_fees(amount)
        self.credit_money(amount)
        print("Money transfer complete.\n")

    @abstractmethod
    def check_balance(self, amount):
        """Check if the account has sufficient balance."""
        pass

    @abstractmethod
    def debit_money(self, amount):
        """Debit the specified amount from the sender's account."""
        pass

    @abstractmethod
    def debit_convenience_fees(self, amount):
        """Debit any applicable convenience fees."""
        pass

    @abstractmethod
    def credit_money(self, amount):
        """Credit the money to the recipient's account."""
        pass


class SendToFriend(UPISendMoneyTemplate):
    """Implementation for sending money to a friend."""
    
    def check_balance(self, amount):
        print(f"Checking balance for ₹{amount}...")

    def debit_money(self, amount):
        print(f"Debiting ₹{amount} from your account...")

    def debit_convenience_fees(self, amount):
        print("No convenience fee for sending money to a friend.")

    def credit_money(self, amount):
        print(f"Crediting ₹{amount} to your friend's account...")


class SendToMerchant(UPISendMoneyTemplate):
    """Implementation for sending money to a merchant."""
    
    def check_balance(self, amount):
        print(f"Checking balance for ₹{amount}...")

    def debit_money(self, amount):
        print(f"Debiting ₹{amount} from your account...")

    def debit_convenience_fees(self, amount):
        print("Debiting a convenience fee of ₹5 for sending to a merchant.")

    def credit_money(self, amount):
        print(f"Crediting ₹{amount} to the merchant's account...")


# Example Usage
if __name__ == "__main__":
    print("Sending money to a friend:")
    friend_transfer = SendToFriend()
    friend_transfer.send_money(500)
    
    print("Sending money to a merchant:")
    merchant_transfer = SendToMerchant()
    merchant_transfer.send_money(1000)


"""
But what if someone overrides the send_money in their class itself?
Mark send_money as final - In Python, you can't directly mark methods as final (like in some other languages such as Java), but you can simulate it by:
- Raising a NotImplementedError if send_money is overridden.
- Alternatively, documenting and enforcing that send_money should not be overridden.

class UPISendMoneyTemplate(ABC):
    def send_money(self, amount):
        ""Template method defining the steps to transfer money. Should not be overridden.""
        print("Initiating money transfer...")
        self.check_balance(amount)
        self.debit_money(amount)
        self.debit_convenience_fees(amount)
        self.credit_money(amount)
        print("Money transfer complete.\n")

    @abstractmethod
    def check_balance(self, amount):
        pass

    @abstractmethod
    def debit_money(self, amount):
        pass

    @abstractmethod
    def debit_convenience_fees(self, amount):
        pass

    @abstractmethod
    def credit_money(self, amount):
        pass

    def __init_subclass__(cls, **kwargs):
        ""Prevent overriding send_money in subclasses.""
        super().__init_subclass__(**kwargs)
        if "send_money" in cls.__dict__:
            raise TypeError(f"Overriding 'send_money' in {cls.__name__} is not allowed.")

"""