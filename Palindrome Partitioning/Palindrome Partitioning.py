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

    def partition(self, s: str) -> List[List[str]]:
        pass

