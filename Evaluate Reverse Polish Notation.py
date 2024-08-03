
class Solution:

    def evalRPN(self, tokens: []) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        symbolsString = ['+', '-', '*', '/']
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in symbolsString:
                stack.append(tokens[i])
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                operatorString = tokens[i]

                if operatorString == '+':
                    result = int(num1) + int(num2)
                elif operatorString == '-':
                    result = int(num1) - int(num2)
                elif operatorString == '*':
                    result = int(num1) * int(num2)
                elif operatorString == '/':
                    result = int(int(num1) / int(num2))
                stack.append(result)
        return stack.pop()

sol = Solution()
print(sol.evalRPN(["0","3","/"]))