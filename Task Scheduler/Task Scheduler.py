import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 1

        distinctCount = [0]*26
        for task in tasks:
            distinctCount[ord(task) - ord('A')] -= 1
        heapq.heapify(distinctCount)

        waitingQueue = [] # [[time, -remainingCharacterCount]]
        result = []
        while sum(distinctCount) < 0 or len(waitingQueue) != 0:
            curr = None
            if len(waitingQueue) > 0 and waitingQueue[0][0] == time:
                curr = -waitingQueue.pop(0)[1]
                result.append('.')
                curr -= 1
                if curr != 0:
                    waitingQueue.append([time + n + 1, -curr])
            elif sum(distinctCount) < 0:
                curr = -heapq.heappop(distinctCount)
                result.append('.')
                curr -=1
                if curr != 0:
                    waitingQueue.append([time+n+1, -curr])
            elif sum(distinctCount) == 0:
                result.append('.')

            time += 1

        print(result)
        return len(result)




sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))