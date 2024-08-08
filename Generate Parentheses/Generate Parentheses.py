class Solution:
    result = []
    def generateParenthesis(self, n: int) -> [str]:
        result = []
        stack = []

        def generate(openN, closeN):
            if openN == closeN == n:
                result.append(''.join(stack))
            if openN < n:
                stack.append('(')
                generate(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                generate(openN, closeN+1)
                stack.pop()

        generate(0, 0)
        return result




sol = Solution()
print(sol.generateParenthesis(3))
