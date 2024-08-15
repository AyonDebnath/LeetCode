class Solution:

    def getTimeToReachTarget(self, d0, speed, target):
        return (target - d0) / speed
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        hasMap = {}
        minStack = []
        fleet = 0
        for idx, pos in enumerate(position):
            hasMap[pos] = idx
        position.sort(reverse = True)
        for d0 in position:
            timeToReachTarget = self.getTimeToReachTarget(d0, speed[hasMap[d0]], target)
            if not minStack:
                minStack.append([timeToReachTarget, 0])
                continue
            elif minStack[-1][0] < timeToReachTarget:
                minStack.append([timeToReachTarget, 0])
                continue
            if minStack and minStack[-1][0] >= timeToReachTarget:
                inFleet = minStack[-1][-1]
                minStack[-1][-1] = 1
            if not inFleet:
                fleet += 1
        temp = []
        for i in minStack:
            if i[-1] == 0:
                temp.append(i)
        minStack = temp
        fleet += len(minStack)
        return fleet


sol = Solution()
print(sol.carFleet(10, [0,4,2], [2,1,3]))
