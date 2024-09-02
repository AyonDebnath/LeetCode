class Solution:
    def search(self, nums: [int], target: int) -> int:

        l, r = 0, len(nums) - 1
        lowestTillNow = [nums[0], 0]
        while l <= r:
            m = (l + r) //2
            if nums[m] < lowestTillNow[0]:
                lowestTillNow = [nums[m], m]

            if nums[m] > nums[r]:
                # Go right for the minimum value
                l = m + 1
            else:
                r = m - 1

        if target >= lowestTillNow[0] and target <= nums[-1]:
            l, r = lowestTillNow[1], len(nums) -1
        else:
            l, r = 0, lowestTillNow[1] - 1


        while l <= r:
            m = (l + r) //2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m

        return -1



sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 1))