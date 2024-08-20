class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:

        triplets = []
        nums.sort()
        numsMap = {}  # value -> index

        if not nums:
            return []

        if len(nums) < 3:
            return []

        for index, value in enumerate(nums):
            numsMap[value] = index

        for i in range(len(nums) - 2):

            if nums[i] == nums[i + 1] and (-(nums[i] + nums[i+1]) in numsMap.keys()) and (numsMap[-(nums[i] + nums[i+1])] != i or numsMap[-(nums[i] + nums[i+1])] != i+1):
                triplets.append([nums[i], nums[i + 1], -(nums[i] + nums[i+1])])

            elif nums[i] + nums[i + 1] + nums[i + 2] == 0:
                triplets.append([nums[i], nums[i + 1], nums[i + 2]])
        return triplets


sol = Solution()
print(sol.threeSum([0, 0, 0]))