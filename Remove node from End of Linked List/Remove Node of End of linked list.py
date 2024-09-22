# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        length = 0
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next

        n = length - n + 1
        i = 1
        pointer = head
        prev = None
        while i < n:
            prev = pointer
            pointer = pointer.next
            i += 1

        if prev is None and pointer is not None:
            head = pointer.next
        elif prev is None:
            return None
        else:
            prev.next = pointer.next
        return head