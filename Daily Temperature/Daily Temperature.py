class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        answer = []
        for i in range(len(temperatures)):
            if i == len(temperatures) - 1:
                answer.append(0)
            j = i + 1
            count = 0
            while j < len(temperatures):
                count += 1
                if temperatures[j] > temperatures[i]:
                    answer.append(count)
                    break
                elif j == len(temperatures) - 1:
                    answer.append(0)
                j += 1
        return answer


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
