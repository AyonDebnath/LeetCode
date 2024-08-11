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
            while minStack and minStack[-1][0] >= timeToReachTarget:
                inFleet = minStack[-1][-1]
                minStack.pop()
            if not inFleet:
                fleet += 1
            minStack.append([timeToReachTarget, 1])
        temp = []
        for i in minStack:
            if i[-1] == 0:
                temp.append(i)
        minStack = temp
        fleet += len(minStack)
        return fleet


sol = Solution()
print(sol.carFleet(27, [19,25,16,11,23,9,18,0,10,17,3,14,12,20,5], [7,9,6,3,3,5,1,8,3,6,10,4,6,2,6]))
