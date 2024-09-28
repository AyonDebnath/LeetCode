class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        pointer = head
        originalHM = {}
        newHM = {}
        index = 0
        while pointer is not None:
            originalHM[pointer] = index
            pointerCopy = copy.deepcopy(pointer)
            newHM[index] = pointerCopy
            index += 1
            pointer = pointer.next

        # for index in newHM.keys():
        #     node = newHM[index]
        #
        #     nextIndex = originalHM[node.next]
        #     node.next = newHM[nextIndex]
        #
        #     randomIndex = originalHM[node.random]
        #     node.random = newHM[randomIndex]


        return newHM[0]


        while head is not None:
            print(head.val)
            head = head.next