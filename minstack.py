class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(self.min_stack[-1], x))
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        self.min_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()