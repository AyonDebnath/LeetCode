from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        currSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            currSum += num
            if currSum < 0:
                currSum = 0
            maxSum = max(currSum, maxSum)
        return maxSum