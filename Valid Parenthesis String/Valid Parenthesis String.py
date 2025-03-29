class Solution:
    def checkValidString(self, s: str) -> bool:
        left= []
        asterisk = []

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                asterisk.append(i)
            elif s[i] == ")":
                if len(left) > 0:
                    left.pop()
                elif len(asterisk) > 0:
                    asterisk.pop()
                else:
                    return False

        while left and asterisk:
            if left.pop() > asterisk.pop():
                return False
        return len(left)==0


sol = Solution()
# sol.checkValidString("(((((*(*********((*(((((****")
print(sol.checkValidString("()"))
