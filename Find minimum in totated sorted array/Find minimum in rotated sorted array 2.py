class Solution:
    def findMin(self, nums: [int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l+r) // 2
        lowestTillNow = nums[m]

        while l <= r:
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
            if nums[m] < lowestTillNow:
                lowestTillNow = nums[m]

        return lowestTillNow



sol = Solution()
print(sol.findMin([4,5,6,7,0,1,2]))