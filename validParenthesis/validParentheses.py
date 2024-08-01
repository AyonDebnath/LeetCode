class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ['(', '{', "["]:
                stack.append(char)
            else:
                closingBracket = char
                if(len(stack) == 0):
                    return False
                openingBracket = stack.pop()
                if(closingBracket == ')' and openingBracket != '('):
                    return False
                elif (closingBracket == '}' and openingBracket != '{'):
                    return False
                elif (closingBracket == '}' and openingBracket != '['):
                    return False
        if(len(stack) == 0):
            return True
        else:
            return False



