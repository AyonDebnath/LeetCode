# Definition for singly-linked list.
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        pointer1 = list1
        pointer2 = list2

        if pointer1.val < pointer2.val:
            pointer3 = ListNode(pointer1.val, None)
            pointer1 = pointer1.next
        else:
            pointer3 = ListNode(pointer2.val, None)
            pointer2 = pointer2.next
        head = pointer3
        while pointer1 != None and pointer2!= None:
            if pointer1.val < pointer2.val:
                pointer3.next = ListNode(pointer1.val, None)
                pointer3 = pointer3.next
                pointer1 = pointer1.next
            else:
                pointer3.next = ListNode(pointer2.val, None)
                pointer3 = pointer3.next
                pointer2 = pointer2.next



        if pointer1 is not None:
            pointer3.next = pointer1
        elif pointer2 is not None:
            pointer3.next = pointer2

        return head


sol = Solution()
print(sol.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))
