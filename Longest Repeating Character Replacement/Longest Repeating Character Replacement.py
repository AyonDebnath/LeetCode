class Solution:
    def getNMaxChar(self, letters):
        nMaxChar = 0
        for letter in letters.keys():
            if letters[letter] > nMaxChar:
                nMaxChar = letters[letter]
        return nMaxChar

    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        letters = {s[0]: 1}
        nMaxChar = 1
        longestSubstring = r - l + 1
        r += 1
        leftIncremented = False
        while r < len(s):
            if s[r] in letters.keys() and not leftIncremented:
                letters[s[r]] += 1
            elif not leftIncremented:
                letters[s[r]] = 1

            if letters[s[r]] > nMaxChar:
                nMaxChar = letters[s[r]]

            if (r - l + 1) - nMaxChar <= k:
                longestSubstring = max(r - l + 1, longestSubstring)
                r += 1
                leftIncremented = False
            else:
                letters[s[l]] -= 1
                l += 1
                leftIncremented = True
                nMaxChar = self.getNMaxChar(letters)
        return longestSubstring

sol = Solution()
print(sol.characterReplacement("ABAA", 0))