class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        i = (l+r)//2
        while r >= l:
            if target > nums[i]:
                l = i+1
            elif target < nums[i]:
                r = i-1
            elif target == nums[i]:
                break
            i = (l+r)//2
        if nums[i] == target:
            return i
        return -1

sol = Solution()
print(sol.search([2, 5], 0))