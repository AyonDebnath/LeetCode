class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        maxC = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxC = max(count.values())

            if not (r-l + 1) - maxC <= k:
                count[s[l]] -= 1
                l += 1

            if (r - l + 1) - maxC <= k:
                result = max(result, r - l + 1)

        return result

sol = Solution()
print(sol.characterReplacement("AABABBA", 1))