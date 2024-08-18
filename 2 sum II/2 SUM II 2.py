class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        firstPointer = 0
        secondPointer = len(numbers) - 1
        while firstPointer < secondPointer:
            currSum = numbers[firstPointer] + numbers[secondPointer]
            if currSum > target:
                secondPointer -= 1
            elif currSum < target:
                firstPointer += 1
            else:
                return [firstPointer+1, secondPointer+1]