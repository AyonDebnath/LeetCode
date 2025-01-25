from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        currSum = 0
        maxSum = nums[0]

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)
        return maxSum