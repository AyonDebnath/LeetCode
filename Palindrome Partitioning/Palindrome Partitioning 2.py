import copy
from typing import List


class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    partition.append(s[i:j+1])
                    dfs(i+1)
                    partition.pop()

        dfs(0)

        return res

sol = Solution()
print(sol.partition('aab'))