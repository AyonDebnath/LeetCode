class Solution:
    def twoSum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            nums_hash[str(nums[i])] = i
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if str(num2) in nums_hash.keys():
                if nums_hash[str(num2)] != i:
                    return [i, nums_hash[str(num2)]]
        return


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
