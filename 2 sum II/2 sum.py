class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        for i in range(len(numbers)):
            j = i + 1
            while j < len(numbers) and numbers[j] <= target - numbers[i] :
                if numbers[j] == target - numbers[i]:
                    return [i+1, j+1]
                j+=1

sol = Solution()
print(sol.twoSum([5,25,75], 100))