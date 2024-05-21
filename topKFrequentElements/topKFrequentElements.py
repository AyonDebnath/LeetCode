from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
        counts = list(numCount.values())
        keys = list(numCount.keys())

        frequentItems = []
        for i in range(k):
            maxCountIndex = counts.index(max(counts))
            maxKey = keys[maxCountIndex]
            frequentItems.append(maxKey)
            counts.pop(maxCountIndex)
            keys.pop(maxCountIndex)

        return frequentItems


s = Solution()
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
