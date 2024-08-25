class Solution:
    def maxArea(self, height: [int]) -> int:
        leftPointer = 0
        rightPointer = len(height) - 1
        maxArea = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
        while leftPointer < rightPointer:
            area = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
            if area > maxArea :
                maxArea = area
            if height[leftPointer] < height[rightPointer]:
                leftPointer += 1
            elif height[leftPointer] >= height[rightPointer]:
                rightPointer -= 1
        return maxArea



sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7]))