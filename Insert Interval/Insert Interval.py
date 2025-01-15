from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        started = False
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            temp = []

            if start < newInterval[0] < end and not started:
                temp.append(start)
                started = True
            elif start < newInterval[1] < end and not started:
                pass
            elif newInterval[1] < start and not started:
                pass
            else:
                output.append(interval)