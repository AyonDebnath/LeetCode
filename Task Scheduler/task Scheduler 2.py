import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-x for x in counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = [] # contains [time, count]

        while q or maxHeap:
            time += 1

            if not maxHeap:
                time = q[0][0]
            else:
                count = 1+heapq.heappop(maxHeap)
                if count != 0:
                    q.append([time+n, count])
            if q and time == q[0][0]:
                count =  q.pop(0)[1]
                heapq.heappush(maxHeap, count)

        return time

sol = Solution()
# print(sol.leastInterval(["B","C","D","A","A","A","A","G"], 1))
print(sol.leastInterval(["A","A","A","B","B","B"], 2))