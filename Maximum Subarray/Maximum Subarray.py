from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = 0

        for num in nums:
            currSum += num
            if currSum < 0:
                currSum = 0
            maxSum = max (currSum, maxSum)
        return maxSum