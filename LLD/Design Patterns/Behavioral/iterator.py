"""
Use case: When you create a custom data structure or collection and want to provide an easy way to traverse its elements.
Real-Life Examples:

Media Playlists:
Iterating through songs in a playlist, skipping or replaying tracks.

Library Management Systems:
Iterating over books, magazines, or journals in a library database.

Game Development:
Iterating through game objects, players, or levels in a game engine.

Most used exmaple would be the Python libraries itself like list, set, dictionary. These store data in different formats, but we can simply iterate on them and get next values through their iterator implmentation
"""

# sample use case: Library 

from collections.abc import Iterator, Iterable

# Custom Iterable Collection
class BookCollection(Iterable):
    def __init__(self):
        self._books = []

    def add_book(self, book: str):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

# Custom Iterator
class BookIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

# Client Code
if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book("The Catcher in the Rye")
    collection.add_book("To Kill a Mockingbird")
    collection.add_book("1984")

    print("Books in the collection:")
    for book in collection:
        print(book)
