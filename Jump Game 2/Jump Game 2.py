class Solution:
    def jump(self, nums: List[int]) -> int:
        minJump = 1
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1) :
            if nums[i] + i < goal:
                minJump += 1
                goal = i
        return minJump