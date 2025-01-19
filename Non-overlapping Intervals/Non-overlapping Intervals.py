from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        if len(intervals) <= 1:
            return 0

        count = 0
        lastEnd = intervals[0]

        for interval in intervals[1:]:
            if lastEnd[1] > interval[0]:
                intervals.remove(interval)
                count +=1
            else:
                lastEnd = interval

        return count

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))