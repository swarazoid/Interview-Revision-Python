"""
Use case: When we are creating something in which I might objects to go to their previous state. So we basically store snapshots of the objects to perform undo operations
"""

class Memento:
    """Stores the state of the Originator."""
    def __init__(self, state: dict):
        self._state = state.copy()

    def get_state(self):
        return self._state


class Originator:
    """The object whose state needs to be saved/restored."""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def create_memento(self):
        """Creates a snapshot of the current state."""
        return Memento(self.__dict__)

    def restore(self, memento: Memento):
        """Restores the state from the memento."""
        self.__dict__.update(memento.get_state())

    def __str__(self):
        return f"Originator(name={self.name}, value={self.value})"


class Caretaker:
    """Manages the mementos."""
    def __init__(self):
        self._mementos = []

    def save(self, memento: Memento):
        self._mementos.append(memento)

    def get(self, index: int) -> Memento:
        return self._mementos[index]


# Example Usage
if __name__ == "__main__":
    originator = Originator(name="MyObject", value=42)
    caretaker = Caretaker()

    print("Initial State:", originator)
    
    # Save the initial state
    caretaker.save(originator.create_memento())

    # Change state
    originator.name = "UpdatedObject"
    originator.value = 99
    print("Modified State:", originator)

    # Save the modified state
    caretaker.save(originator.create_memento())

    # Change state again
    originator.name = "AnotherUpdate"
    originator.value = 123
    print("Further Modified State:", originator)

    # Restore to previous state
    originator.restore(caretaker.get(1))
    print("Restored to Second State:", originator)

    # Restore to initial state
    originator.restore(caretaker.get(0))
    print("Restored to Initial State:", originator)


"""
### **Difference Between Command and Memento Patterns**

Both the **Command** and **Memento** patterns can be used for undo/redo functionality, but they differ in purpose, structure, and implementation:

| Aspect                  | **Command Pattern**                                                                                     | **Memento Pattern**                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Purpose**             | Encapsulates actions or operations as objects, allowing them to be parameterized, queued, or logged.    | Captures and restores an object's state without exposing its internal details.                          |
| **Focus**               | Focuses on behavior (actions to be performed).                                                         | Focuses on state (snapshotting and restoring an object's attributes).                                   |
| **Undo/Redo Mechanism** | Achieved by storing a history of commands and invoking `undo()` or `redo()` logic within the commands. | Achieved by storing snapshots of the object's state (mementos) and restoring them as needed.           |
| **Implementation**      | Requires encapsulating each action (including undo/redo) into separate command objects.                | Requires creating a `Memento` class to save and restore object states without exposing implementation.  |
| **Complexity**          | Can become complex as every action and its undo/redo logic must be explicitly defined.                 | Simpler to implement but limited to state changes.                                                     |
| **Use Case Examples**   | - Text editor actions (cut, copy, paste).<br>- Transactions (commit, rollback).                         | - Snapshots of objects in a game.<br>- Restoring configurations or UI states.                          |

---

### **Use Case Comparison**

#### **Command Pattern for Undo/Redo**
The **Command Pattern** is better suited when the focus is on actions, especially if:
- Each action involves complex business logic.
- Different types of actions need to be queued or executed independently.

Example:
- In a text editor, "insert", "delete", and "replace" are actions. Each has its own logic for execution and undo.

---

#### **Memento Pattern for Undo/Redo**
The **Memento Pattern** is more appropriate when:
- The focus is on preserving and restoring the state of an object.
- Actions are not explicitly managed; only the state is rolled back.

Example:
- In a game, saving and loading a game state is a state-focused operation without concern for individual actions.

---

### **When to Use Which?**

1. **Command Pattern**:
   - Use when you need to encapsulate and manage **actions**.
   - You need fine-grained control over operations and their undo logic.
   - Example: Implementing a stack of actions for a text editor.

2. **Memento Pattern**:
   - Use when you need to snapshot and restore the **state** of an object.
   - Suitable for scenarios with no complex action history, just state rollbacks.
   - Example: Saving and loading configurations.

If undo/redo functionality is required for both actions and state, a hybrid approach combining both patterns may be the best solution.
"""