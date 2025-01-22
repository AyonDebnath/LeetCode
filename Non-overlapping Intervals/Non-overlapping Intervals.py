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
print(sol.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],
                                 [-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))