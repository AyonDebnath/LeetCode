import collections


class Solution:
    def longestConsecutive(self, num):
        print(num)
        numDict = collections.defaultdict(int)
        longestSubstring = 0
        for i in num:
            numDict[i] += 1
        for i in range(len(num)):
            longestSubstringTillNow = 1
            if numDict[num[i] + 1] != 0:
                continue
            j = 1
            while numDict[num[i]-j] != 0:
                longestSubstringTillNow += 1
                j += 1
            if(longestSubstringTillNow > longestSubstring):
                longestSubstring = longestSubstringTillNow
        return longestSubstring


sol = Solution()
# print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
