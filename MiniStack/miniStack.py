class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        pass
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            currentMin = self.minStack[-1]
            if val < currentMin:
                currentMin = val
            self.minStack.append(currentMin)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()