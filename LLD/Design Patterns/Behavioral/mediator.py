"""
Use case: It encourages the objects to have loose coupling with other objects using a mediator.

It's not just an adapter between 2 objects. The scope is much more.
for example:
In airline management system. Flights should know about other flights landing and empty parking spots, but they don't talk to each other. They talk to the mediator airline management system.
Another example chat system, where we talk to the mediator chat app server
another example is auction system. where bidders don't talk directly to each other, rather via a mediator.

So the entitites that want to talk to each other are called colleagues.
"""

from abc import ABC, abstractmethod

# Mediator Interface
class AuctionMediator(ABC):
    @abstractmethod
    def add_bidder(self, bidder):
        pass

    @abstractmethod
    def place_bid(self, bidder, amount):
        pass

    @abstractmethod
    def announce_winner(self):
        pass

    @abstractmethod
    def notify_bidders(self, message):
        pass

# Concrete Mediator
class Auction(AuctionMediator):
    def __init__(self):
        self.bidders = []
        self.highest_bid = 0
        self.winning_bidder = None

    def add_bidder(self, bidder):
        self.bidders.append(bidder)

    def place_bid(self, bidder, amount):
        if amount > self.highest_bid:
            self.highest_bid = amount
            self.winning_bidder = bidder
            self.notify_bidders(f"{bidder.name} placed a new highest bid of ${amount}.")
        else:
            print(f"{bidder.name}'s bid of ${amount} was too low.")

    def announce_winner(self):
        if self.winning_bidder:
            print(f"The winner is {self.winning_bidder.name} with a bid of ${self.highest_bid}.")
        else:
            print("No bids were placed.")

    def notify_bidders(self, message):
        for bidder in self.bidders:
            bidder.receive_notification(message)

# Colleague Interface
class Bidder(ABC):
    def __init__(self, name, mediator: AuctionMediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_bidder(self)

    @abstractmethod
    def bid(self, amount):
        pass

    @abstractmethod
    def receive_notification(self, message):
        pass

# Concrete Colleague
class ConcreteBidder(Bidder):
    def bid(self, amount):
        self.mediator.place_bid(self, amount)

    def receive_notification(self, message):
        print(f"{self.name} received notification: {message}")

# Client Code
if __name__ == "__main__":
    auction = Auction()

    bidder1 = ConcreteBidder("Alice", auction)
    bidder2 = ConcreteBidder("Bob", auction)
    bidder3 = ConcreteBidder("Charlie", auction)

    bidder1.bid(100)
    bidder2.bid(150)
    bidder3.bid(120)
    bidder1.bid(200)

    auction.announce_winner()


"""
Here things might look very similar to observer pattern. In that also we notified all the interested objects.

Great observation! The **Mediator** and **Observer** patterns do share similarities in that they both involve communication between objects. However, there are key distinctions in their purpose and how they organize interactions:

### **Mediator Pattern**:
1. **Centralized Communication**:
   - In the Mediator pattern, communication between objects (colleagues) is explicitly coordinated through a central mediator. The mediator encapsulates all the logic for interaction and prevents direct dependencies between colleagues.
   
2. **Purpose**:
   - It is used to reduce the complexity of object relationships by centralizing the interaction logic in a single object.
   - The mediator acts as a controller or manager for all participants, orchestrating their interactions.

3. **Usage**:
   - When you have multiple objects interacting in complex ways, and you want to simplify and centralize their communication.
   - Examples: Chat rooms, auction systems, traffic control systems.

4. **Structure**:
   - Explicitly defines a `Mediator` class that coordinates the interactions.
   - Objects do not communicate directly but always go through the mediator.

---

### **Observer Pattern**:
1. **Decentralized Communication**:
   - In the Observer pattern, an object (subject) maintains a list of dependents (observers) and notifies them of any state changes. The subject doesn't control how observers respond.

2. **Purpose**:
   - It is used to establish a one-to-many dependency, where one object (subject) needs to notify many objects (observers) about changes in its state.
   - The goal is to keep the observers informed, but they decide how to react.

3. **Usage**:
   - When one object needs to notify multiple objects without tightly coupling them.
   - Examples: Event listeners in UI frameworks, data binding in GUIs, stock market ticker systems.

4. **Structure**:
   - Includes a `Subject` (or Publisher) that notifies observers.
   - Observers register themselves with the subject and are notified directly by it.

---

### **Comparison in the Context of the Auction Example**:
1. **Mediator**:
   - The `Auction` class explicitly controls and manages all interactions between bidders. When a bid is placed, the `Auction` decides how to notify other bidders and update the state.
   - The bidders only interact with the mediator and not directly with each other. This centralizes the interaction logic, keeping the bidders decoupled.

2. **Observer**:
   - In an Observer implementation, the bidders would register themselves directly as observers of an `Auction` subject. When a new bid is placed, the `Auction` would broadcast a notification to all observers without any centralized control or interaction logic.
   - The notification is passive—bidders receive the update and decide independently what to do with it.

---

### **When to Use Which?**
- Use the **Mediator Pattern**:
  - When you need **orchestration**: the mediator can enforce specific rules or logic for how participants interact.
  - When the interaction logic is **complex** and you want a centralized place to manage it.
  - Example: An auction system where only higher bids are accepted, and the mediator enforces the rules.

- Use the **Observer Pattern**:
  - When you need **notification**: observers are merely informed of changes and can act independently.
  - When the relationship is **one-to-many**, and the subject doesn’t need to control how observers respond.
  - Example: A stock ticker that updates all registered subscribers whenever a stock price changes.

---

### Summary Table:

| Feature              | Mediator Pattern                          | Observer Pattern                  |
|----------------------|-------------------------------------------|------------------------------------|
| Communication Style  | Centralized                               | Decentralized                     |
| Interaction Logic    | Managed by the mediator                  | Not managed (Observers decide)    |
| Relationship         | Many-to-Many                             | One-to-Many                       |
| Purpose              | Simplify and orchestrate complex interactions | Notify observers of state changes |

In essence, the **Mediator** controls interactions, while the **Observer** facilitates passive updates.

"""