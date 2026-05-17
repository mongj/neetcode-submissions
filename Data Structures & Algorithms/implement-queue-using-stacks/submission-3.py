class MyQueue:

    def __init__(self):
        self.stack = []
        self.head = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.head += 1
        return self.stack[self.head - 1]

    def peek(self) -> int:
        return self.stack[self.head]

    def empty(self) -> bool:
        return len(self.stack[self.head:]) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()