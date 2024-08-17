import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        frontPointer = 0
        backPointer = len(s) - 1
        while frontPointer <= backPointer :
            if not(s[frontPointer].isalnum()):
                frontPointer += 1
                continue
            if not(s[backPointer].isalnum()):
                backPointer -= 1
                continue
            if s[frontPointer] != s[backPointer]:
                return False
            frontPointer += 1
            backPointer -= 1
        return True


sol = Solution()
sol.isPalindrome('Ayon')