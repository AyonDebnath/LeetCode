# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        prev = None
        holder = 0
        while l1 or l2:
            if l1 is None:
                val = 0 + l2.val + holder
            elif l2 is None:
                val = l1.val + 0 + holder
            else:
                val = l1.val + l2.val + holder
            if val < 10:
                pointer = ListNode(val)
                holder = 0
            else:
                holder = 1
                pointer = ListNode(val - 10)

            if prev is None:
                prev = pointer
            else:
                prev.next = pointer
                prev = pointer

            if head is None:
                head = pointer

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if holder == 1:
            prev.next = ListNode(holder)
            return head

        return head
sol = Solution()
print(sol.addTwoNumbers(ListNode(9, ListNode(9, ListNode(2))) , ListNode(1, ListNode(2, ListNode(8)))))