class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node()
            curr = curr.children[letter]
        curr.isWord = True

    def dfs(self, startIndex, currNode, word):

        for i in range(startIndex, len(word)):
            if word[i] == ".":
                for node in currNode.children.values():
                    if(self.dfs(i+1, node, word)):
                        return True
                return False
            elif word[i] not in currNode.children:
                return False
            else:
                currNode = currNode.children[word[i]]
        return currNode.isWord

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)