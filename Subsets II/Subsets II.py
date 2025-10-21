from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # We include the ith element
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # We dont include the ith element
            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1

            backtrack(i+1, subset)

        backtrack(0, [])
        return res

sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))


