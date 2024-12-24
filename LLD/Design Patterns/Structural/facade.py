"""
Use case: when we want to hide the system complexity from the client, for eg: car functions
This is one of the most basic design pattern. It just uses many internal complex classes to give an easier interface to customer.
otherwise Client needed to call all those classes step by step to perform the actions
"""

# sample use case: ordering system

# Subsystems remain the same
class ProductDAO:
    def get_product(self, product_id):
        print(f"Fetching product with ID: {product_id}")
        return {"id": product_id, "name": "Laptop", "price": 1000}


class Payment:
    def make_payment(self, product):
        print(f"Processing payment for {product['name']} (${product['price']})")
        return True


class Invoice:
    def generate_invoice(self, product):
        print(f"Generating invoice for {product['name']}")
        return "Invoice12345"


class SendNotification:
    def send_notification(self, message):
        print(f"Sending notification: {message}")


# Facade with Dependency Injection
class OrderFacade:
    def __init__(self, product_dao, payment, invoice, notification):
        self.product_dao = product_dao
        self.payment = payment
        self.invoice = invoice
        self.notification = notification

    def create_order(self, product_id):
        # Step 1: Get the product
        product = self.product_dao.get_product(product_id)

        # Step 2: Process payment
        if self.payment.make_payment(product):
            # Step 3: Generate invoice
            invoice = self.invoice.generate_invoice(product)

            # Step 4: Send notification
            self.notification.send_notification(f"Order successful. Invoice ID: {invoice}")

        print("Order creation successful!")


# Client Code with Dependency Injection
if __name__ == "__main__":
    # Dependencies are created and injected into the facade
    product_dao = ProductDAO()
    payment = Payment()
    invoice = Invoice()
    notification = SendNotification()

    facade = OrderFacade(product_dao, payment, invoice, notification)
    facade.create_order(product_id=121)


