class Node :
    def __init__(self, val1, val2 = None, next = None):
        self.val1 = val1
        self.val2 = val2
        self.next = next

class BFS:
    def hasChild(self, node):
        return node.next is not None

    def printBFS(self, root):

        print(
            root.val1,
            root.val2,
            end=""
        )

        while self.hasChild(root):
            for node in [root.val1, root.val2]:
                if node is None:
                    continue
                self.printBFS(node)







if __name__ == "__main__":
    root = Node(5, 6, Node(2, next = Node(2, 3)))
    bfs = BFS()
    bfs.printBFS(root)