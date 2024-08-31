class Solution:
    def findMin(self, nums: [int]) -> int:
        l, r = 0, len(nums) - 1
        lowestTillNow = nums[0]

        while l <= r:
            m = (l + r) // 2
            if nums[m] < lowestTillNow:
                lowestTillNow = nums[m]

            if nums[l] > nums[m] :
                r = m - 1
            elif nums[l] < nums[m] and nums[r] > nums[m]:
                r = m - 1
            else:
                l = m + 1

        return lowestTillNow


sol = Solution()
print(sol.findMin([4,5,6,7,0,1,2]))