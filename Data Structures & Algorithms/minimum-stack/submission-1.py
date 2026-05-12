class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minV = val if not self.stack else min(val, self.getMin())
        self.stack.append((val, minV))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
