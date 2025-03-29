from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIndex = {} # char -> lastIndex

        for i in range(len(s)):
            lastIndex[s[i]] = i

        start = 0
        end = 0
        prev = 0
        output = []
        for i in range(len(s)):
            start += 1
            end = max(end, lastIndex[s[i]])

            if i == end:
                output.append(start)
                start = 0
                prev = start

        return output