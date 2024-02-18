class Solution:
    def groupAnagrams(self, strs):
        sortedStrs = []

        for i in range(len(strs)):
            sortedValue = sorted(strs[i])
            sortedStr = ''.join(sortedValue)
            sortedStrs.append(sortedStr)

        anagramIndexes = {}
        for i in range(len(sortedStrs)):
            if sortedStrs[i] in anagramIndexes:
                anagramIndexes[sortedStrs[i]].append(i)
            else:
                anagramIndexes[sortedStrs[i]] = [i]

        anagrams = []
        for i in anagramIndexes:
            temp = []
            for index in range(len(anagramIndexes[i])):
                temp.append(strs[anagramIndexes[i][index]])
            anagrams.append(temp)

        return anagrams

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))