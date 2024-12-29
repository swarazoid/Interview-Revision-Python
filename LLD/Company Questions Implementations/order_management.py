"""
Question:
An order management system for a restaurant is being developed, Implement the IOrder and IOrder System interface as described.

Create a class called Order implementing Order interface.

Create a new class called OrderSystem and implement the Order System interface supporting following use-cases.

Add the order item to the cart

Remove the order item from the cart

Calculate the discounted prices for each order in the cart and sum the values. Discounted Price-Order Price-((Order Price Discount Rate)/100).

Calculate discounts for each product category in the cart. The method returns a map of categories name and the discount amount. (key category, value category discount)

Retrieve the list of items in the cart along with their quantities.

Category determination is done as follows:

Order Price - 10: Cheap

Order Price <- 20 and Order Price > 10: Moderate

Order Price > 20: Expensive

The discount per category is as follows:

Cheap-10%

Moderate-20%

• Expensive-30%

Example

There are 2 Order objects, with name, price,

Pizza 40

Sandwich 30

After they are added, calculate the total amount from orders,

eg. The Price for Pizza-40 and 40>20, so the discount equals 30%. The discounted price=40-((40*30)/100)=28. Similarly, the 30% discounted price of Sandwich is 21.

Output:

Total Amount: 49

Expensive Category Discount: 21

Pizza (1 items)
"""

# Expected solution

class IOrder:
    def get_name(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError

    def get_category(self):
        raise NotImplementedError


class IOrderSystem:
    def add_order(self, order):
        raise NotImplementedError

    def remove_order(self, order):
        raise NotImplementedError

    def calculate_total(self):
        raise NotImplementedError

    def calculate_category_discounts(self):
        raise NotImplementedError

    def get_items(self):
        raise NotImplementedError


class Order(IOrder):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        if self.price <= 10:
            return 'Cheap'
        elif 10 < self.price <= 20:
            return 'Moderate'
        else:
            return 'Expensive'


class OrderSystem(IOrderSystem):
    def __init__(self):
        self.cart = {}

    def add_order(self, order):
        if order.get_name() not in self.cart:
            self.cart[order.get_name()] = {'order': order, 'quantity': 0}
        self.cart[order.get_name()]['quantity'] += 1

    def remove_order(self, order):
        if order.get_name() in self.cart:
            self.cart[order.get_name()]['quantity'] -= 1
            if self.cart[order.get_name()]['quantity'] == 0:
                del self.cart[order.get_name()]

    def calculate_total(self):
        total = 0
        for item in self.cart.values():
            order = item['order']
            quantity = item['quantity']
            discount_rate = self._get_discount_rate(order.get_category())
            discounted_price = order.get_price() - (order.get_price() * discount_rate / 100)
            total += discounted_price * quantity
        return total

    def calculate_category_discounts(self):
        category_discounts = {'Cheap': 0, 'Moderate': 0, 'Expensive': 0}
        for item in self.cart.values():
            order = item['order']
            quantity = item['quantity']
            discount_rate = self._get_discount_rate(order.get_category())
            discounted_price = order.get_price() - (order.get_price() * discount_rate / 100)
            category_discounts[order.get_category()] += (order.get_price() - discounted_price) * quantity
        return category_discounts

    def get_items(self):
        items = {}
        for item in self.cart.values():
            order = item['order']
            quantity = item['quantity']
            items[order.get_name()] = quantity
        return items

    def _get_discount_rate(self, category):
        if category == 'Cheap':
            return 10
        elif category == 'Moderate':
            return 20
        else:
            return 30


# Example usage:
order1 = Order("Pizza", 40)
order2 = Order("Sandwich", 30)

order_system = OrderSystem()
order_system.add_order(order1)
order_system.add_order(order2)

# Calculate total amount after discounts
total_amount = order_system.calculate_total()
print(f"Total Amount: {total_amount}")

# Calculate category discounts
category_discounts = order_system.calculate_category_discounts()
for category, discount in category_discounts.items():
    print(f"{category} Category Discount: {discount}")

# List the items in the cart
items_in_cart = order_system.get_items()
for item, quantity in items_in_cart.items():
    print(f"{item} ({quantity} items)")
