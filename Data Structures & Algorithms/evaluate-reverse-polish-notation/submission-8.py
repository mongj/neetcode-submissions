class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        stack = []
        for token in tokens:
            if token in ops:
                r, l = stack.pop(), stack.pop()
                val = ops[token](l, r)
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[-1]