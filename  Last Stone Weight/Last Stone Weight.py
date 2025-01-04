import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negatedStones = [-x for x in stones]
        heapq.heapify(negatedStones)
        if len(stones) == 1:
            return stones[0]



        while(len(negatedStones) >= 2):
            y = heapq.heappop(negatedStones)
            x = heapq.heappop(negatedStones)
            newStone = max(-y + x, -1)
            if newStone != -1 : heapq.heappush(negatedStones, -newStone)

        if len(negatedStones) != 0 :
            return -negatedStones[0]
        else:
            return