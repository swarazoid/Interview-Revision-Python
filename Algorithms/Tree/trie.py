class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.trie
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode()
            temp = temp.children[letter]
        temp.isEnd = True

    def search(self, word: str) -> bool:
        temp = self.trie
        for letter in word:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return temp.isEnd

    def startsWith(self, prefix: str) -> bool:
        temp = self.trie
        for letter in prefix:
            if letter not in temp.children:
                return False
            temp = temp.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
print(obj.insert(word))
print(obj.search(word))
print(obj.startsWith("app"))