class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        longestSubstring = r-l+1
        letters = {s[0]: 0}
        for r in range(1, len(s)):
            if s[r] in letters.keys() and letters[s[r]] >= l:
                longestSubstring = max(longestSubstring, r-l)
                l = letters[s[r]] + 1
                letters[s[r]] = r
            else:
                letters[s[r]] = r
        return max(longestSubstring, r-l+1)


sol = Solution()
print(sol.lengthOfLongestSubstring("dvdf"))
print(sol.lengthOfLongestSubstring("abcabcbb"))