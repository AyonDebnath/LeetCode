from typing import List


class Solution:
    def isPalindrome(self, s:str):
        left, right = 0, len(s)-1
        while s[left] == s[right] and left < right:
            left += 1
            right -= 1

        if left >= right:
            return True
        else:
            return False

    def getSubstrings(self, s):
        lst = []

        def dfs(c, string):
            if c in lst:
                return
            lst.append(c)
            if len(string) == 0:
                return

            if len(string) == 1:
                dfs(c + string[0], '')
            else:
                i2 = 1
                while i2 < len(string) and string[i2-1] == string[i2]:
                    i2 += 1
                dfs(c + string[0], string[i2:])

        s = list(s)
        s.sort()
        for i in range(len(s)):
            dfs(s[i], s)
        return lst

    def partition(self, s: str) -> List[List[str]]:
        pass

sol = Solution()
print(sol.getSubstrings('aba'))