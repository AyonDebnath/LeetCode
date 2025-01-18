from typing import List


class Solution:

    def mergeOverlaps(self, range1:List[int], range2:List[int]) -> List[int]:
        pass

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        n = len(intervals)

        if n < 2:
            return intervals

        curr = intervals[0]
        next = intervals[1]
        i = 2
        res = []

        while i < n:

            # if curr and next overlaps
            #   curr = new_interval
            #   next = intervals[i]
            #   i++
            # else
            #   res.append(curr)
            #   curr = next
            #   next = intervals[i]

    # if curr and next overlaps:
    #   curr = new_interval
    #   res.append(curr)

