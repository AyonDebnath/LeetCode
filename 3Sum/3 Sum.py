class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()

        triplets = []
        duplicationAlertFlag = 0
        for i in range((len(nums) - 2)):
            # triplet = [a, b, c]
            a = nums[i]

            if i > 0 and nums[i] == nums[i-1] :
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

                    originalLeftPointer = leftPointer
                    leftPointer += 1
                    while(leftPointer < len(nums) and nums[originalLeftPointer] == nums[leftPointer]):
                        leftPointer += 1
                    originalRightPointer = 1
                    rightPointer -= 1
                    while (rightPointer > 0 and nums[originalRightPointer] == nums[rightPointer]):
                        rightPointer -= 1
        return triplets



sol = Solution()
print(sol.threeSum([-4, -1,-1,0,1,2]))
print(sol.threeSum([0,0,0,0]))
print(sol.threeSum([-2,0,1,1,2]))