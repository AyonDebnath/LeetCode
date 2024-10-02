# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: 'Optional[ListNode]') -> bool:
        if head is None:
            return False

        loopTester = ListNode(0)

        while head is not None:
            if head.next is None:
                return False
            if head.next == loopTester:
                return True
            temp = head.next
            head.next = loopTester
            head = temp

        return False


