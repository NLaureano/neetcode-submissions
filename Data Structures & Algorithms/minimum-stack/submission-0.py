class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []
        self.size = 0

    def push(self, val: int) -> None:
        if self.size > 0:
            lowestSoFar = self.minimumStack[-1]
            if val < lowestSoFar:
                self.minimumStack.append(val)
            else:
                self.minimumStack.append(lowestSoFar)
        else:
            self.minimumStack.append(val)    
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        self.minimumStack.pop(-1)
        self.stack.pop(-1)
        self.size -= 1
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
        
