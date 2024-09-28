
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return head
        oldToNew = {}

        pointer = head

        while pointer is not None:
            oldToNew[pointer] = Node(pointer.val)
            pointer = pointer.next

        for oldNode in oldToNew.keys():
            newNode = oldToNew[oldNode]
            newNode.next = oldToNew[oldNode.next] if oldNode.next is not None else None
            newNode.random = oldToNew[oldNode.random]  if oldNode.random is not None else None

        return oldToNew[head]



sol = Solution()
print(sol.copyRandomList(Node(1, Node(2, Node(3)))))