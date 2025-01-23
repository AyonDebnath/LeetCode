from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        if len(intervals) <= 1:
            return 0

        count = 0
        prev = intervals[0]
        curr = None

        for interval in intervals[1:]:
            curr = interval
            if prev[1] > curr[0]:
                if prev[1]  > curr[1]:
                    #prev is removed
                    prev = curr
                count +=1
            else:
                prev = curr

        return count

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))