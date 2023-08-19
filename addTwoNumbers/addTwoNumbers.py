from ListNode import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        i = 0
        val1 = l1.val
        val2 = l2.val
        startNode = ListNode()
        startNode.val = val1 + val2

        if(startNode.val > 9) :
            startNode.val = startNode.val - 10
            carry = 1
        else :
            carry = 0

        node1 = l1.next
        node2 = l2.next
        tempNode = ListNode()
        if(node1==None and node2 == None and carry == 1) :
            startNode.next = tempNode
            tempNode.val = carry
            return startNode
        if (node1!=None or node2 != None):
            startNode.next = tempNode
        
        while(node1 != None or node2 != None) :
            val1 = (node1.val if node1 is not None else node1)
            val2 = (node2.val if node2 is not None else node2)
            tempValue = (0 if val1 is None else val1) + (0 if val2 is None else val2) + carry
            if(tempValue > 9):
                tempNode.val = tempValue - 10 
                carry = 1
            else:
                tempNode.val = tempValue
                carry = 0
            node1 = node1.next if node1 is not  None else node1
            node2 = node2.next if node2 is not None else node2
            if (node1 != None or node2 != None):
                temp = ListNode()
                tempNode.next = temp
                tempNode = temp
        if(carry == 1):
            tempNode.next = ListNode()
            tempNode.next.val = 1
        return startNode
    
