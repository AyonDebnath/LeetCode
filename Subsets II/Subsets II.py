from copy import deepcopy
from typing import List


class Solution:
    superset = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 0:
            self.subsetsWithDup_2(nums[1:], nums[0])
        elif len(nums) == 0:
            return []

        while [] in self.superset:
            self.superset.remove([])

        self.superset.append([])
        temp = deepcopy(self.superset)
        self.superset = None
        return temp

    def subsetsWithDup_2(self, nums, num):
        if len(nums) > 0:
            self.subsetsWithDup_2(nums[1:], nums[0])

        if [num] not in self.superset:
            copy = deepcopy(self.superset)
            for i in range(len(copy)):
                copy[i].append(num)
            copy.append([num])
            self.superset.extend(copy)
        else:
            copy = deepcopy(self.superset)
            for i in range(len(copy)):
                if num not in copy[i] or [num] == copy[i]:
                    copy[i].append(num)
                else:
                    copy[i] = []
            self.superset.extend(copy)

sol = Solution()
print(sol.subsetsWithDup([1, 1, 2, 2]))