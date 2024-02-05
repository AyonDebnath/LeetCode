from longestSubstring import *

class Main():
    def main(self) :
        tempObj = Solution()

        s = "abcabcbb"
        print("3 :", tempObj.lengthOfLongestSubstring(s))

        s = "bbbbb"
        print("1 :", tempObj.lengthOfLongestSubstring(s))

        s = "pwwkew"
        print("3 :", tempObj.lengthOfLongestSubstring(s))

        s=""
        print("0 :", tempObj.lengthOfLongestSubstring(s))

        s=" "
        print("1 :", tempObj.lengthOfLongestSubstring(s))

        s="au"
        print("2 :", tempObj.lengthOfLongestSubstring(s))

        s = "dvdf"
        print("3 :", tempObj.lengthOfLongestSubstring(s))
        
        # substring = ""
        # print(substring[0])

obj = Main()
obj.main()