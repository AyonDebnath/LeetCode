from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #find the ranges of indices of all the unique letters

        #find all the non-overlapping ranges and return the count