# Definition for singly-linked list.
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        pointer = copy.deepcopy(head)
        nextNode = copy.deepcopy(head.next)
        pointer.next = None
        length = 0
        while nextNode is not None:
            length += 1
            temp = copy.deepcopy(nextNode.next)
            nextNode.next = pointer
            pointer = nextNode
            nextNode = temp
        headRvrsd = pointer


        pointer1 = head
        pointer2 = headRvrsd
        for i in range(length//2 + 1):
            temp = pointer1.next
            pointer1.next = pointer2
            pointer1 = temp


            if i == length//2 + 1:
                continue

            temp = pointer2.next
            pointer2.next = pointer1
            pointer2 = temp


        while head is not None:
            print(head.val)
            head = head.next



sol = Solution()
print(sol.reorderList(ListNode(1, ListNode(2, ListNode(3)))))