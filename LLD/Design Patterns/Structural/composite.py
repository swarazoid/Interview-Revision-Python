"""
Use case: This is mostly used when there is a heirarchy of objects, eg: Emlployee lists, File Lists

The Composite Design Pattern is used to represent part-whole hierarchies, where individual objects (leaves) and compositions of objects (composites) can be treated uniformly. It is particularly useful for file systems, where directories can contain files or other directories.
"""


from abc import ABC, abstractmethod

# Component
class FileSystemItem(ABC):
    """Abstract base class for file system items (files and directories)."""
    @abstractmethod
    def display(self, indent=0):
        """Display the item with indentation based on its hierarchy level."""
        pass

# Leaf
class File(FileSystemItem):
    """Represents a file in the file system."""
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name} (Size: {self.size} bytes)")

# Composite
class Directory(FileSystemItem):
    """Represents a directory in the file system."""
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        """Add a file or directory to the directory."""
        self.children.append(item)

    def remove(self, item):
        """Remove a file or directory from the directory."""
        self.children.remove(item)

    def display(self, indent=0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 4)

# Client code
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt", 1200)
    file2 = File("file2.txt", 800)
    file3 = File("image.png", 2000)

    # Create directories
    root = Directory("root")
    home = Directory("home")
    user = Directory("user")
    documents = Directory("documents")
    pictures = Directory("pictures")

    # Build the file system hierarchy
    root.add(home)
    home.add(user)
    user.add(documents)
    user.add(pictures)
    documents.add(file1)
    documents.add(file2)
    pictures.add(file3)

    # Display the file system
    print("File System Structure:")
    root.display()
