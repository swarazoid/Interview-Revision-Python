from collections import deque
from abc import ABC, abstractmethod
from threading import Lock, Thread, Semaphore

class OrderStrategy(ABC):
    @abstractmethod
    def select_restaurant(self, items, restaurants):
        pass

class LowestPriceStrategy(OrderStrategy):
    def select_restaurant(self, item, restaurants):    
        best_restaurant = None
        best_price = float("inf")
        for restaurant in restaurants.values():
                if restaurant.can_fulfill_order(item):
                    if restaurant.menu[item] < best_price:
                        best_price = restaurant.menu[item]
                        best_restaurant = restaurant
        return best_restaurant
        
class Restaurant:
    def __init__(self, name, menu, capacity):
        self.name = name
        self.menu = menu
        self.capacity = capacity
        self.capacity_semaphore = Semaphore(capacity)  # Controls concurrent orders
        self.revenue = 0

    def can_fulfill_order(self, item):
        menu_check = item in self.menu
        capacity_check = self.capacity_semaphore._value > 0
        return menu_check and capacity_check

    def process_order(self, item):
        if not self.capacity_semaphore.acquire(blocking=False):
            raise Exception(f"Not enough capacity to process order at {self.name}.")
        print(f"Order processed at '{self.name}' for item: {item}")

    def replenish_capacity(self):
        self.capacity_semaphore.release()
        print(f"Capacity replenished for '{self.name}'.")

    def update_menu(self, new_menu):
        self.menu = new_menu

class FoodOrderManager:
    def __init__(self):
        self.restaurants = {}
        self.order_id = 1
        self.orders = {}
        self.strategies = {}
        self.order_lock = Lock()
        self.restaurant_lock = Lock()

    def add_restaurant(self, name, menu, capacity):
        with self.restaurant_lock:
            if name not in self.restaurants:
                self.restaurants[name] = Restaurant(name, menu, capacity)
                print(f"Restaurant '{name}' added successfully.")
            else:
                print(f"Restaurant '{name}' already exists!")

    def change_menu(self, restaurant_name, new_menu):
        restaurant = self.restaurants.get(restaurant_name)
        if restaurant:
            restaurant.update_menu(new_menu)
            print(f"Menu for '{restaurant_name}' updated successfully.")
        else:
            print(f"Restaurant '{restaurant_name}' not found!")

    def register_strategy(self, name, strategy):
        if isinstance(strategy, OrderStrategy):
            self.strategies[name] = strategy

    def order(self, order, strategy_name="lowest_price_strategy"):
        with self.order_lock:   
            strategy = self.strategies.get(strategy_name)
            if not strategy:
                print(f"Order strategy '{strategy_name}' not found!")
                return

            for item in order:
                #
                restaurant = strategy.select_restaurant(item, self.restaurants)
                restaurant.process_order(item)
                self.orders[self.order_id] = restaurant
                price = restaurant.menu[item]
                restaurant.revenue += price
                self.order_id += 1

    def fulfill_order(self, order_id):
        restaurant = self.orders[order_id]
        restaurant.replenish_capacity()
        print(f"Order Id#{order_id} fulfilled. Capacity replenished for '{restaurant.name}'.")
        del self.orders[order_id]

    def print_system_stats(self):
        print("System Stats: [Restaurant Name - Capacity Left]")
        for restaurant in self.restaurants.values():
            print(f"{restaurant.name}: {restaurant.capacity_semaphore._value}")

if __name__ == "__main__":
    manager = FoodOrderManager()
    manager.register_strategy("lowest_price_strategy", LowestPriceStrategy())
    manager.add_restaurant("A2B", {"Idly": 40, "Vada": 30, "Paper Plain Dosa": 50}, 4)
    manager.add_restaurant("Rasaganga", {"Idly": 45, "Set Dosa": 60, "Poori": 25}, 6)
    manager.add_restaurant("Eat Fit", {"Idly": 30, "Vada": 40}, 1)

    def place_orders(manager, order):
        manager.order(order["items"], order["strategy"])

    order1 = {
        "items": ["Idly", "Poori"],
        "strategy": "lowest_price_strategy"
    }
    order2 = {
        "items": ["Idly", "Vada"],
        "strategy": "lowest_price_strategy"
    }


    t1 = Thread(target=place_orders, args=(manager, order1))
    t2 = Thread(target=place_orders, args=(manager, order2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    manager.print_system_stats()

    manager.fulfill_order(1)
    manager.print_system_stats()
    
    manager.change_menu("Eat Fit", {"Idly": 60, "Vada": 40})
    manager.order(["Idly"])

    manager.print_system_stats()
