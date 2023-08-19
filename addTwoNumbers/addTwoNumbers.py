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
        val1 = 0
        i = l1
        position = 1
        while(i != None) :
            val1 += (i.val)*position
            position *= 10
            i = l1.next

        val2 = 0
        i = l2.val
        position = 1
        while(i != None) :
            val2 += (i.val)*position
            position *= 10
            i = l2.next
        
        
        answer = val1 + val2
        answer = list(filter(lambda i:(i),str(answer)))
        answer.reverse()

        startNode = ListNode() 
        j = 0
        if(len(answer)>0) :
            node = ListNode()
            startNode.val = answer[j] 
            j+=1
            node.val = answer[j]
            startNode.next = node
        j+=1
        while(j < len(answer)):
            temp = ListNode()
            node.val = answer[j]
            node.next = temp
            node = temp
            j += 1

        return startNode