import heapq
import math
from typing import List


def getDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancePoints = []
        for point in points:
            temp = []
            temp.append(getDistance(point, [0, 0]))
            temp.extend(point)
            distancePoints.append(temp)

        heapq.heapify(distancePoints)
        kClosestPoints = []
        for i in range(k):
            temp = heapq.heappop(distancePoints)
            kClosestPoints.append(temp[1:])
        return kClosestPoints


# sol = Solution()
# print(sol.kClosest([[2,2],[2,2],[3,3],[2,-2],[1,1]], 4))