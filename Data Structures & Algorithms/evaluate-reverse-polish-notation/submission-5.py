class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            print(stack)
            if t in ops:
                r = int(stack.pop())
                l = int(stack.pop())
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    stack.append(int(l / r))
            else:
                stack.append(int(t))
        return int(stack[-1])