import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        distinctCount = [0]*26
        for task in tasks:
            distinctCount[ord(task) - ord('A')] -= 1
        heapq.heapify(distinctCount)

        waitingQueue = [] # [[time, -remainingCharacterCount]]
        result = []
        while len(distinctCount) != 0 or len(waitingQueue) != 0:
            curr = None
            if len(waitingQueue) != 0 and waitingQueue[0][0] == time:
                curr = -waitingQueue.pop(0)[1]
                result.append('.')
                curr -= 1

                heapq.heappush(distinctCount, -curr)
            else:
                curr = -heapq.heappop(distinctCount)
                if curr == 0 and len(waitingQueue) != 0:
                    result.append('.')

                if curr != 0 :
                    result.append('.')
                    curr -=1
                    if curr != 0:
                        waitingQueue.append([time+n, -curr])

            time += 1

        print(result)
        return len(result)




sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))