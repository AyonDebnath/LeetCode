class Node:
    def __init__(self):
        self.children = {} # character -> Node/None
        self.endNode = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr[c] = Node()
            curr = curr[c]
        curr.endNode = True


    def search(self, word: str) -> bool:
        curr = self.root


    def startsWith(self, prefix: str) -> bool:

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)