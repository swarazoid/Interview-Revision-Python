"""
Use case: This is a type of architectural pattern to divide the concerns of the repos
The MVC pattern separates an application into three interconnected components:

Model: Represents the data and business logic.
View: Displays data to the user and captures user input.
Controller: Mediates between the Model and the View, handling user inputs and updating the Model and View.

Here is a Python example implementing a simple TO-DO application using the MVC pattern:
"""

# Model
class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks


# View
class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if tasks:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("\nNo tasks to display.")

    @staticmethod
    def show_message(message):
        print(f"\n{message}")


# Controller
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)
        self.view.show_message(f"Task '{task}' added successfully!")

    def remove_task(self, task_number):
        tasks = self.model.get_tasks()
        if 0 < task_number <= len(tasks):
            task = tasks[task_number - 1]
            self.model.remove_task(task)
            self.view.show_message(f"Task '{task}' removed successfully!")
        else:
            self.view.show_message("Invalid task number.")

    def display_tasks(self):
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)


# Main Application
if __name__ == "__main__":
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            controller.add_task(task)
        elif choice == "2":
            controller.display_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                controller.remove_task(task_number)
            except ValueError:
                view.show_message("Please enter a valid number.")
        elif choice == "3":
            controller.display_tasks()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
