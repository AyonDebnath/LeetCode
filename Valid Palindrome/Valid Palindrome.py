import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        midPoint = len(s) // 2
        frontPointer = 0
        backPointer = len(s) - 1
        while frontPointer <= midPoint and backPointer >= midPoint :
            if s[frontPointer] != s[backPointer]:
                return False
            frontPointer += 1
            backPointer -= 1
        return True


sol = Solution()
sol.isPalindrome('Ayon')