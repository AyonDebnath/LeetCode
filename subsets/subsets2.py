from copy import deepcopy
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        superset = []

        if len(nums) == 0:
            return []

        self.r_subsets(nums.pop(), nums, superset)
        superset.append([])
        return superset


    def r_subsets(self, num, nums, superset):

        while len(nums) != 0:
            self.r_subsets(nums.pop(), nums, superset)

        superset_copy = deepcopy(superset)
        for i in range(len(superset)):
            superset_copy[i].append(num)
        superset_copy.append([num])
        superset.extend(superset_copy)



sol = Solution()
print(sol.subsets([1, 2, 3]))
# print(sol.subsets([0]))





