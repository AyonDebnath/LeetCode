from copy import deepcopy
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        superset = []

        if len(nums) == 0:
            return []

        self.r_subsets(nums.pop(), nums, superset)
        if [] in superset:
            superset.remove([])
        superset.append([])
        return superset


    def r_subsets(self, num, nums, superset):

        while len(nums) != 0:
            self.r_subsets(nums.pop(), nums, superset)

        superset_copy = deepcopy(superset)
        for i in range(len(superset)):
            temp = deepcopy(superset_copy[i])
            temp.append(num)
            if temp in superset:
                superset_copy[i] = []
                continue
            superset_copy[i].append(num)

        if [num] not in superset:
            superset_copy.append([num])

        superset.extend(superset_copy)


sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))