# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head == None:
            return ListNode()
        prevNode = head
        nextNode = head.next
        head.next = None
        while nextNode != None:
            tempNextNode = nextNode.next
            nextNode.next = prevNode
            prevNode = nextNode
            if tempNextNode == None:
                head = nextNode
            nextNode = tempNextNode
        nextNode = head.next
        while nextNode != None:
            print(nextNode.val)
            nextNode = nextNode.next
        return head



sol = Solution()
print(sol.reverseList(ListNode(1, ListNode(2, ListNode(3)))))