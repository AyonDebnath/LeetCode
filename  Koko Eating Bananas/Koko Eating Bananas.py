import math
class Solution:

    def timeToFinishPile(self, k: int, piles: [int]):
        if len(piles) == 0:
            return 0
        time = 0
        for i in range(len(piles)):
            time += math.ceil(piles[i] / k)

        return time

    def getMax(self, piles):
        if not(piles):
            return -1

        maxElement = piles[0]
        for i in range(len(piles)):
            if piles[i] > maxElement:
                maxElement = piles[i]
        return maxElement

    def minEatingSpeed(self, piles: [int], h: int) -> int:
        l = 1
        r = self.getMax(piles)
        k = -1
        while l <= r:
            m = (l + r) // 2
            time_m = self.timeToFinishPile(m, piles)
            if time_m > h:
                l = m + 1
            elif time_m <= h:
                r = m - 1
                k = m
        return k


sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))
