class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        result = [0] * len(temperatures)
        monotonicStack = [] # contains (index, temperature)
        for index, temperature in enumerate(temperatures):
            if len(monotonicStack) == 0:
                monotonicStack.append([index, temperature])
                continue

            while monotonicStack and temperature > monotonicStack[-1][1]:
                result[monotonicStack[-1][0]] = index - monotonicStack[-1][0]
                monotonicStack.pop()
            monotonicStack.append([index, temperature])
        return result

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
