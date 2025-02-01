import heapq
from tokenize import group
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = {}
        for n in hand:
            counter[n] = 1 + counter.get(n, 0)

        minHeap = list(counter.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]
            for i in range(first, first+groupSize):
                if i not in counter.keys():
                    return False
                counter[i] = counter[i] - 1
                if counter[i] == 0:
                    if i != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)
        return True




sol = Solution()
# sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
sol.isNStraightHand([8,10,12], 3)