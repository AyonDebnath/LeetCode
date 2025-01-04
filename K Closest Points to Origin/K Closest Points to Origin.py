import heapq
import math
from typing import List


def getDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            distances.append(getDistance(points[i], [0, 0]))

        pointsAndDistances = {}
        for i in range(len(points)):
            pointsAndDistances[str(points[i])] = distances[i]

        kDistances = {}
        heapq.heapify(distances)
        for i in range(k):
            kDistances[heapq.heappop(distances)] = 0

        i = 0
        kDistancesPoints = []
        for key in pointsAndDistances.keys():
            if pointsAndDistances[key] in kDistances:
                kDistancesPoints.append(key)
        return kDistancesPoints


