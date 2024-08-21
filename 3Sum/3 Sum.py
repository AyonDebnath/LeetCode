class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()

        triplets = []
        duplicationAlertFlag = 0
        for i in range((len(nums) - 2)):
            # triplet = [a, b, c]
            a = nums[i]

            if duplicationAlertFlag:
                duplicationAlertFlag = 0
                continue

            if len(nums) > 0 and i < len(nums) -1 and nums[i] == nums[i+1]:
                duplicationAlertFlag = 1

            if i > 0 and nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                continue

            leftPointer = i + 1
            rightPointer = len(nums) - 1

            target = -a
            while leftPointer < rightPointer:
                sum = nums[leftPointer] + nums[rightPointer]
                if sum < target:
                    leftPointer += 1
                elif sum > target:
                    rightPointer -= 1
                elif sum == target:
                    triplets.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    if nums[i] == nums[leftPointer]:
                        duplicationAlertFlag = 0
                    break
        return triplets



sol = Solution()
# print(sol.threeSum([-4, -1,-1,0,1,2]))
# print(sol.threeSum([0,0,0,0]))
print(sol.threeSum([-2,0,1,1,2]))