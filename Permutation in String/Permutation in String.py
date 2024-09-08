import copy


class Solution:

    def getFrequency(self, s):
        dict = {}
        for s in s:
            dict[s] = 1 + dict.get(s, 0)

        return dict
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = self.getFrequency(s1)
        s1Cpy = list(s1)
        started = False

        i = 0
        while i < len(s2):
            if started == True and s2[i] not in s1Cpy:
                if s2[i] in s1:
                    i = startIndex + 1
                    s1Cpy = list(s1)[i:]
                else:
                    return False

            if s2[i] in s1Cpy:
                if not started:
                    startIndex = i
                    started = True

                s1Cpy.remove(s2[i])
                if s1Cpy == []:
                    return True
            i+=1

        if s1Cpy == []:
            return True
        else:
            return False

sol = Solution()
# print(sol.checkInclusion("adc", "dcda"))

print(sol.checkInclusion("hello", "ooolleoooleh"))



