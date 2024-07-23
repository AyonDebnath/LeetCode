import collections


class Solution:
    def longestConsecutive(self, num) :
        numDict = collections.defaultdict(int)
        for i in num:
            numDict[i] = 1
        numSet = collections.defaultdict(set)
        for i in num:
            lst = set()
            lst.add(i)
            if numDict[i-1] != 0:
                lst.add(i-1)
            if numDict[i + 1] != 0:
                lst.add(i+1)


            if numDict[i-1] != 0:
                numSet[i - 1].update(lst)
            if numDict[i + 1] != 0:
                numSet[i + 1].update(lst)
            numSet[i].update(lst)

        return numSet


sol = Solution()
# print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))