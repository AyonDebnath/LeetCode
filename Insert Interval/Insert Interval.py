from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start < newInterval[0] and end > newInterval[0]:
                pass
            else:
                pass