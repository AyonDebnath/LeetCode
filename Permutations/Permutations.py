from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for i in range(len(perms)):
            for j in range(len(perms[i])+1):
                p_copy = perms[i].copy()
                p_copy.insert(j, nums[0])
                res.append(p_copy)
        return res