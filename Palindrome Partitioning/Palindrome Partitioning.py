from typing import List


class Solution:
    def isPalindrome(self, s:str):
        if len(s) == 0:
            return False

        left, right = 0, len(s)-1
        while s[left] == s[right] and left < right:
            left += 1
            right -= 1

        if left >= right:
            return True
        else:
            return False

    def getPalindromes(self, nCharacters, string):
        palindromes = []
        s, e = 0, nCharacters
        prev_s = s
        prev_e = 0
        while e < len(string):
            subString1 = string[s:e]
            subString2 = string[prev_s:s]
            if self.isPalindrome(subString1):
                palindromes.append(subString1)
            if self.isPalindrome(subString2):
                palindromes.append(subString2)

            prev_s = s
            s += 1
            prev_e = e
            e = s + nCharacters

        if s < len(string) and prev_e != len(string):
            subString = string[prev_e:]
            if self.isPalindrome(subString):
                palindromes.append(subString)
        return palindromes

    def partition(self, s: str) -> List[List[str]]:
        palindromePartitions = []

        nCharacters = 1
        while nCharacters<= len(s):
            palindrome = self.getPalindromes(nCharacters, s)
            if palindrome :
                palindromePartitions.append(self.getPalindromes(nCharacters, s))
            nCharacters += 1

        return palindromePartitions

sol = Solution()
print(sol.partition('cdd'))