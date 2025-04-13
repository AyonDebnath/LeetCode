from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(i, curr: []):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if sum(curr) > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i + 1, curr)

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1

            curr.pop()
            dfs(i + 1, curr)

        dfs(0, [])
        return res
