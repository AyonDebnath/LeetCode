# Definition for singly-linked list.
import copy
'''

TIME LIMIT EXCEEDED

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head.next is None:
            return

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
        length += 1
        headRvrsd = pointer


        pointer1 = head
        pointer2 = headRvrsd
        for i in range(length//2):
            temp = pointer1.next
            tail = pointer1.next
            pointer1.next = pointer2
            pointer1 = temp

            if length %2 == 0 and i == length//2 -1 :
                tail = pointer2
                break

            temp = pointer2.next
            pointer2.next = pointer1
            pointer2 = temp


        tail.next = None
        while head is not None:
            print(head.val)
            head = head.next
sol = Solution()
print(sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))