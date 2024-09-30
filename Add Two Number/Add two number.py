# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # reverse the two linked lists

        prev, curr = None, l1

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l1 = prev

        prev, curr = None, l2
        while curr is not None:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        l2 = prev

        head = None
        prev = None
        holder = 0
        while l1 and l2:

            val = l1.val + l2.val + holder
            if val < 10:
                pointer = ListNode(val)
                holder = 0
            else:
                holder = val - 9
                pointer = ListNode(val - 10)

            if prev is None:
                prev = pointer
            else:
                prev.next = pointer
                prev = pointer

            if head is None:
                head = pointer

            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is None:
            prev.next = ListNode(holder)
            return head






        return head
sol = Solution()
print(sol.addTwoNumbers(ListNode(1, ListNode(2, ListNode(2))) , ListNode(1, ListNode(2, ListNode(8)))))