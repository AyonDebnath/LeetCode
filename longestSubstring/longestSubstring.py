class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        substrings = []
        i = 0
        if(len(s) != 0) :
            substring = s[i]
        else:
            substring = ""
        i = 1
        while (i < len(s)):
            if (s[i] not in substring):
                substring += s[i]
            else:
                substrings.append(substring)
                substring = s[i]
            i+=1
        if(len(substring) != 0) :
            substrings.append(substring)
        return len(max(substrings, key = len)) if(len(substrings) != 0) else 0
        # return len(max(substrings, key = len))
 