from typing import List


class Solution:

    def mergeOverlaps(self, range1:List[int], range2:List[int]) -> List[int]:
        a = min(range1[0], range2[0])
        b = max(range1[1], range2[1])
        return [a, b]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals

        intervals.sort()
        curr = intervals[0]
        nxt = intervals[1]
        i = 2
        res = []

        while i < n:
            if curr[1] >= nxt[0]:
                curr = self.mergeOverlaps(curr, nxt)
                nxt = intervals[i]
                i+=1
            else:
                res.append(curr)
                curr = nxt
                nxt = intervals[i]

        if curr[1] >= nxt[0]:
            curr = self.mergeOverlaps(curr, nxt)
            res.append(curr)

        if len(res) == 0:
            return intervals

        return res

sol = Solution()
print(sol.merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))
