class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # can be solved in time complexity O(n) and memory complexity O(n) using hashmaps.
        # The interviwer might tell you to write your own sorting algorithm.

        s = sorted(s)
        t = sorted(t)

        return s == t



if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram('rat', 'car'))
    print(s.isAnagram('anagram', 'nagaram'))