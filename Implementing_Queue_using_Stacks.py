class MyQueue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        
        self.stack1.append(x)

    def pop(self):
        self.move()
        if len(self.stack2) == 0 and len(self.stack1) == 0 :
            return None
        else:
            out = self.stack2[-1]
            self.stack2.pop()
            return out
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.stack2[-1]

    def empty(self):
        return (not self.stack1) and (not self.stack2) 
        
    def move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()