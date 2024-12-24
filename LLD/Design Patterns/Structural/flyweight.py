"""
Use case: Assume we are creating a game, such that on click at any point in the screen a tree pops up.
We won't want to create separate tree objects everytime, as it might lead to memory bloating. 
We see that only the x, y coordinates of the tree differ, rest static part remains the same.
Here flyweight comes into play, as it caches the already created trees and reuse it.


Similarly when we design MS Word: we can cache object of each char+type+size and keep reusing it at different x,y positions
"""

class Character:
    """Flyweight class representing a character."""
    def __init__(self, char):
        self.char = char

    def display(self, font, size):
        """Display the character with specific formatting."""
        print(f"Character: {self.char}, Font: {font}, Size: {size}")


class CharacterFactory:
    """Factory for creating and managing Character flyweights."""
    _characters = {}

    @classmethod
    def get_character(cls, char):
        """Get or create a shared instance of a Character."""
        if char not in cls._characters:
            cls._characters[char] = Character(char)
        return cls._characters[char]

    @classmethod
    def get_character_count(cls):
        """Get the total number of unique characters created."""
        return len(cls._characters)


# Client code
class Document:
    """Client class that uses the Character flyweights."""
    def __init__(self):
        self.characters = []

    def add_character(self, char, font, size):
        character = CharacterFactory.get_character(char)
        self.characters.append((character, font, size))

    def render(self):
        """Render the document by displaying all characters."""
        for character, font, size in self.characters:
            character.display(font, size)


# Example usage
if __name__ == "__main__":
    doc = Document()
    doc.add_character('H', 'Arial', 12)
    doc.add_character('e', 'Arial', 12)
    doc.add_character('l', 'Arial', 12)
    doc.add_character('l', 'Arial', 12)
    doc.add_character('o', 'Arial', 12)
    doc.add_character(' ', 'Arial', 12)
    doc.add_character('W', 'Arial', 14)
    doc.add_character('o', 'Arial', 14)
    doc.add_character('r', 'Arial', 14)
    doc.add_character('l', 'Arial', 14)
    doc.add_character('d', 'Arial', 14)

    print(f"Total unique characters created: {CharacterFactory.get_character_count()}")
    print("\nRendering document:")
    doc.render()
