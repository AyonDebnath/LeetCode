class Node:
    def __init__(self, key, val = None):
        self.key = key # Not sure why we need it.
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #maps key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.next = self.right, self.left

    def remove(self, node):
        # the last node from the linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        # insert the node at the beginning of the linked list
        node.prev, node.next = self.right.prev, self.right
        prev = self.right.prev
        prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]